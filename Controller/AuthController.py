from MySql.MysqlCRUD.Config.ConnectDB import connectDB
from MySql.MysqlCRUD.Controller.CardController import CardController
class AuthController:

    @staticmethod
    def authcontroller(email, id):
        while True:
            print('Your Email is: ', email)
            password = input("Enter Your Password: ")
            connection = connectDB()
            cursor = connection.cursor()

            cursor.execute("SELECT firstName,password,cardType FROM Customers WHERE c_id=%s", (id,))
            resultset = cursor.fetchone()
            fname = resultset[0]
            if resultset[1] == password:
                print('User Authenticated')
                cardType = resultset[2]
                match cardType:
                    case 'silver':
                        CardController.cardcontroller(1, id, fname)
                    case 'gold':
                        CardController.cardcontroller(2, id, fname)
                break
            else:
                print('Please try Again')



