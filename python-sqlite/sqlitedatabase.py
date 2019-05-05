import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def createTable():
  cursor.execute("CREATE TABLE IF NOT EXISTS students (ad TEXT, soyad TEXT, numara INT, ogrencinotu INT)")
  
def addValue():
  cursor.execute('INSERT INTO students VALUES ("Berfin", "Omegalul", 11, 32)')
  con.commit()
  con.close()

createTable()
addValue()
print("basariyla dondu")