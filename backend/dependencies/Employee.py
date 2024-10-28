import sys
sys.path.append("./")
import sqlite3
from User import User

class Employee(User):
    def __init__(self, conn, cursor):
        super().__init__(conn, cursor)
        self.employee_table_command = """CREATE TABLE IF NOT EXISTS
            Employee(
                employee_id INTEGER PRIMARY KEY, 
                username TEXT,
                FOREIGN KEY(username) REFERENCES User(username)
            );
        """
        self.cursor.execute(self.employee_table_command)

    def insertNewEmployee(self, username, name, password, balance, employee_id):
        self.insertNewUser(username=username, name=name, password=password, balance=balance)
        insert_employee_command = f"""
        INSERT INTO Employee
        VALUES ({employee_id}, "{username}")
        """
        self.cursor.execute(insert_employee_command)
        return True
    
    def getEmployeeId(self, username):
        get_employeeid_command=f"""
        SELECT employee_id
        FROM Employee
        WHERE username = "{username}"
        """
        return ( self.cursor.execute(get_employeeid_command).fetchall() )[0][0]