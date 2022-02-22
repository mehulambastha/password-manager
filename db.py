from PyQt5 import QtSql
import os

os.remove("data/data.sqlite")

db = QtSql.QSqlDatabase.addDatabase("QSQLITE")

db.setDatabaseName("data/data.sqlite")


if not db.open():
    print("error")


passhidden = input("ENTER A PASSWORD: ")

query = QtSql.QSqlQuery()
query.exec_("Create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, password VARCHAR(100) NOT NULL);")
query.exec_(f"insert into userdata (password) values('{passhidden}')")
query.exec_("select * from userdata where id=1;")
query.first()
print(query.value("password"))