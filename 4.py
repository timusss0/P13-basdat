import mysql.connector as connector
connection = connector.connect(user="root",password="",port=3306)
cursor = connection.cursor()
create_database_query="""CREATE DATABASE litle_demon"""
cursor.execute(create_database_query)
use_database_query="""USE litle_demon"""
cursor.execute(use_database_query)
create_menuitem_table="""
CREATE TABLE MenuItem(
ItemID INT AUTO_INCREMENT,
Nama VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY_KEY(Item)
)
"""

