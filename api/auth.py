from flask import request, jsonify
from services.auth_provider import authenticate
from services.jwt_handler import generate_jwt

def init(app):

    @app.route('/api/auth', methods=['POST'])
    def auth():
        email = request.json.get('email')
        password = request.json.get('password')
        if not email or not password:
            return jsonify({"message": "Email or password missing", "status": 400}), 400

        user_data = authenticate(email, password)
        if not user_data:
            return jsonify({"message": "Invalid credentials", "status": 400}), 400

        token = generate_jwt(payload=user_data, lifetime=60)
        return jsonify({"data": token, "status": 200}), 200