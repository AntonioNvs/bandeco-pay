import os

from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, jsonify, request, g

from datetime import datetime, timedelta

from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = os.environ.get("FLASK_DEBUG")
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

database = Database("databases/database.db")

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify({
        "msg": "Hello Ione!"
    })

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
        access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
        return jsonify({
            "access_token": access_token
        }), 200
    else:
        return jsonify({
            "msg": "Invalid credentials"
        }), 401
    
@app.route("/menu", methods=["GET"])
def get_today_restaurant_menu():
    restaurant_name = request.args.get("restaurant_name")
    meal_period = request.args.get("meal_period")

    today_date = datetime.today().strftime('%Y-%m-%d')

    menu = database.getMenu(restaurant_name, today_date, meal_period)
    return jsonify({
        "menu": menu.split("\n")
    }), 200


@app.route("/get_user_name", methods=["GET"])
@jwt_required(False)
def get_user_name():
    # Obtém o nome de usuário do token JWT
    username = get_jwt_identity()
    
    name = database.getUserName(username)

    return jsonify({
        "name": name
    }), 200

@app.route("/balance", methods=["GET"])
@jwt_required(False)
def get_balance_of_user():
    # Obtém o nome de usuário do token JWT
    username = get_jwt_identity()
    
    # Busca o saldo do usuário a partir do banco de dados
    balance = database.getBalance(username=username)

    return jsonify({
        "name": username,
        "balance": balance
    }), 200


@app.route("/add_balance", methods=["POST"])
@jwt_required(False)
def add_balance_of_user():
    username = get_jwt_identity()
    balance_to_be_add = request.json.get("value")
    type_ = request.json.get("type")
    
    database.insertNewTransaction(
        type_=type_,
        value=float(balance_to_be_add),
        transaction_date=datetime.today().strftime('%Y-%m-%d'),
        username=username,
        restaurant_id=1
    )

    database.addBalance(
        username=username,
        value_to_add=balance_to_be_add
    )
    
    return jsonify({
        "msg": "succeed"
    }), 200 


@app.route("/subtract_balance", methods=["POST"])
def subtract_balance_of_user():
    card_id = request.json.get("cardId")

    username = database.getOwner(card_id)

    ammount_to_pay = database.getAmounttoPay(username=username)

    balance = database.getBalance(username)

    name = database.getUserName(username)

    if balance < ammount_to_pay:
        return jsonify({
            "msg": "no balance enough",
            "name": name,
            "balance": balance
        }), 200

    database.insertNewTransaction(
        type_="debit",
        value=-ammount_to_pay,
        transaction_date=datetime.today().strftime('%Y-%m-%d'),
        username=username,
        restaurant_id=1
    )

    database.addBalance(
        username=username,
        value_to_add=-ammount_to_pay
    )

    return jsonify({
        "msg": "succedd",
        "name": name,
        "value_used": ammount_to_pay,
        "balance": balance - ammount_to_pay
    }), 200 

@app.route("/history", methods=["GET"])
@jwt_required(False)
def get_history_of_transactions():
    username = get_jwt_identity()
    columns = ["transaction_id", "type", "value", "date", "username", "card_id", "restaurant_id"]
    transactions = database.getTransactionsByUser(username)

    rows = [{columns[idx]: attribute for idx, attribute in enumerate(transaction)} for transaction in transactions]

    # Adquirindo os nomes dos restaurantes
    for row in rows:
        restaurant_name = database.getRestaurantNameById(row["restaurant_id"])

        row["description"] = restaurant_name if row["type"] == "debit" else row["type"]
        
        if row["type"] != "debit":
            row["type"] = "credit"

        del row["restaurant_id"]
        del row["username"]
        del row["card_id"]


    return jsonify({
        "transactions": rows[::-1]
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)