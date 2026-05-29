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
