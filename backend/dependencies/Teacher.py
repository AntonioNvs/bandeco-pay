import sys
sys.path.append("./")
import sqlite3
from User import User

class Teacher(User):
    def __init__(self, conn, cursor):
        super().__init__(conn, cursor)
        self.teacher_table_command = """CREATE TABLE IF NOT EXISTS
            Teacher(
                teacher_id INTEGER PRIMARY KEY, 
                username TEXT,
                FOREIGN KEY(username) REFERENCES User(username)
            );
        """
        self.cursor.execute(self.teacher_table_command)

    def insertNewTeacher(self, username, name, password, balance, teacher_id):
        self.insertNewUser(username=username, name=name, password=password, balance=balance)
        insert_teacher_command = f"""
        INSERT INTO Teacher
        VALUES ({teacher_id}, "{username}")
        """
        self.cursor.execute(insert_teacher_command)
        return True
    
    def getTeacherId(self, username):
        get_teacherid_command=f"""
        SELECT teacher_id
        FROM Teacher
        WHERE username = "{username}"
        """
        return ( self.cursor.execute(get_teacherid_command).fetchall() )[0][0]