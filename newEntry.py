# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEntry.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import data_main
import sys
import os 

class Ui_Form(object):
    def setupUi(self, Form, new_data):
        Form.setObjectName("Form")
        Form.resize(732, 400)
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Lobster-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Roboto-Medium.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Poppins-SemiBold.ttf.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Poppins-Medium.ttf')
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 711, 380))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(15, 32, 39, 255), stop:0.505263 rgba(32, 58, 67, 255), stop:1 rgba(44, 83, 100, 255));\n"
                                  "border-radius: 15px;")
        self.widget.setObjectName("widget")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(170, 0, 390, 70))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(60)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FFF;\n"
                                 "background-color:rgba(0,0,0,0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Poppins")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#FFF;\n"
                                   "background-color:rgba(0,0,0,0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(133, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Poppins")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#FFF;\n"
                                   "background-color:rgba(0,0,0,0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(120, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setFamily("Poppins")
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#FFF;\n"
                                   "background-color:rgba(0,0,0,0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 90, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "background-color: rgba(0, 0, 0, 0);\n"
                                    "border:2px solid rgba(0, 0, 0, 0);\n"
                                    "border-bottom-color:#fff;\n"
                                    "color: #fff;\n"
                                    "padding-left:10px;\n"
                                    "padding-right:10px;\n"
                                    "border-radius: 0;\n"
                                    "}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 140, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "background-color: rgba(0, 0, 0, 0);\n"
                                      "border:2px solid rgba(0, 0, 0, 0);\n"
                                      "border-bottom-color:#fff;\n"
                                      "color: #fff;\n"
                                      "padding-left:10px;\n"
                                      "padding-right:10px;\n"
                                      "border-radius: 0;\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 200, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "background-color: rgba(0, 0, 0, 0);\n"
                                      "border:2px solid rgba(0, 0, 0, 0);\n"
                                      "border-bottom-color:#fff;\n"
                                      "color: #fff;\n"
                                      "padding-left:10px;\n"
                                      "padding-right:10px;\n"
                                      "border-radius: 0;\n"
                                      "}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setGeometry(QtCore.QRect(200, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton#saveButton {color:#FFF;\n"
                                      "    background-color: qlineargradient(spread:repeat, x1:0.584, y1:1, x2:0.6, y2:0, stop:0 rgba(15, 32, 39, 255), stop:0.505263 rgba(32, 58, 67, 255), stop:1 rgba(44, 83, 100, 255));\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton#saveButton:pressed{\n"
                                      "    padding-left:5px;\n"
                                      "    padding-top:5px;\n"
                                      "\n"
                                      "background-color: qlineargradient(spread:repeat, x1:0.831, y1:0, x2:0.826, y2:1, stop:0 rgba(15, 32, 39, 255), stop:0.505263 rgba(32, 58, 67, 255), stop:1 rgba(44, 83, 100, 255));\n"
                                      "    background-position:calc(100% - 10px)center;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(lambda : [self.save_button_clicked(new_data)])
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(380, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton#closeButton {color:#FFF;\n"
                                       "    background-color: qlineargradient(spread:repeat, x1:0.584, y1:1, x2:0.6, y2:0, stop:0 rgba(15, 32, 39, 255), stop:0.505263 rgba(32, 58, 67, 255), stop:1 rgba(44, 83, 100, 255));\n"
                                       "}\n"
                                       "QPushButton#closeButton:pressed{\n"
                                       "    padding-left:5px;\n"
                                       "    padding-top:5px;\n"
                                       "background-color: qlineargradient(spread:repeat, x1:0.831, y1:0, x2:0.826, y2:1, stop:0 rgba(15, 32, 39, 255), stop:0.505263 rgba(32, 58, 67, 255), stop:1 rgba(44, 83, 100, 255));\n"
                                       "\n"
                                       "    background-position:calc(100% - 10px)center;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda : [Form.close()])
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.error = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.error.setFont(font)
        self.error.setObjectName("error")
        self.error.setFixedWidth(711)
        self.error.setGeometry(QtCore.QRect(0, 240, 301, 70))
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setStyleSheet("color: gray;\nbackground-color: rgba(0, 0, 0, 0);")
        
        if new_data:    
            self.error.setStyleSheet("color: #0090e0;\nbackground-color: rgba(0, 0, 0, 0);")        
            self.error.setText("Tip: Click the reload button on dashboard (after saving here)\nto update the new entry.")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(13)
            self.error.setFont(font)
        
        else:
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(16)
            self.error.setFont(font)
            self.error.setGeometry(QtCore.QRect(0, 150, 301, 31))
            self.label_3.hide()
            self.label_7.hide()
            self.lineEdit_2.hide()
            self.lineEdit_3.hide()
            self.error.setStyleSheet("color: #0090e0;\nbackground-color: rgba(0, 0, 0, 0);")
            self.error.setText("Enter service name to be deleted.\n(This is case-sensitive input)\nTo modify data, first delete the old one,\nthen add the new credentials via the dashboard.")
            self.error.setMinimumHeight(130)
            self.error.adjustSize()
            self.label.setText("Delete Entries")
            self.saveButton.setText("CONFIRM")
    
    def save_button_clicked(self, new_data):
        empty_str = "".split(',')
        serv = self.lineEdit.text()
        usrname = self.lineEdit_2.text()
        pswd = self.lineEdit_3.text()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(16)
        self.error.setFont(font)
        
        if new_data:        

            if serv not in empty_str and usrname not in empty_str and pswd not in empty_str:
                data_main.new_entry_from_ui(self)
                self.error.setStyleSheet("color: #34c240;\nbackground-color: rgba(0, 0, 0, 0);")
                self.lineEdit.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("")
                self.error.setText("Saved successfully!")                 
            else:
                self.error.setStyleSheet("background: rgba(0, 0, 0, 0);\n""color: #d64242;")    
                self.error.setText("Empty data entered.")
        else: # That means user is trying to delete entries

            if os.path.isfile('data/credentials'):
                # Getting the data from the credentials file first
                if os.stat('data/credentials').st_size !=0:

                    with open("data/credentials") as f:
                        data = json.load(f)  
                                
                    # To check if atleast service is non-empty
                    if serv in empty_str:
                        self.error.setStyleSheet("color: #0090e0;\nbackground-color: rgba(0, 0, 0, 0);")
                        self.error.setText("Bro you need to enter service name atleast.")  
                    # If serv is not empty but pswd and usrname is empty
                    elif serv not in empty_str and pswd in empty_str and usrname in empty_str:
                        for credential in data:
                            if serv in credential["service"]:
                                data.remove(credential)
                                self.error.setStyleSheet("color: #34c240;\nbackground-color: rgba(0, 0, 0, 0);")
                                self.error.setText("Entry deleted successfully!") 
                                self.lineEdit.setText("")
                            else:
                                self.error.setStyleSheet("color: #fa9f47;\nbackground-color: rgba(0, 0, 0, 0);")
                                self.error.setText("This service does not exist yet.\nTo add it, close this dialog and add it via the dashboard.") 
                        with open("data/credentials", "w+") as file:
                            json.dump(data, file, indent=4)
                else:
                    self.error.setStyleSheet("color: #fa9f47;\nbackground-color: rgba(0, 0, 0, 0);")
                    self.error.setText("This service does not exist yet.\nTo add it, close this dialog and add it via the dashboard.")
            else:
                self.error.setStyleSheet("color: #fa9f47;\nbackground-color: rgba(0, 0, 0, 0);")
                self.error.setText("You have deleted the credentials file. Your data is lost forever. Close this dialog box and add all data again.")
            
                    
            

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Create a new entry"))
        self.label_2.setText(_translate("Form", "Service:"))
        self.label_3.setText(_translate("Form", "Username/Email:"))
        self.label_7.setText(_translate("Form", "Password:"))
        self.saveButton.setText(_translate("Form", "SAVE"))
        self.closeButton.setText(_translate("Form", "CLOSE"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form, False)
    Form.show()
    sys.exit(app.exec_())
