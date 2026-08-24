from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

# Load API keys from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

@app.route("/api/check-ip", methods=["POST"])
def check_ip():

    data = request.get_json()

    if not data or "ip" not in data:
        return jsonify({
            "error": "IP address is required"
        }), 400

    ip = data["ip"].strip()

    # -----------------------------
    # VirusTotal
    # -----------------------------

    vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    vt_headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    vt_response = requests.get(
        vt_url,
        headers=vt_headers,
        timeout=15
    )

    if vt_response.ok:

        vt_json = vt_response.json()

        vt_data = vt_json.get("data", {}).get("attributes", {})

        vt_stats = vt_data.get(
            "last_analysis_stats",
            {}
        )

        virustotal = {
            "ip": ip,
            "country": vt_data.get("country", "-"),
            "asn": vt_data.get("asn", "-"),
            "malicious": vt_stats.get("malicious", 0),
            "suspicious": vt_stats.get("suspicious", 0),
            "harmless": vt_stats.get("harmless", 0),
            "undetected": vt_stats.get("undetected", 0),
            "timeout": vt_stats.get("timeout", 0),
            "totalVendors": sum(vt_stats.values())
        }

    else:

        virustotal = {
            "error": f"VirusTotal error: {vt_response.status_code}"
        }


    # -----------------------------
    # AbuseIPDB
    # -----------------------------

    abuse_url = (
        "https://api.abuseipdb.com/api/v2/check"
        f"?ipAddress={ip}&maxAgeInDays=90"
    )

    abuse_headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    abuse_response = requests.get(
        abuse_url,
        headers=abuse_headers,
        timeout=15
    )

    if abuse_response.ok:

        abuse_json = abuse_response.json()

        abuse_data = abuse_json.get(
            "data",
            {}
        )

        abuseipdb = {
            "abuseConfidenceScore":
                abuse_data.get("abuseConfidenceScore", 0),

            "totalReports":
                abuse_data.get("totalReports", 0),

            "isp":
                abuse_data.get("isp", "-"),

            "domain":
                abuse_data.get("domain", "-"),

            "usageType":
                abuse_data.get("usageType", "-"),

            "isTor":
                abuse_data.get("isTor", False)
        }

    else:

        abuseipdb = {
            "error":
                f"AbuseIPDB error: {abuse_response.status_code}"
        }


    # -----------------------------
    # Return results to frontend
    # -----------------------------

    return jsonify({
        "ip": ip,
        "virustotal": virustotal,
        "abuseipdb": abuseipdb
    })


# -----------------------------
# Start server
# -----------------------------

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )