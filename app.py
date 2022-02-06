from flask import Flask
from api.auth import init as init_auth_routes
from api.routes import init as init_routes

def create_app():
    app = Flask(__name__)
    init_auth_routes(app)
    init_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()