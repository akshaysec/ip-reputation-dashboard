from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import ipaddress

app = Flask(__name__)
CORS(app)


# ========================================
# LOAD LOCAL DATASET
# ========================================

with open("reputation_data.json", "r") as file:
    reputation_data = json.load(file)


# ========================================
# SERVE FRONTEND
# ========================================

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")


# ========================================
# CHECK IP
# ========================================

@app.route("/api/check-ip", methods=["POST"])
def check_ip():

    data = request.get_json()

    if not data or "ip" not in data:
        return jsonify({
            "error": "IP address is required"
        }), 400

    ip = data["ip"].strip()

    # Validate IPv4
    try:
        ipaddress.IPv4Address(ip)

    except ValueError:

        return jsonify({
            "error": "Invalid IPv4 address"
        }), 400


    # Search local dataset

    result = next(
        (
            item
            for item in reputation_data
            if item["ip"] == ip
        ),
        None
    )


    # IP not found

    if result is None:

        return jsonify({
            "error":
                "IP address not found in local reputation dataset"
        }), 404


    # Return complete record

    return jsonify(result)


# ========================================
# START SERVER
# ========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )