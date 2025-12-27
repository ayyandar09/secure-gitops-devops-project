from flask import request, jsonify
from functools import wraps
from config import Config

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("X-API-TOKEN")

        if not token or token != Config.API_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated
