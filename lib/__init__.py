from flask import Flask
from .extensions import sock
from .views import main
from .environments import enviroments as env

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = env.secret_key
    app.config["DEBUG"] = True
    sock.init_app(app)
    app.register_blueprint(main)
    return app