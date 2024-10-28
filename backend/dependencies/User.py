import sys
sys.path.append("./")
import sqlite3

class User():
    def __init__(self, conn, cursor): #remember to use ../ if not in the directory
        self.conn = conn
        self.cursor = cursor
        self.user_table_command = """CREATE TABLE IF NOT EXISTS
            User(
                username TEXT PRIMARY KEY, 
                name TEXT,
                password TEXT, 
                balance FLOAT
            );
        """
        self.cursor.execute(self.user_table_command)#USER
    
    def insertNewUser(self, username, name, password, balance):
        insert_new_user_command = f"""
        INSERT INTO User
        VALUES ( "{username}", "{name}", "{password}", {balance} )
        """
        self.cursor.execute(insert_new_user_command)
        return True
    
    def getPassword(self, username):
        get_password_command = f"""
        SELECT password
        FROM User
        WHERE username = "{username}"
        """
        self.cursor.execute(get_password_command)
        return ( self.cursor.fetchall()[0][0] )

    def getName(self, username):
        get_name_command = f"""
        SELECT name
        FROM User
        WHERE username = "{username}"
        """
        self.cursor.execute(get_name_command)
        return ( self.cursor.fetchall()[0][0] )
    
    def getBalance(self, username):
        get_balance_command = f"""
        SELECT balance
        FROM User
        WHERE username = "{username}"
        """
        self.cursor.execute(get_balance_command)
        return ( self.cursor.fetchall()[0][0] )
    
    def setBalance(self, username, new_balance):
        set_balance_command = f"""
        UPDATE User
        SET balance = {new_balance}
        WHERE username = "{username}"
        """
        self.cursor.execute(set_balance_command)
        self.conn.commit()
        return True
