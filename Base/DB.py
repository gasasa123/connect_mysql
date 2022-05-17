import mysql.connector

class DB():
  mydb = my_connect = None
  def __init__(self):
    self.mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rivka1234!",
    database="sakila"
  )

  def connect(self,sql,db_type):
    mycursor = self.mydb.cursor()
    mycursor.execute(sql)
    if db_type == 'select':
      return mycursor.fetchall()
    else:
      self.mydb.comit()




# a = mydb.cursor()
# a.execute("select * from actor")
# print(a.fetchall())
#
# a = mydb.cursor()
# a.execute("select * from film")
# print(a.fetchall())
#
# a= mydb.cursor()
# a.execute("SELECT COUNT(*) FROM actor")
# print(a.fetchall())
#
# a= mydb.cursor()
# a.execute("SELECT COUNT(*) FROM film")
# print(a.fetchall())


