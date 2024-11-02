import sys
sys.path.append("./")
import sqlite3

class Card():
    def __init__(self, conn):
        self.conn = conn
        card_table_command = """CREATE TABLE IF NOT EXISTS
        Card(
            card_id TEXT PRIMARY KEY,
            username TEXT,
            FOREIGN KEY(username) REFERENCES User(username)
            );
        """
        cursor = self.conn.cursor()
        cursor.execute(card_table_command)
        self.conn.commit()
        cursor.close()

    def insertNewCard(self, card_id, username):
        insert_new_card_command = f"""
            INSERT INTO Card
            VALUES ( "{card_id}", "{username}")
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_new_card_command)
        self.conn.commit()
        cursor.close()

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
        cursor = self.conn.cursor()
        result = cursor.execute(get_owner_command).fetchall()[0][0]
        cursor.close()

        return  result
    

    def getAll(self):
        get_All = f"""
            SELECT *
            FROM Card
        """
        cursor = self.conn.cursor()
        result = cursor.execute(get_All).fetchall()
        cursor.close()

        return result

    def getCardIdFromUserName(self, username):
        """
        username: String, representando o ID do usuário
        """
        get_username_command = f"""
            SELECT card_id
            FROM Card
            WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        result = cursor.execute(get_username_command).fetchall()[0][0]
        cursor.close()
        
        return result

