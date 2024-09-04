from db import db_connection

def read_data():
    connetion = db_connection()
    cursor = connetion.cursor()
    cursor.execute("SELECT * FROM PERSONAL")
    result = cursor.fetchall()
    for row in result:
        print(row)
    
    cursor.close()
    connetion.close()

read_data()

