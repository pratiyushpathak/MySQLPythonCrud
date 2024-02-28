from MySql.MysqlCRUD.Config.ConnectDB import ConnectDB
from MySql.MysqlCRUD.Controller.FunctionController import FunctionController
class CardController:

    def subMenu(self):
        print('1. View')
        print('2. Withdraw')
        print('3. Deposit')
        print('4. Increase Limit')
        print('5. Exit')
    @staticmethod
    def cardcontroller(num, id, fname):
        print('Hii,',fname)
        flag = False
        functions = FunctionController()

        while not flag:
            print(f"*********{'SILVER' if num == 1 else 'GOLD'}**********")
            CardController.subMenu(None)
            options = int(input('Enter your choice: '))

            match options:
                case 1:
                    functions.view(id)
                case 2:
                    functions.withdraw(id)
                case 3:
                    functions.deposit(id)
                case 4:
                    functions.increaseLimit(id,num)
                case 5:
                    flag = True
                case _:
                    print('Enter a valid choice')