from backend.eval import build_expression, generate_sequence
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": str(e)}), e.code
    return jsonify({"error": "Internal Server Error", "detail": str(e)}), 500

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json() or {}
    seed = data.get("seed")
    relations = data.get("relations", [])

    if not relations:
        return jsonify({"error": "No relations provided"}), 400

    #verify the starting number is an integer
    try:
        seed_value = int(seed)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid seed"}), 400
    
    #evaluate the sequence
    try:
        rule_list = build_expression(relations)
        sequence = generate_sequence(rule_list, seed_value)
    except ValueError as exc:
        return jsonify({"error": "Sequence divergence or non-cycling rule detected", "detail": str(exc)}), 400
    except Exception as exc:
        return jsonify({"error": "Backend processing failed", "detail": str(exc)}), 500

    return jsonify({"sequence": sequence})