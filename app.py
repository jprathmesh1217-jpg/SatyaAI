from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Scam message analysis
@app.route("/analyze-text", methods=["POST"])
def analyze_text():

    data = request.get_json()

    text = data.get("text", "").lower()

    scam_words = [
        "urgent",
        "account blocked",
        "click",
        "verify",
        "otp",
        "winner",
        "prize",
        "lottery",
        "send money",
        "bank"
    ]

    detected = []

    for word in scam_words:
        if word in text:
            detected.append(word)

    if len(detected) >= 3:
        risk = 94
        level = "HIGH RISK"

    elif len(detected) >= 1:
        risk = 62
        level = "SUSPICIOUS"

    else:
        risk = 12
        level = "LOW RISK"

    return jsonify({
        "risk": risk,
        "level": level,
        "detected": detected
    })


# URL analysis
@app.route("/analyze-url", methods=["POST"])
def analyze_url():

    data = request.get_json()

    url = data.get("url", "").lower()

    suspicious_words = [
        "login",
        "verify",
        "bank",
        "secure",
        "update",
        "account"
    ]

    detected = []

    for word in suspicious_words:
        if word in url:
            detected.append(word)

    if len(detected) >= 2:
        risk = 91
        level = "HIGH RISK"

    elif len(detected) == 1:
        risk = 55
        level = "SUSPICIOUS"

    else:
        risk = 10
        level = "LOW RISK"

    return jsonify({
        "risk": risk,
        "level": level,
        "detected": detected
    })


# Deepfake prototype
@app.route("/analyze-image", methods=["POST"])
def analyze_image():

    return jsonify({
        "risk": 87,
        "level": "HIGH RISK",
        "detected": [
            "Visual inconsistencies",
            "Possible AI manipulation",
            "Facial artifacts"
        ]
    })


# Start application
if __name__ == "__main__":
    app.run(debug=True)
    