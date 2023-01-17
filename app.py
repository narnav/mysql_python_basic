import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PASSWORD"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE delme1")

print(mydb)