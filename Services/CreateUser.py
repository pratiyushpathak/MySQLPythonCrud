
from MySql.MysqlCRUD.Config.ConnectDB import connectDB

class CreateUser:
    def __init__(self):
        self.db = connectDB()
        self.db.autocommit = True
        self.cursor = self.db.cursor()

    def create_user(self, email):
        query = 'insert into Customers(firstName, lastName, email, password,loan, cardType, balance ) values(%s, %s, %s, %s, %s, %s, %s)'
        first_name= input('Enter Your First Name: ')
        last_name= input('Enter Your Last Name: ')
        card_type = input('Eter your Card Type[Silver/Gold]: ')
        password = input('Enter your password')
        loan=0

        def balance(card_type):
            if card_type.lower() == 'silver':
                return 50000
            elif card_type.lower() == 'gold':
                return 100000
            else:
                while True:
                    card_type = input('Enter a valid card type: ')
                    if card_type.lower() == 'silver':
                        return 50000
                    elif card_type.lower() == 'gold':
                        return 100000
        final_balance= balance(card_type)
        try:
            self.cursor.execute(query, (first_name, last_name, email, password,loan, card_type, final_balance))
            self.db.commit()  # Commit the transaction
            print('User Added Successfully')
        except Exception as e:
            print('Error:', e)
            self.db.rollback()