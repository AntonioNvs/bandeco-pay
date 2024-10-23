import sys
sys.append("./")
import sqlite3

class User():
    def __init__(self, database_filename): #remember to use ../ if not in the directory
        self.conn = sqlite3.connect(database_filename)
        self.cursor = self.conn.cursor()
        self.user_table_command = """CREATE TABLE IF NOT EXISTS
            User(
                user_id INTEGER PRIMARY KEY, 
                name TEXT, 
                balance FLOAT, 
                price_to_pay FLOAT
            );
        """
        self.cursor.execute(self.user_table_command)#USER
    
    def getName(self, user_id):
        get_name_command = f"""
        SELECT name
        FROM User
        WHERE user_id = {user_id}
        """
        self.cursor.execute(get_name_command)
        return (self.cursor.fetchall())
    
    def getBalance(self, user_id):
        get_balance_command = f"""
        SELECT balance
        FROM User
        WHERE user_id = {user_id}
        """
        self.cursor.execute(get_balance_command)
        return (self.cursor.fetchall())
    
    def getPriceToPay(self, user_id):
        get_pricetopay_command = f"""
        SELECT price_to_pay
        FROM User
        WHERE user_id = {user_id}
        """
        self.cursor.execute(get_pricetopay_command)
        return (self.cursor.fetchall())
    
    def setBalance(self, user_id, new_balance):
        set_balance_command = f"""
        UPDATE User
        SET balance = {new_balance}
        WHERE user_id = {user_id}
        """
        self.cursor.execute(set_balance_command)
        self.conn.commit()
        return True
