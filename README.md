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
