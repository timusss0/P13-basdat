import mysql.connector as connector;
try:
    connection=connector.connect(
        user="root",
        password=''
    )
except:
    print("""
    There was a problem connecting to the database.
    Please check your username or the password.
    """)