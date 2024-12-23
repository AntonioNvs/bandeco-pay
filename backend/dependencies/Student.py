import sys
sys.path.append("./")
import sqlite3
from User import User

class Student(User):
    def __init__(self, conn):
        super().__init__(conn)
        self.student_table_command =  """CREATE TABLE IF NOT EXISTS
            Student(
                registration_number INTEGER PRIMARY KEY,  
                fump_level INTEGER,
                username TEXT,
                FOREIGN KEY(username) REFERENCES User(username)
            );
            """
        cursor = self.conn.cursor()
        cursor.execute(self.student_table_command)
        self.conn.commit()
        cursor.close()

    def insertNewStudent(self, username, name, password, balance, registration_number, fump_level):
        self.insertNewUser(username, name, password, balance)
        insert_command_for_student = f"""
        INSERT INTO Student
        VALUES ({registration_number}, {fump_level}, "{username}")
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_command_for_student)
        self.conn.commit()
        cursor.close()
        return True

    def getFumpLevel(self, username):
        get_fumplevel_command = f"""
            SELECT fump_level
            FROM Student
            WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        cursor.execute(get_fumplevel_command)
        result = cursor.fetchall()[0][0]
        cursor.close()

        return result
    
    def getAmounttoPay(self, username):
        fump_level = self.getFumpLevel(username)
        if (fump_level == 1):
            return 0.0
        elif ((fump_level == 2) or (fump_level == 3)):
            return 1.00
        elif (fump_level == 4):
            return 2.00
        elif (fump_level == 5):
            return 2.90
        elif (fump_level == 6):
            return 5.60
        else:
            return -1.0

    def getRegistrationNumber(self, username):
        get_registration_command = f"""
        SELECT registration_number
        FROM Student
        WHERE username = {username}
        """
        cursor = self.conn.cursor()
        cursor.execute(get_registration_command)
        result = cursor.fetchall()[0][0]
        cursor.close()

        return result