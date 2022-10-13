import mysql.connector as mysql
from mysql.connector import Error
db=mysql.connect(
    host="localhost",
    user="root",
    passwd="acandmysql",
    database="testdb")
print(db)
cursor = db.cursor()
str = "CREATE TABLE people(Name varchar(50),Age int,City varchar (50))"
cursor.execute(str)
