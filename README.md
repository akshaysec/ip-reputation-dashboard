# IP Reputation Dashboard

A lightweight web-based SOC analyst tool for analyzing IPv4 addresses against a local/sample IP reputation dataset.

The project is designed for educational and demonstration purposes. It allows a security analyst to enter an IPv4 address and view available reputation, network, and threat-related information from a locally stored dataset.

---

## Project Overview

The IP Reputation Dashboard provides a simple interface for investigating an IP address.

The application:

- Accepts an IPv4 address from the user
- Validates the IP address
- Searches a local/sample reputation dataset
- Displays reputation information
- Displays network information such as ASN, ISP, and domain
- Displays malicious and suspicious detection counts
- Displays abuse confidence and report information
- Identifies whether the IP is associated with Tor
- Works without external threat-intelligence APIs

> **Educational SOC Project — Reputation data is local/sample data and is not real-time threat intelligence.**

---

## Features

### IP Address Validation

The application validates the entered IPv4 address before performing the lookup.

Example:

```text
203.0.113.50
```
Invalid input such as:
```
999.999.999.999
```
is rejected.

---
## Local Reputation Lookup

The application searches the IP address against:
```
reputation_data.json
```
Only IP addresses available in the local dataset can return reputation information.

---
## Reputation Information

### The dashboard displays:

- IP Address
- Country
- ASN
- ISP
- Domain
- Usage Type
- Malicious Detections
- Suspicious Detections
- Harmless Detections
- Undetected Results
- Detection Sources
- Confidence Score
- Total Reports
- Tor Status

---
## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python 3
- Flask
- Flask-CORS

### Data Storage
- Local JSON dataset

No database or external threat-intelligence service is required.

---
## How the Application Works
The application follows a simple request and response architecture.

![application_flow](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/application-flow.jpg)

---
## Backend API
The application provides the following endpoint:

Check IP
POST /api/check-ip

Request:

{
    "ip": "203.0.113.50"
}

Example response:

{
    "ip": "203.0.113.50",
    "country": "IN",
    "asn": 64500,
    "isp": "Sample ISP",
    "domain": "example.com",
    "usageType": "ISP",
    "malicious": 4,
    "suspicious": 3,
    "harmless": 40,
    "undetected": 44,
    "totalVendors": 91,
    "abuseConfidenceScore": 55,
    "totalReports": 35,
    "isTor": false
}
Local Dataset

The application uses:

reputation_data.json

Example:

[
    {
        "ip": "203.0.113.50",
        "country": "IN",
        "asn": 64500,
        "isp": "Sample ISP",
        "domain": "example.com",
        "usageType": "ISP",
        "malicious": 4,
        "suspicious": 3,
        "harmless": 40,
        "undetected": 44,
        "totalVendors": 91,
        "abuseConfidenceScore": 55,
        "totalReports": 35,
        "isTor": false
    }
]

The dataset is provided for demonstration and educational purposes.

It does not represent real-time threat intelligence.

---
## Security Features

The project includes several basic security and validation controls.

### 1. Backend IP Validation

The backend validates the supplied IP address using Python's ipaddress module.

ipaddress.IPv4Address(ip)

This prevents invalid IPv4 addresses from being processed.

---
## 3. Local Data Processing

The application processes reputation information from a local dataset rather than sending the entered IP address to an external service.

## 4. Input Validation

The frontend also validates the IPv4 address before sending the request to the backend.

---
## Installation

### Step 1 — Install Python

Make sure Python 3 is installed.

Check:

python --version

or:

py --version

### Step 2 — Install Dependencies

Install Flask and Flask-CORS:

py -m pip install flask flask-cors
Running the Application

Open a terminal in the project directory:

IP-Reputation-Dashboard

Run:
py app.py

The Flask server should start at:

http://127.0.0.1:5000

Open the address in a web browser.

---
## Screenshots
### Dashboard

Add your dashboard screenshot here:

![Dashboard](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/screenshot/dashboard.png)
IP Reputation Result

Add your result screenshot here:

![IP Reputation Result](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/screenshot/result-output.png)

---
## Limitations

This project is an educational MVP and has some limitations:

The reputation data is local/sample data.
The application does not provide real-time threat intelligence.
The dataset must be manually updated.
The application does not use a production database.
The Flask development server should not be used for production deployment.
The project currently focuses on IPv4 addresses.

---
## Future Improvements

Possible future enhancements include:

Larger reputation datasets
CSV/database support
IPv6 support
Historical IP searches
Search history
Export investigation results

---
## Disclaimer

Educational SOC Project — Reputation data is local/sample data and is not real-time threat intelligence.
