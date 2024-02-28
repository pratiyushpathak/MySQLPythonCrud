from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class Display:
    def __init__(self):
        self.db = connectDB()
        self.cursor = self.db.cursor()

    def display(self, id, amount):
        query = 'select * from Customers where c_id= %s'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        print(result)