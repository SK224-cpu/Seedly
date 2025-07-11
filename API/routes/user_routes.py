from datetime import datetime
from flask import Flask, Blueprint, jsonify, request
from Logic.User import user_login, user_signup, fetch_all_user, fetch_user_detail, delete_user, user_profile_update, user_password_update
from Repository.DB_conn import DBconn
from Logs.logger import get_logger

connection_var = DBconn()
user_blueprint = Blueprint("users", __name__)
route_log = get_logger("user_routes")

@user_blueprint.route('/login', methods=['GET'])
def login():
    conn = None
    try:
        conn = connection_var.get_conn()
        json_data = request.get_json()
        user_name = json_data.get('username')
        user_password = json_data.get('password')
        if user_name or user_password:
            if user_login(user_name, user_password, conn) == True:
                route_log.info("admin login successful")
                return jsonify({"message": "Hello admin!"}), 200
            else:
                route_log.warning(f"Wrong credentials entereed. Username:{user_name} and Password:{user_password}")
                return jsonify({"message": "Check credentials!"}), 401
        return jsonify({"message": "Missing username or password"}), 400

    except Exception as e:
        route_log.error(f" request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)

@user_blueprint.route('/all', methods=['GET'])
def display_list_of_users():
    conn = None
    try:
        conn = connection_var.get_conn()
        users = fetch_all_user(conn)
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        route_log.error(f" request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)


@user_blueprint.route('/<int:user_id>', methods=['GET'])
def display_user_details(user_id):
    conn = None
    try:
        conn = connection_var.get_conn()
        user = fetch_user_detail(user_id,conn)
        return jsonify(user.to_dict())
    except Exception as e:
        route_log.error(f" request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)


@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user_details(user_id):
    conn = None
    try:
        conn = connection_var.get_conn()
        user = delete_user(user_id, conn)
        return  jsonify({"message": user}), 200
    except Exception as e:
        route_log.error(f" request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)

@user_blueprint.route(rule='/signup', methods=['POST'])
def signup():
    conn = None
    try:
        conn = connection_var.get_conn()
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
        route_log.error(f" request failed. Error:{p}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)


@user_blueprint.route('/<int:user_id>', methods=['PATCH'])
def update_user_details(user_id):
    conn = None
    try:
        conn = connection_var.get_conn()
        json_data = request.get_json()

        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        dob = json_data.get('dob')
        objective = json_data.get('objective')

        user = user_profile_update( first_name,last_name,dob,objective,user_id,conn)
        return  jsonify({"message": user}), 200
    except Exception as e:
        route_log.error(f" request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)

@user_blueprint.route('/forgotpassword/<int:user_id>', methods=['PATCH'])
def forgot_password_details(user_id):
    conn = None
    try:
        conn = connection_var.get_conn()
        json_data = request.get_json()

        password = json_data.get('password')

        user = user_password_update(password, user_id, conn)
        return jsonify({"message": user}), 200
    except Exception as e:
        route_log.error(f" request failed. Error:{e}")
        return jsonify({"Error": "Technical error, try again later!"}), 500
    finally:
        if conn:
            connection_var.return_conn(conn)
