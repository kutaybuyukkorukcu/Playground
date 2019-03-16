import sqlite3
import random
import time
import datetime

con = sqlite3.connect("lessons.db")

cursor = con.cursor()

def createTable():
  cursor.execute("CREATE TABLE IF NOT EXISTS dbTable (rTime REAL, date TEXT, keyword TEXT, value REAL)")

def addRandomValue():
  rTime = time.time()
  date = str(datetime.datetime.fromtimestamp(rTime).strftime('%Y-%M-%D %H:%M:%S'))
  keyword = 'Python Sqlite3'
  value = random.randrange(0,10)
  cursor.execute('INSERT INTO dbTable (rTime, date, keyword, value) VALUES(?, ?, ?, ?)',(rTime, date, keyword, value))
  con.commit()

""" createTable()
i = 0
while (i < 10):
    addRandomValue()
    time.sleep(1)
    i += 1 """

def getValues():
  cursor.execute('SELECT rTime, keyword, value FROM dbTable WHERE value = 2.0')
  data = cursor.fetchall()
  print(type(data))
  for i in data:
    print(i)

def updateValues():
  cursor.execute('SELECT value FROM dbTable')
  data = cursor.fetchall()
  print("First ones")
  for i in data:
    print(i)
  
  cursor.execute("UPDATE dbTable SET value = 99.0 WHERE value = 2.0")
  # cursor.execute('SELECT * FROM dbTable')
  cursor.execute('SELECT value FROM dbTable')
  
  data = cursor.fetchall()
  print("Values after the update")
  for i in data:
    print(i)

def deleteValues():
  cursor.execute('DELETE FROM dbTable WHERE value = 99.0')
  print("Values after deleting 99's")
  cursor.execute('SELECT value FROM dbTable WHERE value = 99.0')
  data = cursor.fetchall()
  for i in data:
    print(i)
  print("There's none")
  
updateValues()
deleteValues()
print("done")

con.close()
