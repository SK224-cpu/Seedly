import datetime
from flask import Flask, Blueprint, jsonify, request
from Logic.User import user_login
from configparser import ConfigParser
import psycopg2

api = Blueprint('api', __name__, url_prefix='/api/v1')

config = ConfigParser()
config.read("config/config.ini")
host_var = config['DB']['host']
database_var = config['DB']['database']
user_var = config['DB']['user']
password_var = config['DB']['password']
conn = psycopg2.connect(host=host_var, database=database_var, user=user_var, password=password_var)

@api.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Blueprint!"})


@api.route('/user/login', methods=['GET'])
def login():
    try:
        jason_data = request.get_json()
        user_name = jason_data.get('username')
        user_password = jason_data.get('password')
        if user_name or user_password:
            if user_login(user_name, user_password, conn) == True:
                print(f"time:{datetime.datetime.now()}, levelname: Info, name:{__name__}, message: admin login successful")
                return jsonify({"message": "Hello admin!"}), 200
            # elif name == 'user' and password124 == 'user4321':
            #     print(f"time:{datetime.datetime.now()}, levelname: Info, name:{__name__}, message: user login successful")
            #     return jsonify({"message": "Hello user!"}), 200
            else:
                print(f"time:{datetime.datetime.now()}, levelname: Warning, name:{__name__}, message:Wrong credentials entereed. Username:{user_name} and Password:{user_password}")
                return jsonify({"message": "Check credentials!"}), 401
        return jsonify({"message": "Missing username or password"}), 400
    except Exception as e:
        print(f"time:{datetime.datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app