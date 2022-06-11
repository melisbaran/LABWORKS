import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",  password = "")

cursor = db.cursor()

cursor.execute("DROP DATABASE IF EXISTS movie")
cursor.execute("CREATE DATABASE movie")

connection = mysql.connector.connect(host="localhost", user="root", password="", database="movie")

if connection.is_connected():
    print("You are connected to MySQL server.")

try:
 connection = mysql.connector.connect(host="localhost", user="root", database="movie", passwd="")

 createQuery = """CREATE TABLE MarvelMovies(ID INT(50) NOT NULL,Movie VARCHAR(150) NOT NULL, Date VARCHAR(150) NOT NULL, MCU_Phase VARCHAR(150) NOT NULL,PRIMARY KEY (ID))"""

 cursor.execute(createQuery)

 result = cursor.execute(createQuery)

 print("Creation is successful!")

 path = open('//Users//melo//Desktop//Marvel.txt', 'r')


 while path:
    text = path.readline()
    if text == "":
        break

    splitlines = text.split()

    insertTableQuery = """ INSERT INTO NewTable (ID , MOVIE, DATE, MCU_PHASE)
                               VALUES (%s, %s, %s ,%s )"""

    record = (splitlines[0], splitlines[1], splitlines[2], splitlines[3])

    cursor.execute(insertTableQuery, record)
    db.commit()


 connection.commit()


 listQuery = "SELECT * FROM Marvel"
 cursor.execute(listQuery)
 rows = cursor.fetchall()


 for row in rows:
    print(row)

 sqlDeleteMovie = "DELETE FROM NewTable WHERE MOVIE = 'TheIncredibleHulk'"

 cursor = connection.cursor()
 cursor.execute(sqlDeleteMovie)
 connection.commit()

 sqlList2 = "SELECT * FROM NewTable Where MCU_PHASE = 'Phase2'"
 cursor = connection.cursor()
 cursor.execute(sqlList2)
 rec = cursor.fetchall()


 for row2 in rec:
    print(row2)

 sqlDate = "UPDATE NewTable SET DATE = 'November 3, 2017' WHERE MOVIE = 'Thor:Ragnork'"
 cursor = connection.cursor()
 cursor.execute(sqlDate)
 connection.commit()

except mysql.connector.Error as error:
    print("FAILED : {}".format(error))

finally:

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL is closed")






