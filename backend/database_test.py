import sys
sys.path.append("./dependencies")
import sqlite3
from dependencies.User import User
from dependencies.Student import Student
from dependencies.Employee import Employee
from dependencies.Teacher import Teacher
from dependencies.Restaurant import Restaurant
#from dependencies.Transaction import Transaction
#from dependencies.Card import Card

def isnull(target):
    if (target==[]):
        return True
    return False

class Database():
    def __init__(self, database_filename):
        self.conn = sqlite3.connect(database_filename)
        self.cursor = self.conn.cursor()
        self.User_Management = User(conn=self.conn, cursor=self.cursor)
        self.Student_Management = Student(conn=self.conn, cursor=self.cursor)
        self.Employee_Management = Employee(conn=self.conn, cursor=self.cursor)
        self.Teacher_Management = Teacher(conn=self.conn, cursor=self.cursor)
        self.Restaurant_Management = Restaurant(conn=self.conn, cursor=self.cursor)

    def print_database(self):
        table_list = ["User", "Student", "Teacher", "Employee", "Card", "Transaction", "Restaurant", "Menu"]
        for table in table_list:
            try:
                print_database_command = f"""
                SELECT *
                FROM {table}
                """
                self.cursor.execute(print_database_command)
                print(f"TABLE {table}", "\n")
                for element in self.cursor.fetchall():
                    print(element)
                print("\n")
            except:
                print(f"no table {table} available yet")
                continue
    
    def insertNewStudent(self, username, name, password, balance, registration_number, fump_level):
        result = self.Student_Management.insertNewStudent(username, name, password, balance, registration_number, fump_level)
        if result:
            return True
        return False
    
    def insertNewTeacher(self, username, name, password, balance, teacher_id ):
        result = self.Teacher_Management.insertNewTeacher(username=username, name=name, password=password, balance=balance, teacher_id=teacher_id)
        if result:
            return True
        return False
    
    def insertNewEmployee(self, username, name, password, balance, employee_id):
        result = self.Employee_Management.insertNewEmployee(username=username, name=name, password=password, balance=balance, employee_id=employee_id)
        if result:
            return True
        return False
    
    def getBalance(self, username):
        return self.User_Management.getBalance(username=username)
    
    def addBalance(self, username, value_to_add):
        actual_balance = self.getBalance(username)
        new_balance = actual_balance + value_to_add
        self.User_Management.setBalance(username=username, new_balance=new_balance)

    def subtractBalance(self, username, value_to_subtract):
        actual_balance = self.getBalance(username)
        new_balance = actual_balance - value_to_subtract
        self.User_Management.setBalance(username=username, new_balance=new_balance)

    def getPassword(self, username):
        return self.User_Management.getPassword(username=username)
    
    def getAmounttoPay(self, username):
        #testando se usuario é aluno, empregado ou professor para definir o preço a pagar
        command_for_student = f"""
        SELECT fump_level
        FROM Student
        WHERE username = "{username}"
        """
        result = self.cursor.execute(command_for_student).fetchall()
        if (not (isnull(result)) ): #alunos dependem do seu nivel de fump
            return self.Student_Management.getAmounttoPay(username=username)
        else:
            command_for_employee = f"""
            SELECT *
            FROM Employee
            WHERE username = "{username}"
            """
            result = self.cursor.execute(command_for_employee).fetchall()
            if (not (isnull(result)) ): #empregados paga 8.50
                return 8.50
        #o usuario nao eh aluno nem empregado
        return 13.00
    
    def insertRestaurant(self, restaurant_id, restaurant_name):
        """
        restaurant_id: Inteiro representando o ID do restaurante. \n
        restaurant_name: String contendo o nome do restaurante.
        """
        res = self.Restaurant_Management.insertRestaurant(restaurant_id=restaurant_id, restaurant_name=restaurant_name)
        if res:
            return True
        return False
        
    def insertMenu(self, menu_description, day, meal_period, restaurant_name):
        """
        menu_description: String contendo toda a alimentação do dia. \n
        day: Data em formato aaaa-mm-dd \n
        meal_period: String contendo Almoco ou Janta. \n
        restaurant_id: ID do restaurante que serve o menu descrito, no dia e período especificado. \n
        """
        get_id_command = f"""
        SELECT restaurant_id
        FROM Restaurant
        WHERE restaurant_name = "{restaurant_name}"
        """
        restaurant_id = self.cursor.execute(get_id_command).fetchall()[0][0]
        res = self.Restaurant_Management.insertMenu(menu_description=menu_description, day=day, meal_period=meal_period, restaurant_id=restaurant_id)
        if res:
            return True
        return False
    
    def getMenu(self, restaurant_name, day, meal_period):
        """
        restaurant_name: String com o nome do restaurante.\n
        day: Data em formato aaaa-mm-dd. \n
        meal_period: String (Almoco ou Janta). \n
        """
        self.Restaurant_Management.getMenu(restaurant_name=restaurant_name, day=day, meal_period=meal_period)



database = Database("testdatabase.db")
database.insertNewStudent(username="antonio.caetano", name="Antonio Caetano Neves Neto", password="antoniosenha123", balance=10.50, registration_number=2022043555, fump_level=5)
database.insertNewStudent(username="raphael.mendes", name="Raphael A. Carreiro Mendes", password="raphaelsenha123", balance=5.60, registration_number=2022043556, fump_level=4)
database.insertNewStudent(username="bernardo.dutra", name="Bernardo Dutra Lemos", password="bdlemossenha123", balance=12.20, registration_number=2022043557, fump_level=2)
database.insertNewStudent(username="joao.lucas", name="João Lucas Simões Moreira", password="joaolucassenha123", balance=2.30, registration_number=2022043558, fump_level=1)

print(f"""antonio balance: {database.getBalance("antonio.caetano")}""")
print(f"""raphael balance: {database.getBalance("raphael.mendes")}""")

print(f"""bernardo password: {database.getPassword("bernardo.dutra")}""")
print(f"""joao lucas password: {database.getPassword("joao.lucas")}""")


