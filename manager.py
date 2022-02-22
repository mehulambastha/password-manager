from PyQt5 import QtWidgets, QtSql, QtGui, QtCore
from login_ui import Ui_Form
import sys
from dashboard import Ui_dashboard


class myApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.openDB()
        self.pushButton.clicked.connect(self.checkUser)

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/data.sqlite")
        if not self.db.open():
            print("Could not open database")
        self.query = QtSql.QSqlQuery()

    def checkUser(self):
        self.openDB()
        pswd = self.lineEdit_2.text()
        self.query.exec_(
            "select * from userdata where password = '%s';" % (pswd))
        self.query.first()
        print(self.query.value)
        if self.query.value("password") != None:
            print("Login Successfull!")
            self.label_4.setText("Login Successful")
            self.close()
            self.welcomeWindow = QtWidgets.QMainWindow()
            self.ui = Ui_dashboard()
            self.ui.setupUi(self.welcomeWindow)
            self.welcomeWindow.show()
        else:
            self.label_4.setText("INVALID PASSWORD")
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = myApp()
    Form.show()
    sys.exit(app.exec_())
