from backend.eval import build_expression, generate_sequence
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json() or {}

    seed = data.get("seed")
    relations = data.get("relations", [])

    if not relations:
        return jsonify({"error": "No relations provided"}), 400

    try:
        seed_value = int(seed)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid seed"}), 400
    
    rule_list = build_expression(relations)
    sequence = generate_sequence(rule_list, seed_value, limit=50)
    return jsonify({"sequence": sequence})