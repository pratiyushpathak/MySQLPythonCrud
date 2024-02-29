from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class IncreaseLimit:
    def __init__(self):
        self.db = connectDB()
        self.db.autocommit = True
        self.cursor = self.db.cursor()

    def increase_limit(self, id,limit):
        query = 'UPDATE Customers SET balance = %s WHERE c_id = %s'
        newLimit = limit + 50000
        try:
            self.cursor.execute(query, (newLimit, id))
            self.db.commit()  # Commit the transaction
            print('Limit Increased successfully')
        except Exception as e:
            print('Error:', e)
            self.db.rollback()