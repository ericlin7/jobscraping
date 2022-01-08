import mysql.connector
import csv

db = mysql.connector.connect(host='localhost', database='testdatabase', user='root', password='74$ppkt123')
mycursor = db.cursor()
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")  
#mycursor.execute("DROP TABLE IF EXISTS Person")
#mycursor.execute("INSERT INTO Person (name, age) Values (%s, %s)", ("bob", 22))
#db.commit()
#mycursor.execute("SHOW TABLES")
#mycursor.execute("ALTER TABLE Person ADD COLUMN gender VARCHAR(50)")
#mycursor.execute("SELECT * FROM Person")
#mycursor.execute("ALTER TABLE Person name last VARCHAR(50) NOT NULL")
#mycursor.execute("UPDATE Person SET gender = 'M'")
#db.commit()
#mycursor.execute("DESCRIBE Person")

mycursor.execute("CREATE TABLE Jobs (title VARCHAR(50), names smallint UNSIGNED, description int PRIMARY KEY AUTO_INCREMENT)")  

#for x in mycursor:
#    print(x)  

csv_data = csv.reader('test.csv')
for row in csv_data:

    mycursor.execute('INSERT INTO testcsv(TITLES, \
          NAMES, DESCRIPTION )' \
          'VALUES("%s", "%s", "%s")', 
          row)

db.commit()