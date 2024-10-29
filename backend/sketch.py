import sqlite3
import sys
sys.path.append("./dependencies")
from dependencies.User import User
from dependencies.Student import Student

# define connection and cursor

connection = sqlite3.connect('bandecopay.db')

cursor = connection.cursor()

# adding tables on db

user_table_command = """CREATE TABLE IF NOT EXISTS
User(
    user_id INTEGER PRIMARY KEY, 
    name TEXT, 
    balance FLOAT, 
    price_to_pay FLOAT
    );
"""

cursor.execute(user_table_command)#USER

student_table_command = """CREATE TABLE IF NOT EXISTS
Student(
    registration_number INTEGER PRIMARY KEY,  
    fump_level INTEGER,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    );
"""

cursor.execute(student_table_command)#STUDENT

employee_table_command = """CREATE TABLE IF NOT EXISTS
Employee(
    employee_id INTEGER PRIMARY KEY, 
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    );
"""

cursor.execute(employee_table_command)#EMPLOYEE

teacher_table_command = """CREATE TABLE IF NOT EXISTS
Teacher(
    teacher_id INTEGER PRIMARY KEY, 
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    );
"""

cursor.execute(teacher_table_command)#TEACHER

card_table_command = """CREATE TABLE IF NOT EXISTS
Card(
    card_id TEXT PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    );
"""

cursor.execute(card_table_command) #CARD

restaurant_table_command = """CREATE TABLE IF NOT EXISTS
Restaurant(
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name TEXT
    );
"""

cursor.execute(restaurant_table_command)#RESTAURANT

menu_table_command = """CREATE TABLE IF NOT EXISTS
Menu(
    menu_description TEXT,
    day DATE,
    day_period TEXT,
    restaurant_id INTEGER,
    FOREIGN KEY(restaurant_id) REFERENCES Restaurant(restaurant_id)
    );
"""

cursor.execute(menu_table_command)

transaction_table_command = """CREATE TABLE IF NOT EXISTS
Traction(
    transaction_id INTEGER PRIMARY KEY,
    transaction_type TEXT,
    transaction_value FLOAT,
    transaction_date DATE,
    restaurant TEXT,
    user_id INTEGER,
    card_id TEXT,
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    FOREIGN KEY(card_id) REFERENCES Card(card_id)
    );
"""

cursor.execute(transaction_table_command)

# insert examples

cursor.execute("""
INSERT INTO User
VALUES (123, "Antonio Caetano", 201.50, 6.50)
""")

cursor.execute("""
INSERT INTO Student 
VALUES (2022043213, 4, 123)
""")

cursor.execute("""
INSERT INTO Card
VALUES ("CD01_043", 123)
""")

cursor.execute("""
INSERT INTO Traction
VALUES (1, "pagamento_RU", 6.50, "RU01", 123, "CD01_043")
""")

# get tables function

def print_tables(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

print(print_tables("User"))
datalist = print_tables("User")
print(print_tables("Student"))
print(print_tables("Card"))
print(print_tables("Traction"))

cursor.execute(f"""SELECT fump_level 
               FROM 
                User INNER JOIN Student ON User.user_id = Student.user_id 
               WHERE 
                User.user_id = 123""")
f_level = cursor.fetchall()[0][0]
print(f_level)