## 🛡️ HEXASHIELD

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

Hexashield is a lightweight Security Operations (SecOps) Authentication Gateway and Network Monitoring Platform built using Python, Flask, and Scapy. It provides real-time packet sniffing, role-based access control, security event detection, automated alerts, and report generation.

The system captures live network traffic, classifies protocol activity, identifies suspicious behavior patterns, and generates downloadable CSV and PDF reports for security analysis and auditing.

---

## Features

### Security Authentication Gateway
- Role-Based Access Control (RBAC)
- Secure session handling
- Multiple user roles (Admin, SOC Analyst, Incident Response Operator)

### Real-Time Network Monitoring
- Live packet capture using Scapy
- TCP, UDP, ICMP traffic analysis
- Multi-threaded packet processing
- Continuous network logging

### Security Event Detection
- Suspicious activity detection logic
- Real-time alert generation
- Security incident monitoring

### Dashboard Interface
- Dark-themed Flask dashboard
- Live traffic visualization
- Security event monitoring panel

### Email Alert System
- SMTP-based alerts
- Instant security notifications
- Configurable recipients

### Reporting System
- CSV export for logs
- PDF report generation
- Security audit documentation

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Backend | Python |
| Framework | Flask |
| Packet Analysis | Scapy |
| Database | SQLite |
| Reporting | CSV / PDF |
| Notifications | SMTP |

---

## Project Structure

```text
HEXASHIELD/
│
├── Hexashield.py              # Main Flask app + packet sniffer engine
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
└── .gitignore                 # Git ignore rules
```

---

## Prerequisites

- Python 3.8+
- Pip package manager
- Npcap (Windows) or root privileges (Linux/macOS)
- Admin access for packet sniffing

---

## Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Hexashield.git
cd Hexashield
```

---

## 2. Create Virtual Environment

### Windows

```cmd
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows (CMD)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Configuration

Set environment variables for email alert system:

### Windows

```cmd
set HEXASHIELD_EMAIL=your-sender-email@gmail.com
set HEXASHIELD_PASSWORD=your-google-app-password
set HEXASHIELD_TARGET=security-alerts@yourdomain.com
```

### Linux / macOS

```bash
export HEXASHIELD_EMAIL="your-sender-email@gmail.com"
export HEXASHIELD_PASSWORD="your-google-app-password"
export HEXASHIELD_TARGET="security-alerts@yourdomain.com"
```

---

## Run Application

### Windows (Run as Administrator)

```cmd
python Hexashield.py
```

### Linux / macOS

```bash
sudo ./venv/bin/python Hexashield.py
```

---

## Access Dashboard

After running the application, open:

```text
http://127.0.0.1:5000
```

Login credentials (auto-generated) will appear in the terminal for:
- Admin
- SOC Analyst
- Incident Response Operator

---

## Security Features

- Role-Based Access Control (RBAC)
- Real-time packet inspection
- Automated threat detection
- Secure session management
- Audit logging system
- Security event monitoring

---

## Export Features

- CSV export for network logs
- PDF security reports
- Incident analysis reports

---

## Future Enhancements

- GeoIP threat intelligence integration
- SIEM correlation engine
- WebSocket live dashboard updates
- REST API integration
- Multi-factor authentication (MFA)
- Advanced intrusion detection system

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This tool is intended for educational and authorized security monitoring purposes only. Unauthorized network monitoring is strictly prohibited.
