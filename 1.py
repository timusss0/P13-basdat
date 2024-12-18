import mysql.connector as connector

connection = connector.connect(user="root",password="",port=3306,
                               host="localhost",database="pertemuan13-BD")
try:
    connection=connector.connect(user="not_root!",password="")
except:
    print("there was an error connection to the database")