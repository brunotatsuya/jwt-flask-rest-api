from flask import jsonify
from services.auth_guard import auth_guard

def init(app):

    @app.route('/api/protected_route', methods=['GET'])
    @auth_guard() # <--- Requires the authentication, but do not restricts authorization by roles
    def protected_route():
        return jsonify({"message": 'You have accessed a protected route.', "status": 200}), 200

    @app.route('/api/protected_route_user', methods=['GET'])
    @auth_guard('user') # <--- Requires the authentication AND authorization by 'user' role
    def protected_route_user():
        return jsonify({"message": 'You have accessed a user protected route.', "status": 200}), 200

    @app.route('/api/protected_route_admin', methods=['GET'])
    @auth_guard('admin') # <--- Requires the authentication AND authorization by 'admin' role
    def protected_route_admin():
        return jsonify({"message": 'You have accessed a admin protected route.', "status": 200}), 200

    @app.route('/api/protected_route_super_admin', methods=['GET'])
    @auth_guard('super_admin') # <--- Requires the authentication AND authorization by 'super_admin' role
    def protected_route_super_admin():
        return jsonify({"message": 'You are a SUPER ADMIN!', "status": 200}), 200