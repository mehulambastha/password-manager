# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import platform, json
import data_main
import sys, webbrowser, os
from PyQt5 import QtCore, QtGui, QtWidgets
import newEntry
from newPassword import Ui_Form1
from datetime import date

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        dashboard.setObjectName("dashboard")
        dashboard.resize(989, 761)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/padlock_main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dashboard.setWindowIcon(icon)
        dashboard.setStyleSheet("background: none;")
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Lobster-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/BioRhyme-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Roboto-Medium.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Roboto-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Poppins-SemiBold.ttf.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/Poppins-Medium.ttf')
        QtGui.QFontDatabase.addApplicationFont(':/icons/resources/fonts/NotoSansJP-Medium.otf')
        self.frame = QtWidgets.QFrame(dashboard)
        self.frame.setGeometry(QtCore.QRect(10, 30, 881, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(240, 30, 631, 611))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.0631579 rgba(28, 181, 224, 255), stop:0.952632 rgba(0, 0, 70, 255));\n"
                                  "border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(51, 90, 307, 61))
        self.frame_2.setStyleSheet("background: none;")
        self.frame_2.setObjectName("frame_2")
        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(-6, 0, 251, 59))
        self.widget_3.setStyleSheet("background: none;")
        self.widget_3.setObjectName("widget_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(9, 10, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
        self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setToolTip("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background: none;\n"
                                    "padding-left: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.searchButton = QtWidgets.QPushButton(self.frame_2)
        self.searchButton.setGeometry(QtCore.QRect(230, 10, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
        self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setStyleSheet("background-color: rgb(45, 210, 0);")
        self.searchButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/magnifying-glass-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QtCore.QSize(25, 25))
        self.searchButton.setObjectName("searchButton")
        iconSearch = QtGui.QIcon()
        iconSearch.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/magnifying-glass-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(iconSearch)
        self.searchButton.clicked.connect(self.search_cred)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "text-decoration: underline;\n"
                                   "font: 10 bold 45pt \"Lobster\";\n"
                                   "background-color: none;\n"
                                   "border-radius: 5pt;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLabel(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 100, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:1, y2:1, stop:0.0473684 rgba(255, 88, 88, 255), stop:0.915789 rgba(240, 152, 25, 255));")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, 611, 461))
        self.tableWidget.setStyleSheet("background: rgba(0, 0 , 0, 0);\n"
"color: white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 198)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setRowCount(0)
        data_main.load(self, "")
        item = QtWidgets.QTableWidgetItem()
        item.setText("Service")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(27, 177, 221))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Username/Email")
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(83, 208, 243))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(26, 171, 215))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(True)
        item.setFont(font)
        item.setText("")
        item.setBackground(QtGui.QColor(26, 171, 215))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        # Disable table editing
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.reload = QtWidgets.QPushButton(self.widget)
        self.reload.setGeometry(QtCore.QRect(572, 100, 51, 41))
        self.reload.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.reload.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/resources/icons/reload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon12)
        self.reload.setIconSize(QtCore.QSize(50, 50))
        self.reload.setObjectName("reload")
        self.reload.clicked.connect(lambda : [data_main.load(self, "")])
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 251, 651))
        self.widget_2.setMaximumSize(QtCore.QSize(1000, 1200))
        self.widget_2.setMouseTracking(True)
        self.widget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.0466321 rgba(142, 45, 226, 255), stop:0.984456 rgba(74, 0, 224, 255));\n"
                                    "border-radius: 20px;")
        self.widget_2.setObjectName("widget_2")
        self.exitButton = QtWidgets.QPushButton(self.widget_2)
        self.exitButton.setGeometry(QtCore.QRect(20, 560, 211, 81))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(40)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(237, 8, 0);\n"
                                      "border-radius: 20px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon2)
        self.exitButton.setIconSize(QtCore.QSize(50, 50))
        self.exitButton.setObjectName("exitButton")
        self.createNew = QtWidgets.QPushButton(self.widget_2)
        self.createNew.setGeometry(QtCore.QRect(20, 320, 211, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.createNew.sizePolicy().hasHeightForWidth())
        self.createNew.setSizePolicy(sizePolicy)
        self.createNew.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.createNew.setFont(font)
        self.createNew.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.createNew.setStyleSheet("background-color: rgb(45, 210, 0);\n"
                                     "border-radius: 20px;\n"
                                     "QPushButton#createNew:pressed{\n"
                                     "    padding-left:5px;\n"
                                     "    padding-top:5px;\n"
                                     "    background: blue;\n"
                                     "}\n"
                                     "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createNew.setIcon(icon3)
        self.createNew.setIconSize(QtCore.QSize(45, 45))
        self.createNew.setFlat(False)
        self.createNew.setObjectName("createNew")
        self.createNew.clicked.connect(lambda : [self.newentry(True)])
        self.seeJson = QtWidgets.QPushButton(self.widget_2)
        self.seeJson.setGeometry(QtCore.QRect(20, 480, 209, 71))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.seeJson.sizePolicy().hasHeightForWidth())
        self.seeJson.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        self.seeJson.setFont(font)
        self.seeJson.setStyleSheet("background-color: rgb(45, 210, 0);\n"
                                   "border-radius: 20px")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.seeJson.setIcon(icon4)
        self.seeJson.setIconSize(QtCore.QSize(50, 50))
        self.seeJson.setObjectName("seeJson")
        self.seeJson.clicked.connect(self.open_json)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 191, 181))
        self.label_7.setStyleSheet("background: none;")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setLineWidth(24)
        self.label_7.setMidLineWidth(9)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/user(1).png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.masterPswd = QtWidgets.QPushButton(self.widget_2)
        self.masterPswd.setGeometry(QtCore.QRect(20, 240, 209, 71))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.masterPswd.sizePolicy().hasHeightForWidth())
        self.masterPswd.setSizePolicy(sizePolicy)
        self.masterPswd.setMaximumSize(QtCore.QSize(16777215, 76))
        self.masterPswd.setSizeIncrement(QtCore.QSize(0, 0))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            ":/icons/resources/icons/padlock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.masterPswd.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("NotoSansJP")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.masterPswd.setFont(font)
        self.masterPswd.setAutoFillBackground(False)
        self.masterPswd.setStyleSheet("border-radius: 20px;\n"
                                      "background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:1, y2:1, stop:0.0473684 rgba(255, 88, 88, 255), stop:0.915789 rgba(240, 152, 25, 255));")
        self.masterPswd.setIcon(icon)
        self.masterPswd.setIconSize(QtCore.QSize(50, 50))
        self.masterPswd.setObjectName("masterPswd")
        self.masterPswd.clicked.connect(self.newpass)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(42, 210, 171, 21))
        font = QtGui.QFont()
        font.setFamily("BioRhyme")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background: none;\n"
                                   "font: 85 18pt;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.delete = QtWidgets.QPushButton(self.widget_2)
        self.delete.setGeometry(QtCore.QRect(20, 400, 209, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete.sizePolicy().hasHeightForWidth())
        self.delete.setSizePolicy(sizePolicy)
        self.delete.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.delete.setFont(font)
        self.delete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.delete.setStyleSheet("background-color: rgb(45, 210, 0);\n"
"border-radius: 20px;\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/resources/icons/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete.setIcon(icon6)
        self.delete.setIconSize(QtCore.QSize(45, 45))
        self.delete.setFlat(False)
        self.delete.setObjectName("delete")
        self.delete.clicked.connect(lambda  : [self.newentry(False)])
        self.closeButton = QtWidgets.QToolButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(810, 0, 61, 51))
        self.closeButton.setToolTip("")
        self.closeButton.setStyleSheet("color: rgb(255, 0, 0);\n"
                                       "background-color: rgb(255, 0, 0);\n"
                                       "border-radius: 2px;")
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(30, 30))
        self.closeButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda : [self.close_completely(dashboard)])
        self.exitButton.clicked.connect(lambda : [self.close_completely(dashboard)])
        self.widget.raise_()
        self.closeButton.raise_()
        self.widget_2.raise_()
        dashboard.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        dashboard.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.retranslateUi(dashboard)
        QtCore.QMetaObject.connectSlotsByName(dashboard)

        # ===================================
        # Adding shadows
        self.masterPswd.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.closeButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.createNew.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.seeJson.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.exitButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.searchButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        self.widget_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=3, yOffset=0))
        # -----------------------------------

    def close_completely(self, dashboard):
        if os.path.isfile("./data/saved_passwords.json"):
            os.remove("./data/saved_passwords.json")
        dashboard.close()
    
    def search_cred(self):
        query = self.lineEdit.text().lower()
        data_main.load(self, query)

    # Handles the new credential entries from user
    def newentry(self, new_data):
        self.Form = QtWidgets.QWidget()
        self.ui = newEntry.Ui_Form()

        self.ui.setupUi(self.Form, new_data)
        # Build and show the new data window
        self.Form.show()

    # Changing or adding the new password
    def newpass(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.Form)
        self.Form.show()
        
    # To open the json file having encrypted data.
    def open_json(self):
        if os.path.isfile('data/credentials'):
            with open('data/credentials', "r") as file:
                # setting file pointer at the start so as to read everything completely
                file.seek(0)
                t = file.read()
                # Saving the already existing data
                data = json.loads(t)
            with open('data/saved_passwords.json', 'w+') as f:
                json.dump(data, f)
        else:
            with open('data/credentials') as f:
                pass

            # Empty data
            data = []
            with open('data/saved_passwords.json', 'w+') as f:
                json.dump(data, f)
                
        if platform.system() == 'Linux':
            os.system("xdg-open data/saved_passwords.json")
        elif platform.system() == 'Windows':
            os.system("notepad data/saved_passwords.json")
        else:
            webbrowser.open("data/saved_passwords.json")


    def retranslateUi(self, dashboard):
        _translate = QtCore.QCoreApplication.translate
        dashboard.setWindowTitle(_translate("dashboard", "Form"))
        self.lineEdit.setPlaceholderText(_translate("dashboard", "Search"))
        self.label_3.setText(_translate("dashboard", "All saved credentials"))
        today = date.today()
        day_formatted = today.strftime("%B %d, %Y")
        self.lineEdit_2.setText(_translate(
            "dashboard", "Today: {}".format(day_formatted)))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dashboard", "Password"))
        self.exitButton.setText(_translate("dashboard", " Exit"))
        self.createNew.setText(_translate("dashboard", " New entry"))
        self.seeJson.setText(_translate("dashboard", "  Your data"))
        self.masterPswd.setText(_translate("dashboard", " Change "
                                           "master\n password"))
        self.label_8.setText(_translate("dashboard", "WELCOME"))
        self.delete.setText(_translate("dashboard", "Delete entry"))
        self.closeButton.setText(_translate("dashboard", "..."))



import resources_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboard = QtWidgets.QWidget()
    ui = Ui_dashboard()
    ui.setupUi(dashboard)
    dashboard.show()
    sys.exit(app.exec_())
