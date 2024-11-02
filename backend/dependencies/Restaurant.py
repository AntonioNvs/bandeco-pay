import sys
sys.path.append("./")
import sqlite3

class Restaurant():
    def __init__(self, conn):
        self.conn = conn
        self.restaurant_table_command = """CREATE TABLE IF NOT EXISTS
            Restaurant(
            restaurant_id INTEGER PRIMARY KEY,
            restaurant_name TEXT
            );
        """
        cursor = self.conn.cursor()
        cursor.execute(self.restaurant_table_command)
        self.conn.commit()
        
        self.menu_table_command = """CREATE TABLE IF NOT EXISTS
            Menu(
            menu_description TEXT,
            day DATE,
            meal_period TEXT,
            restaurant_id INTEGER,
            FOREIGN KEY(restaurant_id) REFERENCES Restaurant(restaurant_id)
            );
        """

        cursor.execute(self.menu_table_command)
        self.conn.commit()
        cursor.close()

    def insertRestaurant(self, restaurant_id, restaurant_name):
        """
        restaurant_id: Inteiro representando o ID do restaurante. \n
        restaurant_name: String contendo o nome do restaurante.
        """
        insert_restaurant_command = f"""
        INSERT INTO Restaurant
        VALUES ({restaurant_id}, "{restaurant_name}")
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_restaurant_command)
        self.conn.commit()
        cursor.close()

        return True

    def insertMenu(self, menu_description, day, meal_period, restaurant_id):
        """
        menu_description: String contendo toda a alimentação do dia. \n
        day: Data em formato aaaa-mm-dd \n
        meal_period: String contendo Almoco ou Janta. \n
        restaurant_id: ID do restaurante que serve o menu descrito, no dia e período especificado. \n
        """
        insert_menu_command = f"""
        INSERT INTO Menu
        VALUES ("{menu_description}", {day}, "{meal_period}", {restaurant_id})
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_menu_command)
        self.conn.commit()
        cursor.close()

        return True


    def getRestaurantNameById(self, restaurant_id):
        """
            restaurant_id: int, identificador único do restaurante

            returns: string, nome do restaurante
        """
        get_menu_command = f"""
            SELECT restaurant_name
            FROM Restaurant
            WHERE restaurant_id == {restaurant_id}
        """

        cursor = self.conn.cursor()
        cursor.execute(get_menu_command)
        result = cursor.fetchall()[0][0]
        cursor.close()

        return result

    def getMenu(self, restaurant_name, day, meal_period):
        """
        restaurant_name: String com o nome do restaurante.\n
        day: Data em formato aaaa-mm-dd. \n
        meal_period: String (Almoco ou Janta). \n
        """
        get_menu_command = f"""
            SELECT menu_description
            FROM 
                Menu INNER JOIN Restaurant
                ON Restaurant.restaurant_id = Menu.restaurant_id
            WHERE Restaurant.restaurant_name = "{restaurant_name}" AND Menu.day = {day} AND Menu.meal_period = "{meal_period}"
        """
        cursor = self.conn.cursor()
        result = cursor.execute(get_menu_command).fetchall()[0][0]
        cursor.close()
        return result
        
    
