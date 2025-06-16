from flask import Flask, Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Blueprint!"})


app = Flask(__name__)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)