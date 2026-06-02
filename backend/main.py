import os
from eval import build_expression
from eval import generate_sequence
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app = Flask(__name__, static_folder=BASE_DIR, static_url_path="/static")
CORS(app, resources={r"/process": {"origins": "*"}})

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/process", methods=["POST"])
def process():
    incoming = request.get_json()

    seed = incoming.get("seed")
    relations = incoming.get("relations", [])

    if not relations:
        return jsonify({"error": "No relations provided"}), 400

    try:
        seed_value = int(seed)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid seed"}), 400
    
    rule_list = build_expression(relations)
    sequence = generate_sequence(rule_list, seed_value, limit=50)
    reply = {"sequence": sequence}
    return jsonify(reply)


if __name__ == "__main__":
    app.run(debug=True)