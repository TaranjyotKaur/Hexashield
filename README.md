# 🛡️ HEXASHIELD

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Hexashield** is an advanced, lightweight SecOps Role Authentication Gateway and live SIEM (Security Information and Event Management) Network Packet Analyzer. Built with Python, Flask, and Scapy, it sniffs network traffic in real-time, categorizes protocols, maps geo-locations, and alerts security teams to suspicious behaviors via automated email integrations and downloadable PDF/CSV reports.

---

## 🚀 Key Features

* **Terminal-Driven Engine:** Multi-threaded packet ingestion backend with synchronous logging.
* **SecOps Authentication Gateway:** Role-based operator identity portal with cryptographically secure session handling.
* **Real-time Traffic Sniffing:** Passive observation of TCP, UDP, and ICMP structures via native network bindings.
* **Dynamic Security Dashboard:** Modern, sleek dark-mode telemetry workspace featuring interactive analytical rendering.
* **Email Alert Integration:** Instant SMTP notifications for rapid triage of critical network anomalies.
* **Data Export Capability:** Native engines to generate clean CSV logs or professional executive PDF files.

---

## 📸 System Walkthrough

### 1. Backend Ingestion Engine
Hexashield initializes database lifecycles, starts the core multi-threaded sniffer worker, and prepares network interface listener bindings.
![Terminal Initialization](terminal.jpg)

### 2. Operator Identity Access Gateway
Secure gateway login access preventing unauthenticated traffic manipulation. Operators input designated security credentials to provision an authenticated workspace session.
![Login Page](login%20page.png)
![Admin Credentials Verified](admin%20logged%20in%20credentials.png)

### 3. Dynamic SIEM Analytics Dashboard
Once authenticated, security teams gain immediate access to core system telemetry, bandwidth indices, real-time alert tickers, and continuous geolocation capture pools.
![SIEM Dashboard Overview](dashboard.png)

### 4. Traffic Metrics & Protocol Distributions
Interactive visual mapping tracking telemetry balances between TCP, UDP, and ICMP concentrations alongside high-severity incident counters.
![Analytics Charts](chart,graph.png)

### 5. Deep Packet Analysis Workspace
Granular structural logs detailing transport payloads, localized timestamps, target vectors, and country classifications.
![Packet Analyzer Engine](analyzer.png)
![Packet Payload Inspection Window](packet%20info.png)

### 6. Automated Alert Integrations & Reporting Tools
Instantly flag and pipe alerts to remote email boxes via the native SMTP transaction workflow, or downscale logs into portable CSV formats and executive PDF report tables.
![Mail Integration Interface](mail%20integration.png)
![Data Export Configuration Panel](exports.png)

---

## 🛠️ Deployment & Installation Guide

Follow these sequential steps to safely build your virtual environment, satisfy dependencies, configure internal variables, and launch the platform framework.

### 1. Prerequisites
Ensure you have Python 3.8+ installed along with packet capture privileges (e.g., Npcap on Windows or `sudo` capabilities on Linux/macOS for network interface sniffing).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Hexashield.git](https://github.com/YOUR_USERNAME/Hexashield.git)
cd Hexashield
