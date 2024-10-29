import os

from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, jsonify, request

from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

jwt = JWTManager(app)

database = Database("database.db")

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    try:
        database_password = database.getPassword(username)
    except:
        return jsonify({
            "msg": "User not found"
        }), 401
      
    if check_password_hash(database_password, password):
        access_token = create_access_token(identity=username)
        return jsonify({
            "access_token": access_token
        }), 200
    else:
        return jsonify({
            "msg": "Invalid credentials"
        }), 401
    
@app.route("/menu", methods=["GET"])
def get_today_restaurant_menu():
    restaurant = request.form.get("restaurant")

    raise NotImplementedError("The connection with database will be implemented yet.")

    return jsonify(), 200

@app.route("/balance", methods=["GET"])
# @jwt_required
def get_balance_of_user():
    # username = get_jwt_identity()
    
    balance = database.getBalance("antonio.caetano") 

    return jsonify({
        "balance": balance
    }), 200

@app.route("/add_balance", methods=["PUT"])
@jwt_required
def add_balance_of_user():
    username = get_jwt_identity()
    balance_to_be_add = request.form.get("value")

    raise NotImplementedError("The connection with database will be implemented yet.")

    return jsonify(logged_in_as=username), 200 

@app.route("/subtract_balance", methods=["PUT"])
def subtract_balance_of_user():
    card_id = request.form.get("card_id")
    balance_to_be_subtract = request.form.get("value")

    raise NotImplementedError("The connection with database will be implemented yet.")

    return jsonify(logged_in_as=username), 200 

# @app.route("/history", methods=["GET"])
# @jwt_required
# def get_history_of_uses():
#     username = get_jwt_identity()

#     raise NotImplementedError("The connection with database will be implemented yet.")

#     return jsonify(logged_in_as=username), 200

if __name__ == '__main__':
    app.run(debug=True)
