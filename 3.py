import mysql.connector as connector

try:
    connection=connector.connect(
        user="root",
        password="",
        database="pertemuan13-BD"
)
except connector.Error as er:
    print("error code:",er.errno)
    print("error meesage:",er.msg)
