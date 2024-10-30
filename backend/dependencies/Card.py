import sys
sys.path.append("./")
import sqlite3

class Card():
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        card_table_command = """CREATE TABLE IF NOT EXISTS
        Card(
            card_id TEXT PRIMARY KEY,
            username TEXT,
            FOREIGN KEY(username) REFERENCES User(username)
            );
        """
        cursor.execute(card_table_command)

    def insertNewCard(self, card_id, username):
        insert_new_card_command = f"""
            INSERT INTO Card
            VALUES ( "{card_id}", "{username}")
        """
        self.cursor.execute(insert_new_card_command)
        self.conn.commit()
        return True

    def getOwner(self, card_id):
        """
        card_id: String representando o ID do cartão.
        """
        get_owner_command = f"""
            SELECT username
            FROM Card
            WHERE card_id = "{card_id}"
        """
        return ( self.cursor.execute(get_owner_command).fetchall() )[0][0]
    

    def getAll(self):
        get_All = f"""
            SELECT *
            FROM Card
        """
        return self.cursor.execute(get_All).fetchall()

    def getCardIdFromUserName(self, username):
        """
        username: String, representando o ID do usuário
        """
        get_username_command = f"""
            SELECT card_id
            FROM Card
            WHERE username = "{username}"
        """
        return ( self.cursor.execute(get_username_command).fetchall() )[0][0]

