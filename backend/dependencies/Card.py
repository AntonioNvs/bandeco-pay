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