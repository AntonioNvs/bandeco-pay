import sys
import time

sys.path.append("./dependencies")
import sqlite3
from dependencies.User import User
from dependencies.Student import Student
from dependencies.Employee import Employee
from dependencies.Teacher import Teacher
from dependencies.Restaurant import Restaurant
from dependencies.Transaction import Transaction
from dependencies.Card import Card

from werkzeug.security import generate_password_hash


def isnull(target):
    if (target==[]):
        return True
    return False

lunch ="""Salada de Alface Crespa
Salada Tabule
Feijão Carioca
Isca de Frango Colorida
Bife de milho
Macarrão parafuso com brócolis
Arroz Branco
Molho de Hortelã
Sobremesa Laranja
Copo Refresco
"""

class Database():
    def __init__(self, database_filename):
        self.conn = sqlite3.connect(database_filename, check_same_thread=False, timeout=5)
        self.User_Management = User(conn=self.conn)
        self.Student_Management = Student(conn=self.conn)
        self.Employee_Management = Employee(conn=self.conn)
        self.Teacher_Management = Teacher(conn=self.conn)
        self.Restaurant_Management = Restaurant(conn=self.conn)
        self.Card_Management = Card(conn=self.conn)
        self.Transaction_Management = Transaction(conn=self.conn)

        self.initializate_database_data()

    def close(self):
        self.conn.close()

    def initializate_database_data(self):
        if self.User_Management.verifyIfUsernameExists("antonio.caetano"): return

        self.insertNewStudent(username="antonio.caetano", name="Antonio Caetano Neves Neto", password=generate_password_hash("antoniosenha123"), registration_number=2022043555, fump_level=5)
        
        self.insertNewStudent(username="raphael.mendes", name="Raphael A. Carreiro Mendes", password=generate_password_hash("raphaelsenha123"), registration_number=2022043556, fump_level=4)
        self.insertNewStudent(username="bernardo.dutra", name="Bernardo Dutra Lemos", password=generate_password_hash("bdlemossenha123"), registration_number=2022043557, fump_level=2)
        self.insertNewStudent(username="joao.lucas", name="João Lucas Simões Moreira", password=generate_password_hash("joaolucassenha123"), registration_number=2022043558, fump_level=1)

        self.insertRestaurant(restaurant_id=1, restaurant_name="Pampulha 1")
        self.insertRestaurant(restaurant_id=2, restaurant_name="Pampulha 2")
        self.insertRestaurant(restaurant_id=3, restaurant_name="Campus Saúde")
        self.insertRestaurant(restaurant_id=4, restaurant_name="Campus Direito")
        self.insertRestaurant(restaurant_id=5, restaurant_name="Campus ICA")

        for date in ["2024-11-03", "2024-11-04", "2024-11-05", "2024-11-06", "2024-11-07", "2024-11-08", "2024-11-09"]:
            for j, restaurant_name in enumerate(["Pampulha 1", "Pampulha 2", "Campus Saúde", "Campus Direito", "Campus ICA"]):
                self.insertMenu(lunch, date, "Almoco", restaurant_name, j+1)
                self.insertMenu(lunch, date, "Janta", restaurant_name, j+1)

        self.insertNewCard(card_id="7CA288BD", username="antonio.caetano")
        self.insertNewCard(card_id="64090D64", username="raphael.mendes")
        self.insertNewCard(card_id="8E87EE9C", username="bernardo.dutra")

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
            
    
    def insertNewCard(self, card_id, username):
        """
        card_id: String - Identificador Único do cartão do usuário
        username: String - Nome do usuário.\n

        returns: Verdadeiro, se não houve problemas em adicionar ao banco de dados.
        """
        return self.Card_Management.insertNewCard(card_id, username)


    def insertNewStudent(self, username, name, password, registration_number, fump_level):
        """
        username: String - Nome do usuário.\n
        name: String - Nome completo do usuário.\n
        password: String - Senha do usuário.\n
        registration_number: Inteiro - N° de matrícula do aluno.\n
        fump_level: Inteiro [1-5] - Grau do aluno na prioridade de assistência social (FUMP).\n

        returns: Verdadeiro, se não houve problemas em adicionar ao banco de dados.
        """
        result = self.Student_Management.insertNewStudent(username, name, password, 0.0, registration_number, fump_level)
        if result:
            return True
        return False
    
    def insertNewTeacher(self, username, name, password, teacher_id ):
        """
        username: String - Nome do usuário.\n
        name: String - Nome completo do usuário.\n
        password: String - Senha do usuário.\n
        teacher_id: Inteiro - ID do professor.\n

        returns: Verdadeiro, se não houve problemas em adicionar ao banco de dados.
        """
        result = self.Teacher_Management.insertNewTeacher(username=username, name=name, password=password, balance=0.0, teacher_id=teacher_id)
        if result:
            return True
        return False
    
    def insertNewEmployee(self, username, name, password, employee_id):
        """
        username: String - Nome do usuário.\n
        name: String - Nome completo do usuário.\n
        password: String - Senha do usuário.\n
        employee_id: Inteiro - ID do empregado.\n

        returns: Verdadeiro, se não houve problemas em adicionar ao banco de dados.
        """
        result = self.Employee_Management.insertNewEmployee(username=username, name=name, password=password, balance=0.0, employee_id=employee_id)
        if result:
            return True
        return False
    
    def insertNewTransaction(self, type_, value, transaction_date, username, restaurant_id=1):
        card_id = self.Card_Management.getCardIdFromUserName(username=username)

        result = self.Transaction_Management.insertTransaction(
            type_=type_, 
            value=value, 
            transaction_date=transaction_date, 
            username=username, 
            card_id=card_id,
            restaurant_id=restaurant_id
        )
        
        if result:
            return True
        return False


    def getRestaurantNameById(self, restaurant_id):
        """
            restaurant_id: int, identificador único do restaurante

            returns: string, nome do restaurante
        """
        return self.Restaurant_Management.getRestaurantNameById(restaurant_id)


    def getTransactionsByUser(self, username):
        return self.Transaction_Management.retrieveUserTransaction(username=username)

    def getBalance(self, username):
        """
        username: String contendo o nome do usuário. \n

        returns: Float contendo o saldo do usuário.
        """
        return self.User_Management.getBalance(username=username)
    
    def getOwner(self, card_id):
        """
        card_id: String representando o ID do cartão.\n

        return: String contendo o nome do usuário que é dono do cartão.
        """
        return self.Card_Management.getOwner(card_id=card_id)
    
    def getUserName(self, username):
        """
        username: String, representando o username do usuário

        return: String, nome completo do usuário
        """

        return self.User_Management.getName(username)

    def addBalance(self, username, value_to_add):
        """
        username: String contendo o nome do usuário a receber o valor especificado. \n
        value_to_add: Float representando o valor a ser adicionado.
        """
        actual_balance = self.getBalance(username)
        new_balance = actual_balance + value_to_add
        self.User_Management.setBalance(username=username, new_balance=new_balance)

    def subtractBalance(self, username, value_to_subtract):
        """
        username: String contendo o nome do usuário a perder o valor especificado. \n
        value_to_add: Float representando o valor a ser subtraído.
        """
        actual_balance = self.getBalance(username)
        new_balance = actual_balance - value_to_subtract
        self.User_Management.setBalance(username=username, new_balance=new_balance)

    def getPassword(self, username):
        """
        username: String contendo o nome do usuário.\n

        returns: String contendo a senha do usuário.
        """
        return self.User_Management.getPassword(username=username)
    
    def getAmounttoPay(self, username):
        """
        username: String contendo o nome do usuário.

        returns: Float contendo o valor a ser pago em uma refeição pelo usuário.
        """
        #testando se usuario é aluno, empregado ou professor para definir o preço a pagar
        command_for_student = f"""
        SELECT fump_level
        FROM Student
        WHERE username = "{username}"
        """
        cursor = self.conn.cursor()
        result = cursor.execute(command_for_student).fetchall()
        cursor.close()
        if (not (isnull(result)) ): #alunos dependem do seu nivel de fump
            return self.Student_Management.getAmounttoPay(username=username)
        else:
            command_for_employee = f"""
            SELECT *
            FROM Employee
            WHERE username = "{username}"
            """
            cursor = self.conn.cursor()
            result = cursor.execute(command_for_employee).fetchall()
            cursor.close()
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
        
    def insertMenu(self, menu_description, day, meal_period, restaurant_name, restaurant_id):
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
        return self.Restaurant_Management.getMenu(restaurant_name=restaurant_name, day=day, meal_period=meal_period)

