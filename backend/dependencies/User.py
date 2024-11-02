import sys
sys.path.append("./")

class User():
    def __init__(self, conn): #remember to use ../ if not in the directory
        self.conn = conn
        self.user_table_command = """CREATE TABLE IF NOT EXISTS
            User(
                username TEXT PRIMARY KEY, 
                name TEXT,
                password TEXT, 
                balance FLOAT
            );
        """
        cursor = self.conn.cursor()
        cursor.execute(self.user_table_command)
        self.conn.commit()
        cursor.close()
    
    def insertNewUser(self, username, name, password, balance):
        insert_new_user_command = f"""
        INSERT INTO User
        VALUES ( "{username}", "{name}", "{password}", {balance} )
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_new_user_command)
        self.conn.commit()
        cursor.close()

        return True
    
    def getPassword(self, username):
        get_password_command = f"""
        SELECT password
        FROM User
        WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        cursor.execute(get_password_command)
        result = cursor.fetchall()[0][0]
        cursor.close()
        
        return result

    def verifyIfUsernameExists(self, username):
        get_name_command = f"""
            SELECT *
            FROM User
            WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        cursor.execute(get_name_command)
        result = cursor.fetchall()

        return len(result) == 1

    def getName(self, username):
        get_name_command = f"""
            SELECT name
            FROM User
            WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        cursor.execute(get_name_command)
        result = cursor.fetchall()[0][0]
        cursor.close()

        return result
    
    def getBalance(self, username):
        get_balance_command = f"""
            SELECT balance
            FROM User
            WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        cursor.execute(get_balance_command)
        result = cursor.fetchall()[0][0]
        cursor.close()
            
        return result
    
    def setBalance(self, username, new_balance):
        set_balance_command = f"""
            UPDATE User
            SET balance = {new_balance}
            WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        cursor.execute(set_balance_command)
        self.conn.commit()
        cursor.close()
        
        return True
