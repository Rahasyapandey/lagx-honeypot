This project is an Agentic Honey-Pot API built by Team LagX.
The purpose of this API is to receive text messages and analyze them to determine whether they look like scam or malicious messages. It acts like a honeypot, meaning it passively observes and classifies suspicious behavior rather than blocking users.

The API is deployed online and is publicly accessible.
The base address of the deployed service is:
https://lagx-honeypot-fixed.onrender.com

The actual working endpoint is not the base URL.
The endpoint that does the analysis is:
/analyze

So the full API endpoint that must be submitted and tested is:
https://lagx-honeypot-fixed.onrender.com/analyze

The API is protected using an API key.
Every request must include a special header called x-api-key.
If this header is missing or the value is incorrect, the API will reject the request with an “Unauthorized” error.

The API key value that the evaluator must use is:
lagx_sk_abc123xyz789

The API only accepts POST requests.
It expects data in JSON format.
The JSON must contain a field called “message”, which is the text that needs to be analyzed.

When a request is sent, the API reads the message, converts it to lowercase, and checks for certain keywords.
If the message contains urgency-related or credential-related words like “urgent”, “verify”, or “password”, the threat level is marked as high.
If the message contains financial scam terms like “bitcoin”, “crypto”, or “investment”, the threat level is marked as critical.
If none of these appear, the threat level remains low.

The API responds with a JSON object.
This response contains two fields:

threat_level – which can be low, high, or critical

extracted_entities – currently an empty list, reserved for future expansion

The system is built using Python with the Flask web framework.
Flask-CORS is used to allow cross-origin requests.
Gunicorn is used as the production server.
The service is deployed on the Render cloud platform.

For local testing, the project can be run by installing the dependencies listed in the requirements file and starting the app using Python.
Locally, the API runs on port 5000.

This API is ready for automated evaluation.
It is publicly accessible, stable, authenticated using headers, and returns consistent JSON responses.
This makes it suitable for security testing and competition evaluation.

At this stage, your job is complete: the endpoint is live, secured, documented, and ready to be submitted.
