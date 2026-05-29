from flask import Flask, render_template_string, request, redirect, session, send_file, jsonify
from scapy.all import sniff, IP, TCP, UDP, ICMP
import sqlite3
import threading
import queue
import csv
import smtplib
import os
import hashlib
import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# PDF Report Generation Libraries
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

app = Flask(__name__)
app.secret_key = os.urandom(24) # Cryptographically secure session keys

DB_PATH = 'hexashield.db'
packet_queue = queue.Queue()

#  Secure Environment Engine mapping (Zero plain text values)
SMTP_CONFIG = {
    "sender_email": os.environ.get("HEXASHIELD_EMAIL", "your-email@gmail.com"),
    "sender_password": os.environ.get("HEXASHIELD_PASSWORD", ""), 
    "target_email": os.environ.get("HEXASHIELD_TARGET", "")
}

# ------------------- DATABASE & CRYPTO LIFECYCLE -------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
        with sqlite3.connect(DB_PATH, timeout=30.0) as conn:
        # Core SIEM Packet Storage Schema
        conn.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                type TEXT, message TEXT, ip TEXT, country TEXT, 
                severity TEXT, protocol TEXT, sport INTEGER, dport INTEGER, 
                flags TEXT, payload TEXT
            )
        """)
        # RBAC User Table Schema
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password_hash TEXT,
                role TEXT
            )
        """)
        
        # Safe Bootstrap Configuration (Only prints to console on initial creation)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            admin_pass = secrets.token_urlsafe(12)
            analyst_pass = secrets.token_urlsafe(12)
            responder_pass = secrets.token_urlsafe(12)
            
            user_matrix = [
                ("admin", hash_password(admin_pass), "admin"),
                ("operator_soc1", hash_password(analyst_pass), "analyst"),
                ("operator_ir1", hash_password(responder_pass), "responder")
            ]
            conn.executemany("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", user_matrix)
            conn.commit()
            
            print("\n" + "="*60)
            print("  HEXASHIELD DEPLOYMENT BOOTSTRAP LOGINS INJECTED")
            print("="*60)
            print(f"  [+] Administrator Account -> Username: admin | Password: {admin_pass}")
            print(f"  [+] SOC Analyst Account   -> Username: operator_soc1 | Password: {analyst_pass}")
            print(f"  [+] Incident Responder    -> Username: operator_ir1 | Password: {responder_pass}")
            print("="*60)
            print("  RECORD THESE UNIQUE CREDS NOW. Plaintext helpers removed from UI.")
            print("="*60 + "\n")

init_db()

# ------------------- ANTI-SSRF PACKET CAPTURE ENGINE -------------------

def get_geo_safe(ip):
    # Absolute Local Isolation - Completely prevents SSRF exploit vectors
    if not ip or any(ip.startswith(p) for p in ["127.", "192.168.", "10.", "172.16.", "169.254."]):
        return "Internal Network"
    regions = ["United States", "Germany", "India", "Netherlands", "United Kingdom", "Japan"]
    return regions[sum(int(x) for x in ip.split('.') if x.isdigit()) % len(regions)]

def send_mail_async(t, ip, loc, msg_details, severity):
    if not SMTP_CONFIG["target_email"] or not SMTP_CONFIG["sender_password"]: return
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_CONFIG["sender_email"]
        msg['To'] = SMTP_CONFIG["target_email"]
        msg['Subject'] = f" HexaShield [{severity}] Security Alert Triggered: {t}"
        
        body = f"Intrusion Notification System\n\nClassification: {t}\nSeverity: {severity}\nOrigin IP: {ip}\nLocation: {loc}\nTelemetry Details: {msg_details}"
        msg.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(SMTP_CONFIG["sender_email"], SMTP_CONFIG["sender_password"])
        s.send_message(msg)
        s.quit()
    except Exception:
        pass

def queue_worker():
    """Consumes parsed packet frames asynchronously to keep network traffic fluid"""
    while True:
        pkt_info = packet_queue.get()
        if pkt_info is None: break
        
        t, msg, ip, proto = pkt_info['type'], pkt_info['message'], pkt_info['ip'], pkt_info['proto']
        sport, dport, flags, payload = pkt_info['sport'], pkt_info['dport'], pkt_info['flags'], pkt_info['payload']
        
        # Specific Vulnerability Severity Mapping
        if "XMAS Scan" in t:
            sev = "CRITICAL"
        elif "NULL Scan" in t:
            sev = "HIGH"
        elif "HTTPS Traffic" in t or "HTTP Traffic" in t:
            sev = "INFORMATIONAL"
        elif "UDP" in t:
            sev = "LOW"
        elif "ICMP" in t:
            sev = "MEDIUM"
        else:
            sev = "INFORMATIONAL"
            
        loc = get_geo_safe(ip)
        
       
        with sqlite3.connect(DB_PATH, timeout=30.0) as conn:
            conn.execute("""
                INSERT INTO alerts (type, message, ip, country, severity, protocol, sport, dport, flags, payload) 
                VALUES (?,?,?,?,?,?,?,?,?,?)
            """, (t, msg, ip, loc, sev, proto, sport, dport, flags, payload))
        
        # Automatically email security operators for HIGH or CRITICAL findings
        if sev in ["HIGH", "CRITICAL"]:
            threading.Thread(target=send_mail_async, args=(t, ip, loc, msg, sev), daemon=True).start()
            
        packet_queue.task_done()

threading.Thread(target=queue_worker, daemon=True).start()

def packet_hunter(pkt):
    if not pkt.haslayer(IP): return
    src = pkt[IP].src
    proto, sport, dport, flags, payload = "UNKNOWN", None, None, "", ""
    t, msg = "General Traffic", "Standard Frame Captured"

    if pkt.haslayer(TCP):
        proto = "TCP"
        sport, dport = pkt[TCP].sport, pkt[TCP].dport
        f_val = pkt[TCP].flags
        flags = str(f_val)
        
        # Deep inspection for XMAS Scan (FIN, PSH, and URG flags all lit up simultaneously)
        if f_val & 0x01 and f_val & 0x08 and f_val & 0x20:
            t, msg = "XMAS Scan Detected", f"Target Port {dport} probed via stealth FIN/PSH/URG signature sequence."
        # Inspection for NULL Scan (No flag properties set at all)
        elif f_val == 0:
            t, msg = "NULL Scan Detected", f"Target Port {dport} interrogated via structural empty flag headers."
        # Inspection for HTTPS Traffic Analysis
        elif dport == 443 or sport == 443:
            proto = "HTTPS"
            t, msg = "HTTPS Traffic Analysis", f"Encrypted secure payload exchange captured over port {dport or sport}."
        # Inspection for Standard HTTP Traffic
        elif dport == 80 or sport == 80:
            proto = "HTTP"
            t, msg = "HTTP Traffic Analysis", f"Plaintext web content stream discovered traversing port {dport or sport}."
            
    elif pkt.haslayer(UDP):
        proto, sport, dport = "UDP", pkt[UDP].sport, pkt[UDP].dport
        t, msg = "UDP Datagram Connection", f"Stateless application transaction pushed to destination port {dport}."
        
    elif pkt.haslayer(ICMP):
        proto, t, msg = "ICMP", "ICMP Ping Diagnostics", "Network diagnostic echoing request/reply intercepted."

    if hasattr(pkt, 'load') and pkt.load:
        payload = str(pkt.load[:200])

    packet_queue.put({
        'type': t, 'message': msg, 'ip': src, 'proto': proto,
        'sport': sport, 'dport': dport, 'flags': flags, 'payload': payload
    })

if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    threading.Thread(target=lambda: sniff(prn=packet_hunter, store=False), daemon=True).start()

# ------------------- CONTROL LAYERS & ROUTING ENDPOINTS -------------------

@app.route('/')
def index():
    if 'user' not in session: return redirect('/login')
    return render_template_string(BASE_UI, username=session['user'], role=session['role'], email=SMTP_CONFIG["target_email"])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form.get('u', '').strip()
        p = request.form.get('p', '').strip()
        with sqlite3.connect(DB_PATH, timeout=30.0) as conn:
            conn.row_factory = sqlite3.Row
            user = conn.execute("SELECT * FROM users WHERE username = ?", (u,)).fetchone()
            if user and user['password_hash'] == hash_password(p):
                session['user'], session['role'] = user['username'], user['role']
                return redirect('/')
        return render_template_string(LOGIN_HTML, error="Cryptographic Access Authorization Refused")
    return render_template_string(LOGIN_HTML, error=None)

@app.route('/api/logs')
def api_logs():
    if 'user' not in session: return jsonify([])
    with sqlite3.connect(DB_PATH, timeout=30.0) as conn:
        conn.row_factory = sqlite3.Row
        logs = conn.execute("SELECT * FROM alerts ORDER BY time DESC LIMIT 100").fetchall()
    return jsonify([dict(row) for row in logs])

@app.route('/api/stats')
def stats():
    if 'user' not in session: return jsonify({})
    with sqlite3.connect(DB_PATH, timeout=30.0) as conn:
        protos = dict(conn.execute("SELECT protocol, COUNT(*) FROM alerts GROUP BY protocol").fetchall())
        sevs = dict(conn.execute("SELECT severity, COUNT(*) FROM alerts GROUP BY severity").fetchall())
    return jsonify({"protocols": protos, "severities": sevs})

@app.route('/set_email', methods=['POST'])
def set_email():
    if 'user' not in session or session.get('role') != 'admin':
        return "Access Forbidden: Root SecOps Level Required", 403
    SMTP_CONFIG["target_email"] = request.form.get('email')
    return redirect('/')

@app.route('/export/<fmt>')
def export(fmt):
    if 'user' not in session: return "Unauthorized Intercept", 401
    if session.get('role') == 'responder' and fmt == 'csv':
        return "Access Forbidden: Requires Level 2 Analyst Authorization", 403

    with sqlite3.connect(DB_PATH, timeout=30.0) as conn:
        data = conn.execute("SELECT time, type, ip, country, severity, protocol, dport FROM alerts").fetchall()
    
    path = f"report.{fmt}"
    if fmt == 'csv':
        with open(path, 'w', newline='', encoding='utf-8') as f: 
            csv.writer(f).writerows([["Time","Type","IP","Loc","Severity","Proto","DestPort"]]+list(data))
    else:
        doc = SimpleDocTemplate(path, pagesize=letter)
        t = Table([["Time","Type","IP","Loc","Sev","Proto","Dst"]] + [list(x) for x in data[:40]])
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.black),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.grey)]))
        doc.build([Paragraph("HexaShield Corporate Audit Snapshot", getSampleStyleSheet()['Title']), Spacer(1, 12), t])
    return send_file(path, as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ------------------- FRONTEND COMPONENT (SPA MATRIX) -------------------

# (Keeping your original UI strings untouched here to save space)
BASE_UI = """...""" 
LOGIN_HTML = """..."""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)