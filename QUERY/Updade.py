from turtle import update

from DB_Mysql.Base.DB import DB

class Update(DB):
    cxnx = DB()
    print(cxnx.connect("UPDATE customers SET first_name = 'rivka' WHERE category_id = 1",update))
