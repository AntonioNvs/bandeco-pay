import sys
sys.path.append("./")
import sqlite3
from User import User

class Teacher(User):
    
    def __init__(self, database_filename):
        super.__init__(database_filename)
        self.teacher_table_command = """CREATE TABLE IF NOT EXISTS
            Teacher(
                teacher_id INTEGER PRIMARY KEY, 
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
        """
        self.cursor.execute(self.employee_table_command)#EMPLOYEE
    
    # TODO --> EmployeeId not well defined. It supposes Student is a single object, not a table.
    # Requires some 'information' to search i.e. name, user_id, etc...
    def getEmployeeId(self, user_id):
        error = "Not implemented yet."
        print(error)
        return False