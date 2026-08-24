# IP Reputation & Threat Intelligence Dashboard

## Project Overview

The IP Reputation & Threat Intelligence Dashboard is a web-based cybersecurity tool designed to help SOC analysts investigate the reputation of an IPv4 address.

The application accepts an IPv4 address from the analyst and retrieves threat intelligence information from multiple sources, including:

- VirusTotal
- AbuseIPDB

The collected information is displayed in a centralized dashboard. The application also calculates a custom SOC Risk Score to help analysts prioritize potentially suspicious IP addresses.

---

## Project Objectives

The main objectives of this project are:

- Investigate the reputation of an IPv4 address.
- Collect threat intelligence from multiple sources.
- Correlate VirusTotal and AbuseIPDB information.
- Display malicious and suspicious detections.
- Display AbuseIPDB confidence and reporting information.
- Calculate a custom SOC Risk Score.
- Reduce manual effort during initial IP investigation.
- Demonstrate secure API credential handling.

---

## Features

### 1. IP Address Validation

The application validates the entered IPv4 address before performing the investigation.

Example of an invalid IP:

```text
999.999.999.999


### 2. VirusTotal Integration
The application retrieves reputation information from VirusTotal.
The dashboard displays:
•	IP Address 
•	Country 
•	ASN 
•	Malicious Vendors 
•	Malicious Detection Ratio 
•	Suspicious Vendors 
•	Harmless Vendors 
•	Undetected Vendors 
Example:
Malicious Vendors: 1
Detection Ratio: 1 / 91 vendors
Suspicious: 0
Harmless: 0
Undetected: 90
The values are retrieved dynamically from the VirusTotal API.

### 3. AbuseIPDB Integration
The application retrieves reputation information from AbuseIPDB.
The dashboard displays:
•	Abuse Confidence Score 
•	Total Reports 
•	ISP 
•	Domain 
•	Usage Type 
•	Tor Status

### 4. SOC Risk Score
The application calculates a custom risk score between 0 and 100.
Risk levels:
Score	Risk Level
0–19	LOW
20–49	MEDIUM
50–74	HIGH
75–100	CRITICAL
The risk level is displayed using different colors:
•	LOW → Green 
•	MEDIUM → Yellow 
•	HIGH → Orange 
•	CRITICAL → Red 
The SOC Risk Score is a custom scoring mechanism developed for this project. It is not an official VirusTotal or AbuseIPDB score.


## Risk Scoring Methodology
The score combines several threat-intelligence indicators.
VirusTotal Malicious Vendors
Maximum contribution: 40 points.
Malicious vendors × 10
Maximum = 40 points
VirusTotal Suspicious Vendors
Maximum contribution: 10 points.
Suspicious vendors × 5
Maximum = 10 points
AbuseIPDB Confidence Score
Maximum contribution: 30 points.
AbuseIPDB confidence × 0.30
For example:
Confidence = 80%

80 × 0.30 = 24 points
AbuseIPDB Reports
Reports	Points
0	0
1–9	2
10–49	5
50–99	7
100+	10
Tor Detection
Tor detected = 5 points
Tor not detected = 0 points
The final score is capped at 100.
________________________________________
System Architecture
 


Technology Stack
Frontend
•	HTML5 
•	CSS3 
•	Vanilla JavaScript 
Backend
•	Python 3 
•	Flask 
•	Flask-CORS 
•	Requests 
•	python-dotenv 
APIs
•	VirusTotal API 
•	AbuseIPDB API


Project Structure
IP-Reputation-Dashboard/
│
├── app.py                 # Flask backend
├── index.html             # Web dashboard
├── README.md              # Project documentation
├── .env                   # Private API credentials
├── .env.example           # Example environment configuration
└── .gitignore             # Files excluded from source control



Installation
Step 1: Install Python
Make sure Python 3 is installed.
Check the installed version:
python --version
________________________________________
Step 2: Install Required Packages
Run:
pip install flask flask-cors requests python-dotenv
________________________________________
Configuration
Create a .env file in the project directory.
VIRUSTOTAL_API_KEY=your_virustotal_api_key
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
Replace the placeholder values with your actual API keys.
Important Security Note
Do not put API keys directly inside index.html or frontend JavaScript.
The application stores API credentials in environment variables and accesses the external APIs through the Flask backend.


.env.example
The project includes an .env.example file for configuration reference.
Example:
VIRUSTOTAL_API_KEY=your_virustotal_api_key
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
The .env.example file does not contain real credentials.


.gitignore
The .gitignore file prevents sensitive files from being tracked by Git.
Example:
.env
__pycache__/
*.pyc
The real .env file should never be uploaded to a public repository.


Running the Application
Start the Flask backend:
python app.py
The application will start locally.
Open the following address in a browser:
http://127.0.0.1:5000/

Application Workflow
The investigation process works as follows:
Step 1
The analyst enters an IPv4 address.
Example:
8.8.8.8
Step 2
The frontend validates the IP address.
Step 3
The frontend sends the IP address to the Flask backend.
Step 4
The Flask backend sends requests to VirusTotal and AbuseIPDB.
Step 5
The backend processes the API responses.
Step 6
The results are returned to the dashboard.
Step 7
The application calculates the SOC Risk Score.
Step 8
The analyst reviews the reputation information and risk level.
________________________________________
Security Features
API Key Protection
API credentials are stored in the .env file rather than exposed in frontend JavaScript.
Source Control Protection
The .gitignore file prevents .env from being tracked by Git.
Input Validation
The application validates IPv4 addresses before performing the investigation.
Backend API Architecture
External threat-intelligence API requests are handled by the Flask backend.
This prevents API credentials from being directly exposed to the browser.
API Timeout
External API requests use a timeout to prevent indefinite waiting if an API becomes unavailable.
Error Handling
The application checks API responses and displays an appropriate error when a request fails.
________________________________________
Testing
The following test cases were used to validate the application.
Test Case	Input	Expected Result
Valid IPv4	8.8.8.8	Reputation information displayed
Invalid IPv4	999.999.999.999	Validation error
Empty input	Empty field	Validation error
Reported IP	Known reported IP	Reputation information displayed
API failure	Invalid API key	API error handled
Backend unavailable	Flask stopped	Connection error
Enter key	Valid IP + Enter	Investigation starts
________________________________________
Example Dashboard Output
Example VirusTotal result:
VirusTotal

IP Address:          141.101.96.80
Country:             FR
ASN:                 13335

Malicious Vendors:   1
Detection Ratio:     1 / 91 vendors
Suspicious:          0
Harmless:            0
Undetected:          90
Example AbuseIPDB information:
AbuseIPDB

Confidence Score:    API Result
Total Reports:       API Result
ISP:                 API Result
Domain:              API Result
Usage Type:          API Result
Tor:                 API Result
The values returned by the external services can change over time.
________________________________________
SOC Investigation Use Case
The dashboard can be used during the initial investigation of an alert involving a suspicious source IP.
A simplified SOC workflow is:
Security Alert
      |
      v
Identify Source IP
      |
      v
IP Reputation Check
      |
      +--------------------+
      |                    |
      v                    v
 VirusTotal           AbuseIPDB
      |                    |
      +---------+----------+
                |
                v
          Correlate Results
                |
                v
          SOC Risk Score
                |
                v
       Analyst Investigation
The dashboard helps an analyst quickly determine whether an IP requires additional investigation.
________________________________________
Limitations
•	The current version supports IPv4 addresses. 
•	Results depend on the availability of VirusTotal and AbuseIPDB. 
•	API rate limits may apply. 
•	Threat intelligence information can change over time. 
•	A malicious reputation does not automatically prove that an IP is currently attacking an organization. 
•	The SOC Risk Score is a custom prioritization mechanism. 
•	The application is not intended to replace a SIEM, SOAR, or enterprise threat-intelligence platform. 
________________________________________
Future Improvements
Possible future enhancements include:
•	IPv6 support 
•	Additional threat-intelligence sources 
•	WHOIS information 
•	IP geolocation 
•	Historical reputation tracking 
•	Vendor-by-vendor VirusTotal results 
•	Threat category classification 
•	CSV/PDF report generation 
•	Investigation history 
•	User authentication 
•	Role-based access control 
•	SIEM integration 
•	SOAR integration 
•	Automated IOC enrichment 
________________________________________
Disclaimer
This project is intended for cybersecurity learning, authorized security testing, SOC investigation, and defensive security purposes.
Threat-intelligence results should be validated using additional context before taking actions such as blocking an IP address.
________________________________________
Author
IP Reputation & Threat Intelligence Dashboard
Cybersecurity / SOC Project

### After creating it

Your project folder should now look like:

```text
IP-Reputation-Dashboard
│
├── app.py
├── index.html
├── README.md        ← created now
├── .env
├── .env.example
└── .gitignore

