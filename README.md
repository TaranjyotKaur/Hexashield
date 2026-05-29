# 🛡️ HEXASHIELD

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Hexashield** is an advanced, lightweight SecOps Role Authentication Gateway and live SIEM (Security Information and Event Management) Network Packet Analyzer. Built with Python, Flask, and Scapy, it sniffs network traffic in real-time, categorizes protocols, maps geo-locations, and alerts security teams to suspicious behaviors via automated email integrations and detailed downloadable PDF/CSV reports.

---

##  Key Features

* **Terminal-Driven Engine:** Multi-threaded packet ingestion backend with synchronized concurrency logging.
* **SecOps Authentication Gateway:** Role-based access control (RBAC) operator identity gateway with cryptographically secure session handling.
* **Real-time Traffic Sniffing:** Passive inspection of TCP, UDP, and ICMP structures via direct system network socket bindings.
* **Dynamic Security Dashboard:** Modern, sleek dark-mode telemetry workspace featuring real-time data analytical updates.
* **Email Alert Integration:** Instant SMTP notifications for rapid containment and triage of critical network anomalies.
* **Data Export Capability:** Dedicated export managers to generate clean CSV network logs or professional executive PDF files.

---

##  Deployment & Installation Guide

Follow these sequential steps to configure your virtual environment, satisfy application dependencies, configure environment variables, and launch the platform framework cleanly.

### 1. Prerequisites
Ensure you have Python 3.8+ installed along with packet capture privileges (e.g., Npcap on Windows or `sudo` capabilities on Linux/macOS for network interface sniffing).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Hexashield.git](https://github.com/YOUR_USERNAME/Hexashield.git)
cd Hexashield

3. Initialize a Virtual Environment (venv)
Isolate the platform environment architecture from your global system libraries.

On Windows:

DOS
python -m venv venv
On macOS / Linux:

Bash
python3 -m venv venv
4. Activate the Virtual Environment
Activate the terminal context before installing dependencies or executing runtime environments.

On Windows (Command Prompt):

DOS
venv\Scripts\activate
On Windows (PowerShell):

PowerShell
.\venv\Scripts\Activate.ps1
On macOS / Linux:

Bash
source venv/bin/activate
Your terminal line should now display the (venv) tag prefix.

5. Install Project Dependencies
Upgrade your local package manager and install the exact framework components listed in the requirements manifest:

Bash
pip install --upgrade pip
pip install -r requirements.txt
6. Configure Environment Secrets
To uphold strict security protocols and prevent static credential leaks, Hexashield processes mail relays directly out of your runtime terminal's environment variable buffer. Inject them into your workspace before launching:

On Windows (Command Prompt):

DOS
set HEXASHIELD_EMAIL=your-sender-email@gmail.com
set HEXASHIELD_PASSWORD=your-google-app-password
set HEXASHIELD_TARGET=security-alerts@yourdomain.com
On macOS / Linux:

Bash
export HEXASHIELD_EMAIL="your-sender-email@gmail.com"
export HEXASHIELD_PASSWORD="your-google-app-password"
export HEXASHIELD_TARGET="security-alerts@yourdomain.com"
7. Run the Application (With Admin Privileges)
Because the Scapy backend must bind directly to your hardware network adapter to listen for raw packet streams, the script requires administrative elevation.

On Windows: (Open your terminal app with Run as Administrator privileges)

DOS
python Hexashield.py
On macOS / Linux:

Bash
sudo ./venv/bin/python Hexashield.py
🚪 Accessing the SIEM Gateway
Capture Bootstrap Accounts: Upon database initialization, check your terminal output. A secure runtime configuration matrix will print auto-generated credentials for your administrative and analyst operational tiers (admin, operator_soc1, operator_ir1). Copy these strings down immediately.

Launch Interface: Open your web browser of choice and interact with the gateway locally at:
http://127.0.0.1:5000
