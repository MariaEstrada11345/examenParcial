
from flask import Flask, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_PATH = os.path.join(os.path.dirname(__file__), "canciones.json")

@app.route("/canciones", methods=["GET"])
def get_canciones():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
