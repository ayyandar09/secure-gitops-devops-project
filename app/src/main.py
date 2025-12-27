from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest
from config import Config
from auth import token_required
from logger import setup_logger
import logging

setup_logger()
app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

@app.before_request
def before_request():
    REQUEST_COUNT.inc()
    logging.info(f"{request.method} {request.path}")

@app.route("/health")
def health():
    return jsonify({"status": "UP", "service": Config.APP_NAME})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

@app.route("/api/users", methods=["GET"])
@token_required
def get_users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    })

@app.route("/api/orders", methods=["GET"])
@token_required
def get_orders():
    return jsonify({
        "orders": [
            {"id": 101, "item": "Laptop"},
            {"id": 102, "item": "Phone"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
