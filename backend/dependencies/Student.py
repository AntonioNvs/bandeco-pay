import sys
sys.append("./")
import sqlite3
import User

class Student(User):
    def __init__(self, database_filename):
        super.__init__(database_filename)
        self.student_table_command =  """CREATE TABLE IF NOT EXISTS
            Student(
                registration_number INTEGER PRIMARY KEY,  
                fump_level INTEGER,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
            """
        self.cursor.execute(self.student_table_command)
    
    def getFumpLevel(self, user_id):
        get_fumplevel_command = f"""
        SELECT fump_level
        FROM Student
        WHERE user_id = {user_id}
        """
        self.cursor.execute(get_fumplevel_command)
        return ( self.cursor.fetchall() )
    
    # TODO --> RegistrationNumber not well defined. It supposes Student is a single object, not a table.
    # Requires some 'information' to search i.e. name, user_id, etc...
    def getRegistrationNumber(self):
        error = "Not implemented yet."
        print(error)
        return False