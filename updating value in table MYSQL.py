import mysql.connector as mysql
from mysql.connector import Error
db=mysql.connect(
    host="localhost",
    user="root",
    passwd="acandmysql",
    database="testdb")
print(db)
cursor = db.cursor() # instantiates object ehivch can be used to execute operations on database
print(db.is_connected()) # gives boolean whether the databse is connected or not
str="""update people set Name = "rekha" where Age = 0 """   # update and set are used 
cursor.execute(str)
db.autocommit=True
print("changes made")