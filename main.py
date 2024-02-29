
from Config.ConnectDB import connectDB
from Controller.AuthController import AuthController
from Services.CreateUser import CreateUser

def auth(email, resultset):
    id = resultset[0]
    AuthController.authcontroller(email, id)

def create(email):
    createUser = CreateUser()
    createUser.create_user(email)
    cursor.execute("SELECT c_id FROM Customers WHERE email=%s", (email,))
    new_resultset = cursor.fetchone()
    print(new_resultset)
    auth(email, new_resultset)

connection = connectDB()
cursor = connection.cursor()
email = input('Enter your email: ')

cursor.execute("SELECT c_id FROM Customers WHERE email=%s", (email,))
resultset = cursor.fetchone()
# print(resultset[0])


if resultset:
    auth(email, resultset)
else:
    create(email)