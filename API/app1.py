from datetime import datetime
from flask import Flask, Blueprint, jsonify, request
from Logic.User import user_login, user_signup, fetch_all_user, fetch_user_detail, delete_user, user_profile_update, user_password_update
from Repository.DB_conn import DBconn

api = Blueprint('api', __name__, url_prefix='/api/v1')
connection_var = DBconn()

@api.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Blueprint!"})


@api.route('/user/login', methods=['GET'])
def login():
    conn = None
    try:
        conn = connection_var.get_conn()
        json_data = request.get_json()
        user_name = json_data.get('username')
        user_password = json_data.get('password')
        if user_name or user_password:
            if user_login(user_name, user_password, conn) == True:
                print(f"time:{datetime.now()}, levelname: Info, name:{__name__}, message: admin login successful")
                return jsonify({"message": "Hello admin!"}), 200
            else:
                print(f"time:{datetime.now()}, levelname: Warning, name:{__name__}, message:Wrong credentials entereed. Username:{user_name} and Password:{user_password}")
                return jsonify({"message": "Check credentials!"}), 401
        return jsonify({"message": "Missing username or password"}), 400
    except Exception as e:
        print(f"time:{datetime.datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)

@api.route('/user/all', methods=['GET'])
def display_list_of_users():
    try:
        users = fetch_all_user(conn)
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        print(f"time:{datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500

@api.route('/user/<int:user_id>', methods=['GET'])
def display_user_details(user_id):
    try:
        user = fetch_user_detail(user_id,conn)
        return jsonify(user.to_dict())
    except Exception as e:
        print(f"time:{datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500

@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user_details(user_id):
    try:
        user = delete_user(user_id, conn)
        return  jsonify({"message": user}), 200
    except Exception as e:
        print(f"time:{datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500

@api.route(rule='/user/signup', methods=['POST'])
def signup():
    try:
        json_data = request.get_json()
        password =  json_data.get('password')
        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        dob = json_data.get('dob')
        user_name = json_data.get('user_name')
        objective = json_data.get('objective')
        # creation_date, lock_account, last_login

        if password or first_name or last_name or user_name or dob:
            dob1 = datetime.strptime(dob, "%Y-%m-%d").date()
            new_user = user_signup(first_name,  last_name,dob1,objective,user_name,password,conn)
            message, userid = new_user
            if userid>0:
                return jsonify({"message": f'{message} {userid}' }),200
            else:
                return  jsonify({"message": f'{message} {userid}'}),401

        return jsonify({"message": "Something is missing"}),400
    except Exception as p:
        print(f"time:{datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{p}")
        return jsonify({"Error": "Technical error, try again later!"}), 500


@api.route('/user/<int:user_id>', methods=['PATCH'])
def update_user_details(user_id):
    try:
        json_data = request.get_json()

        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        dob = json_data.get('dob')
        objective = json_data.get('objective')

        user = user_profile_update( first_name,last_name,dob,objective,user_id,conn)
        return  jsonify({"message": user}), 200
    except Exception as e:
        print(f"time:{datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500


@api.route('/user/forgotpassword/<int:user_id>', methods=['PATCH'])
def forgot_password_details(user_id):
    try:
        json_data = request.get_json()

        password = json_data.get('password')

        user = user_password_update(password, user_id, conn)
        return jsonify({"message": user}), 200
    except Exception as e:
        print(f"time:{datetime.now()}, levelname: Error, name:{__name__}, message: request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app