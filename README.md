# IP Reputation & Threat Intelligence Dashboard

A web-based cybersecurity tool for investigating IPv4 addresses using multiple threat intelligence sources.

The dashboard integrates with VirusTotal and AbuseIPDB to collect IP reputation information and provides a custom SOC Risk Score to help analysts prioritize suspicious IP addresses.

---

## Project Overview

During a SOC investigation, analysts may need to determine whether an IP address associated with an alert has a known malicious or suspicious reputation.

This project provides a centralized interface where an analyst can enter an IPv4 address and retrieve reputation information from multiple threat intelligence services.

The application collects the results, displays them in a dashboard, and calculates a custom risk score based on the available indicators.

---

## Objectives

- Investigate IPv4 address reputation.
- Integrate multiple threat intelligence sources.
- Reduce manual effort during initial IP investigation.
- Display malicious and suspicious detections.
- Display AbuseIPDB abuse confidence and reporting information.
- Calculate a custom SOC Risk Score.
- Demonstrate secure handling of API credentials.
- Provide a simple and user-friendly SOC investigation interface.

---

## Features

### IP Address Validation

The application validates IPv4 addresses before performing the investigation.

Example:

```text
8.8.8.8
```
Invalid such as 
```
999.999.999.999
```
is Rejected.

---

## The application retrieves IP reputation information from VirusTotal.

The dashboard displays:

IP Address
Country
ASN
Malicious Vendors
Malicious Detection Ratio
Suspicious Vendors
Harmless Vendors
Undetected Vendors
Total analyzed vendors

The actual values depend on the current VirusTotal reputation data.

---
## AbuseIPDB Integration

The application retrieves reputation information from AbuseIPDB.

The dashboard displays:

Abuse Confidence Score
Total Reports
ISP
Domain
Usage Type
Tor Status

---
## SOC Risk Assessment

The application calculates a custom risk score between 0 and 100.

Risk levels:

Score	Risk Level
0–19	LOW
20–49	MEDIUM
50–74	HIGH
75–100	CRITICAL

Risk levels are visually represented using different colors:

LOW → Green
MEDIUM → Yellow
HIGH → Orange
CRITICAL → Red

The SOC Risk Score is a custom scoring mechanism developed for this project. It is not an official score provided by VirusTotal or AbuseIPDB.

---
## Risk Scoring Methodology

The risk score combines several reputation indicators.

VirusTotal Malicious Vendors

Malicious vendor detections contribute up to 40 points.

Malicious Vendors × 10
Maximum = 40 points
VirusTotal Suspicious Vendors

Suspicious detections contribute up to 10 points.

Suspicious Vendors × 5
Maximum = 10 points
AbuseIPDB Confidence

AbuseIPDB confidence contributes up to 30 points.

Abuse Confidence × 0.30
Maximum = 30 points

For example:

Abuse Confidence = 80%

80 × 0.30 = 24 points
AbuseIPDB Reports
Number of Reports	Points
0	0
1–9	2
10–49	5
50–99	7
100+	10
Tor Detection
Tor detected = 5 points
Tor not detected = 0 points

The final risk score is capped at 100.

---
## System Architecture

![system_architecture](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/architecture-diagram.jpg)

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
      - Requests
      - python-dotenv
### Threat Intelligence
      - VirusTotal API
      - AbuseIPDB API

---
## Installation
### 1. Install Python
 Make sure Python 3 is installed.
 Check:
 ```
 python --version
 ```

### 2. Install Dependencies
Install the required Python packages:
```
pip install flask flask-cors requests python-dotenv
```

### API Configuration
The application uses environment variables for API credentials.

Create a file named:
```
.env
```
Add:
```
VIRUSTOTAL_API_KEY=your_virustotal_api_key
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
```
Replace the placeholder values with your actual API keys.

### Environment Template
The project includes:
```
.env.example
```
Example:
```
VIRUSTOTAL_API_KEY=your_virustotal_api_key
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
```
The .env.example file contains placeholders only and should not contain real API credentials.

### Security

API keys are not stored directly in the frontend.

The application uses the following architecture:
```
Browser
   |
   v
Flask Backend
   |
   +----> VirusTotal
   |
   +----> AbuseIPDB
```
The API credentials are loaded by the Flask backend from environment variables.

### .gitignore
The .gitignore file contains:
```
.env
__pycache__/
*.pyc
```
This prevents sensitive environment files and Python cache files from being tracked by Git.
### Important
Never upload the real .env file to a public GitHub repository.

---
## Running the Application
Start the Flask server:
```
python app.py
```
The application runs locally at:
```
http://127.0.0.1:5000/
```
Open the address in your browser.

---
## Application Workflow
The investigation process follows these steps:

![application_diagram](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/application-workflow.jpg)

---
## Screenshot 
### Dashboard
The main dashboard provides an interface for entering an IPv4 address and starting an IP reputation investigation.

![Dashboard](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/screenshot/dashboard_screenshot.png)

### Threat Intelligence Results
The dashboard displays reputation information retrieved from VirusTotal and AbuseIPDB.
![ip_result](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/screenshot/IP-reputation-result.png)

### SOC Risk Assessment
The dashboard calculates a custom SOC Risk Score and displays the corresponding risk level.
![risk_scoring](https://github.com/akshaysec/ip-reputation-dashboard/blob/main/img/screenshot/risk-scoring-result.png)

---
## Security Features Implemented
The project includes several security-related controls:

1. API Credential Protection
API credentials are stored in environment variables rather than frontend JavaScript.

2. Backend API Integration
Third-party API requests are handled by the Flask backend.

3. Input Validation
IPv4 addresses are validated before processing.

4. API Error Handling
The backend checks external API responses and handles unsuccessful requests.

5. Request Timeout
External API requests use a timeout to prevent indefinite waiting.

6. Source Control Protection
The .gitignore file prevents .env from being tracked by Git.

---
##Limitations

- The current version supports IPv4 addresses.
- Results depend on external API availability.
- VirusTotal and AbuseIPDB may impose API rate limits.
- Threat intelligence results may change over time.
- A malicious reputation does not automatically prove that an IP is currently attacking an organization.
- The custom SOC Risk Score is intended for prioritization and is not an official vendor score.
- The application is not a replacement for an enterprise SIEM, SOAR, or full threat intelligence platform.

---
## Future Enhancements
Potential future improvements include:
- WHOIS enrichment
- IP geolocation
- URL reputation check
- File hash reputation check

---
