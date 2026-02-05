from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# YOUR API KEY
SECRET_API_KEY = "lagx_sk_abc123xyz789"

# --- Helper Functions ---
def extract_urls(text):
    """Extract URLs from text"""
    try:
        url_pattern = r'https?://[^\s<>"{}|\^`\[\]]+'
        urls = re.findall(url_pattern, text)
        return [{"type": "url", "value": url, "risk": "high"} for url in urls]
    except:
        return []

def extract_emails(text):
    """Extract email addresses"""
    try:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return [{"type": "email", "value": email, "risk": "medium"} for email in emails]
    except:
        return []

def extract_phones(text):
    """Extract phone numbers"""
    try:
        phone_pattern = r'[\+]?[()]?[0-9]{1,3}[)]?[- \.]?[()]?[0-9]{1,4}[)]?[- \.]?[0-9]{1,4}[- \.]?[0-9]{1,9}'
        phones = re.findall(phone_pattern, text)
        return [{"type": "phone", "value": phone, "risk": "medium"} for phone in phones]
    except:
        return []

@app.route("/", methods=["GET"])
def home():
    """Health check"""
    return jsonify({
        "status": "online",
        "service": "Team LagX Honey"
    })

@app.route("/analyze", methods=["POST"])
def analyze():
    # 1. Authentication Check
    api_key = request.headers.get("x-api-key")

    if api_key != SECRET_API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    # 2. Parse Data
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "threat_level": "low",
            "extracted_entities": []
        }), 200

    message = data.get("message", {})
    text = message.get("text", "")

    # Safety check to ensure text is a string
    if not isinstance(text, str):
        text = str(text)

    # Convert to lower case for keyword matching, but keep original for extraction if needed
    text_lower = text.lower()

    # 3. Determine Threat Level
    threat_level = "low"

    # High risk keywords
    if any(keyword in text_lower for keyword in ["urgent", "verify", "password", "blocked"]):
        threat_level = "high"

    # Critical risk keywords
    if any(keyword in text_lower for keyword in ["bitcoin", "crypto", "investment"]):
        threat_level = "critical"

    # 4. Extract Entities (Actually calling the functions now)
    results = []
    results.extend(extract_urls(text))
    results.extend(extract_emails(text))
    results.extend(extract_phones(text))

    # 5. Return Single, Correct JSON Response
    return jsonify({
        "threat_level": threat_level,
        "extracted_entities": results
    }), 200

if __name__ == "__main__":
    app.run(debug=True)




