from eval import build_expression
from eval import generate_sequence
from flask import Flask, request, jsonify
from flask_cors import CORS

def main():
    #accept input from script.js
    rules = ("n / 3", "2*n + 1", "2*n - 1")
    rule_list = build_expression(rules)
    print(generate_sequence(rule_list, start=10, limit=50))
    #send sequence back to script.js

if __name__ == "__main__":
    main()
