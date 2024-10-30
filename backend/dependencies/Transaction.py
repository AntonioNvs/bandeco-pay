import sys
sys.path.append("./")
import sqlite3

class Transaction():
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        self.create_transaction_command = """CREATE TABLE IF NOT EXISTS
        Traction(
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_type TEXT,
            transaction_value FLOAT,
            transaction_date DATE,
            username TEXT,
            card_id TEXT,
            restaurant_id INTEGER,
            FOREIGN KEY(username) REFERENCES User(username),
            FOREIGN KEY(card_id) REFERENCES Card(card_id)
            FOREIGN KEY(restaurant_id) REFERENCES Restaurant(restaurant_id)
            );
        """
        self.cursor.execute(self.create_transaction_command)
        self.conn.commit()
    
    def insertTransaction(self, type_, value, transaction_date, username, card_id, restaurant_id):
        """
        type_: String contendo o tipo da transação.\n
        value: Float contendo o valor da transação.\n
        transaction_date: String contendo a data da transação em formato YYYY-MM-DD.\n
        username: String contendo o nome do usuário que efetuou a transação. \n
        restaurant_name: String contendo o nome do restaurante no qual a transação foi efetuada. Pode ser nulo. (String "" por padrão.)\n
        """
        #recuperar o id do usuario.
        # retrieve_restaurant_id = f"""
        #     SELECT restaurant_id
        #     FROM Restaurant
        #     WHERE restaurant_name = "{restaurant_name}"
        # """
        # fetch_command = self.cursor.execute(retrieve_restaurant_id).fetchall()
        
        insert_transaction_command = f"""
            INSERT INTO Traction (transaction_type, transaction_value, transaction_date, username, card_id, restaurant_id)
            VALUES ("{type_}", {value}, "{transaction_date}", "{username}", "{card_id}", {restaurant_id})
        """
        
        self.cursor.execute(insert_transaction_command)
        self.conn.commit()
        return True
    
    def retrieveUserTransaction(self, username):
        """
        username: String contendo o nome de usuário para um determinado usuário no sistema.\n

        returns: Uma lista de tuplas contendo todas as transações do usuário. [(ID, TIPO, VALOR, DATA, RESTAURANTE_RESPONSÁVEL, USUARIO_DONO)]
        """
        retrieve_usertransaction_command = f"""
            SELECT *
            FROM Traction
            WHERE username = "{username}"
            ORDER BY transaction_date
        """
        self.cursor.execute(retrieve_usertransaction_command)

        return self.cursor.fetchall()