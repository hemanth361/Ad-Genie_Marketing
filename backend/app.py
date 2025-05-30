from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Ad Genie Backend Running!'

@app.route('/generate-call', methods=['POST'])
def generate_call():
    data = request.json
    return jsonify({"message": f"Calling {data.get('name')} with message: {data.get('message')}"})

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    text = request.json.get("text")
    sentiment = "positive" if "good" in text.lower() else "neutral"
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)