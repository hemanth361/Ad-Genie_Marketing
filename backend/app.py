from flask import Flask, request, jsonify
from ai_models.call_generator import generate_call_script
from ai_models.sentiment_analysis import analyze
from ai_models.social_post_generator import generate_post

app = Flask(__name__)

@app.route('/')
def index():
    return "Ad Genie Backend is Running!"

@app.route('/generate-call', methods=['POST'])
def call():
    name = request.json.get("name", "User")
    message = generate_call_script(name)
    return jsonify({"script": message})

@app.route('/analyze', methods=['POST'])
def sentiment():
    text = request.json.get("text", "")
    result = analyze(text)
    return jsonify({"sentiment": result})

@app.route('/post', methods=['POST'])
def post():
    product = request.json.get("product", "service")
    audience = request.json.get("audience", "everyone")
    content = generate_post(product, audience)
    return jsonify({"post": content})

if __name__ == '__main__':
    app.run(debug=True)