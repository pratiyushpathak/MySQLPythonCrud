
from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class Deposit:
    def __init__(self):
        self.db = connectDB()
        self.db.autocommit = True
        self.cursor = self.db.cursor()

    def deposit_amount(self, id, amount, limit, loan):
        query = 'UPDATE Customers SET balance = %s, loan = %s WHERE c_id = %s'
        newlimit = limit + amount
        newloan = loan - amount
        try:
            self.cursor.execute(query, (newlimit, newloan, id))
            self.db.commit()  # Commit the transaction
            print('Amount Deposited successfully')
        except Exception as e:
            print('Error:', e)
            self.db.rollback()
