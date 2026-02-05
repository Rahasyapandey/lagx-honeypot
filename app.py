from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# YOUR API KEY (this is what you will submit)
SECRET_API_KEY = "lagx_sk_abc123xyz789"

@app.route("/analyze", methods=["POST"])
def analyze():
    api_key = request.headers.get("x-api-key")

    if api_key != SECRET_API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    data = request.get_json()
    message = data.get("message", "")

    message = message.lower()

    threat_level = "low"

    if "urgent" in message or "verify" in message or "password" in message:
        threat_level = "high"

    if "bitcoin" in message or "crypto" in message or "investment" in message:
        threat_level = "critical"

    return jsonify({
        "threat_level": threat_level,
        "extracted_entities": []
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

