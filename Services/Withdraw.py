from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class Withdraw:
    def __init__(self):
        self.db = connectDB()
        self.cursor = self.db.cursor()

    def withdraw_amount(self, id, amount, limit, loan):
        query = 'UPDATE Customers SET limit = %s, loan = %s WHERE id = %s'
        newlimit = limit - amount
        newloan = loan + amount
        self.cursor.execute(query, (newlimit, newloan, id))
        print('Amount Withdrawn successfully')