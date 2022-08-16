import mysql.connector as mysql
from mysql.connector import Error
db=mysql.connect(
    host="localhost",
    user="root",
    passwd="acandmysql",
    database="testdb")
print(db)
cursor = db.cursor() # instantiates object ehivch can be used to execute operations on database
print(db.is_connected())
cursor.execute("select*from testdb.people")
result=cursor.fetchall()
for rows in result:
    print(result)
    print("\n")
print("task done")
cursor.close()
db.close()
