from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class Display:
    def __init__(self):
        self.db = connectDB()
        self.db.autocommit = True
        self.cursor = self.db.cursor()

    def display(self, id):
        query = 'select * from Customers where c_id= %s'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        print("Name:",result[1]+' '+result[2])
        print("Card Type:", result[6])
        print("Loan amount:", result[5])
        print("Balance:", result[7])