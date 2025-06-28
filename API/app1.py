from API.routes.user_routes import user_blueprint
from flask import Flask, Blueprint
from Repository.DB_conn import DBconn
from Logs.logger import get_logger
import atexit

DB_obj = DBconn()
logger = get_logger()
app = Flask(__name__)
app.register_blueprint(user_blueprint,url_prefix='/api/v1/users')


def create_app():
    logger.info("API started")
    return app

@atexit.register
def close_db_pool():
    logger.critical("API stopped!")
    DB_obj.close_conn()