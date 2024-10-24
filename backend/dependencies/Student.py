import sys
sys.path.append("./")
import sqlite3
from User import User

class Student(User):
    def __init__(self, database_filename):
        super.__init__(database_filename)
        self.student_table_command =  """CREATE TABLE IF NOT EXISTS
            Student(
                registration_number INTEGER PRIMARY KEY,  
                fump_level INTEGER,
                username TEXT,
                FOREIGN KEY(username) REFERENCES User(username)
            );
            """
        self.cursor.execute(self.student_table_command)
    
    def insertNewStudent(self, username, name, password, balance, registration_number, fump_level):
        self.insertNewUser(username, name, password, balance)
        insert_command_for_student = f"""
        INSERT INTO Student
        VALUES ({registration_number}, {fump_level}, {username})
        """
        self.cursor.execute(insert_command_for_student)
        return True

    def getFumpLevel(self, user_id):
        get_fumplevel_command = f"""
        SELECT fump_level
        FROM Student
        WHERE user_id = {user_id}
        """
        self.cursor.execute(get_fumplevel_command)
        return ( self.cursor.fetchall() )[0][0]
    
    def getAmounttoPay(self, username):
        fump_level = self.getFumpLevel()
        if (fump_level == 0):
            return 0.0
        elif (fump_level == 1):
            return 1.00
        elif (fump_level == 2):
            return 2.50
        elif (fump_level == 3):
            return 5.60
        else:
            print("Invalid Fump Level: {fump_level}")
            return -1.0
    
    
    # TODO --> RegistrationNumber not well defined. It supposes Student is a single object, not a table.
    # Requires some 'information' to search i.e. name, user_id, etc...
    def getRegistrationNumber(self):
        error = "Not implemented yet."
        print(error)
        return False