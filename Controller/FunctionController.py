from MySql.MysqlCRUD.Config.ConnectDB import connectDB
from MySql.MysqlCRUD.Services.Deposit import Deposit
from MySql.MysqlCRUD.Services.Withdraw import Withdraw
from MySql.MysqlCRUD.Services.Display import Display
from MySql.MysqlCRUD.Services.IncreaseLimit import IncreaseLimit

class FunctionController:
    def __init__(self):
        self.db = connectDB()
        self.cursor = self.db.cursor()
    def view(self, id):
        viewData = Display()
        viewData.display(id)

    def deposit(self, id):
        depositAmount = Deposit()
        query = 'select loan, limit from Customers where c_id= %s'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        loan = result[0]
        limit = result[1]
        amount = int(input('Enter the amount you want to withdraw'))
        if amount <= loan:
            depositAmount.deposit_amount(id, amount, limit, loan)
        else:
            print('Cant deposit more than loan')
    def withdraw(self, id):
        withdrawAmount = Withdraw()
        query = 'select limit, loan from Customers where c_id= %s'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        limit = result[0]
        loan = result[1]
        amount = int(input('Enter the amount you want to withdraw'))
        if amount <= limit:
            withdrawAmount.withdraw_amount(id, amount, limit, loan)
        else:
            print('Cant withdraw more than limit')


    def increaselimit(self, id, num):
        increase = IncreaseLimit()
        if num == 2:
            query = 'select limit, loan from Customers where c_id= %s'
            self.cursor.execute(query, (id,))
            result = self.cursor.fetchone()
            limit = result[0]
            loan = result[1]
            if limit + loan <= 100000:
                increase.increase_limit(id,limit)
        else:
            print('Limit cannot be increased for ilver card users')
