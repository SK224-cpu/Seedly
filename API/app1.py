from API.routes.user_routes import user_blueprint
from flask import Flask, Blueprint

#api = Blueprint('api', __name__, url_prefix='/api/v1')
app = Flask(__name__)
app.register_blueprint(user_blueprint,url_prefix='/api/v1/users')


def create_app():
    return app