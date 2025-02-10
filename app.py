from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return "Hello, Flask !"

@app.route('/api/greet')
def greet():
    return jsonify(message="Hello, Shantanu")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
