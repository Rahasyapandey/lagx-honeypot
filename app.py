from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

SECRET_API_KEY = "lagx_sk_abc123xyz789"

def extract_urls(text):
    try:
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        urls = re.findall(url_pattern, text)
        return [{"type": "url", "value": url, "risk": "high"} for url in urls]
    except:
        return []

def extract_emails(text):
    try:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return [{"type": "email", "value": email, "risk": "medium"} for email in emails]
    except:
        return []

def extract_phones(text):
    try:
        phone_pattern = r'[\+]?[(]?[0-9]{1,3}[)]?[-\s\.]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,9}'
        phones = re.findall(phone_pattern, text)
        return [{"type": "phone", "value": phone, "risk": "medium"} for phone in phones]
    except:
        return []

@app

