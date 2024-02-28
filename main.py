
from Config.ConnectDB import connectDB
from Controller.AuthController import AuthController

connection = connectDB()
cursor = connection.cursor()
email = input('Enter your email: ')

cursor.execute("SELECT c_id FROM Customers WHERE email=%s", (email,))
# id = cursor.execute('select c_id from Customers where email')

resultset = cursor.fetchone()
id = resultset[0]
# print(resultset[0])
if resultset:
    AuthController.authcontroller(email, id)