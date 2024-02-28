from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class IncreaseLimit:
    def __init__(self):
        self.db = connectDB()
        self.cursor = self.db.cursor()

    def increase_limit(self, id,limit):
        query = 'UPDATE Customers SET limit = %s WHERE id = %s'
        newLimit = limit + 50000
        self.cursor.execute(query, (newLimit, id,))
        print('Limit Increased Successfully')