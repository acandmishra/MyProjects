import mysql.connector as mysql
from mysql.connector import Error
db=mysql.connect(
    host="localhost",
    user="root",
    passwd="acandmysql",
    database="testdb")
print(db)
cursor = db.cursor() 
print(db.is_connected()) 
cursor.execute('Delete from people where Name="rekha"')
db.autocommit=True