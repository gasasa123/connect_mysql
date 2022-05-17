from DB_Mysql.Base.DB import DB

class Select(DB):
    cxnx = DB()
    print(cxnx.connect("select * from actor" , select))
    print(cxnx.connect("select * from address"))
    print(cxnx.connect("select * from film"))
    print(cxnx.connect("select * from category"))
    print(cxnx.connect("select * from customer"))
    