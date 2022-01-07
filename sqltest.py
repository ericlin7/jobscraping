import mysql.connector

db = mysql.connector.connect(host='localhost', database='testdatabase', user='root', password='74$ppkt123')
mycursor = db.cursor()
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("DESCRIBE Person")
for x in mycursor:
    print(x)    