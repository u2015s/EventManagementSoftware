# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EMS_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_S1_Designation(object):
    def setupUi(self, S1_Designation):
        S1_Designation.setObjectName("S1_Designation")
        S1_Designation.resize(1154, 743)
        self.centralwidget = QtWidgets.QWidget(S1_Designation)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 1151, 681))
        self.stackedWidget.setStyleSheet("background-color:rgb(128,128,128);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.designation = QtWidgets.QWidget()
        self.designation.setObjectName("designation")
        self.groupBox = QtWidgets.QGroupBox(self.designation)
        self.groupBox.setGeometry(QtCore.QRect(360, 100, 431, 461))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.comboBox_designation = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_designation.setGeometry(QtCore.QRect(20, 240, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_designation.setFont(font)
        self.comboBox_designation.setMouseTracking(False)
        self.comboBox_designation.setTabletTracking(False)
        self.comboBox_designation.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_designation.setAutoFillBackground(False)
        self.comboBox_designation.setEditable(True)
        self.comboBox_designation.setDuplicatesEnabled(False)
        self.comboBox_designation.setObjectName("comboBox_designation")
        self.comboBox_designation.addItem("")
        self.comboBox_designation.addItem("")
        self.comboBox_designation.addItem("")
        self.comboBox_designation.addItem("")
        self.comboBox_designation.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 160, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.designation)
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.groupBox_3 = QtWidgets.QGroupBox(self.login)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 90, 381, 421))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(70, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(92, 200, 211, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_input_username = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_input_username.setGeometry(QtCore.QRect(160, 60, 201, 31))
        self.comboBox_input_username.setEditable(True)
        self.comboBox_input_username.setObjectName("comboBox_input_username")
        self.comboBox_input_password = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_input_password.setGeometry(QtCore.QRect(160, 120, 201, 31))
        self.comboBox_input_password.setEditable(True)
        self.comboBox_input_password.setObjectName("comboBox_input_password")
        self.loginpage_backbutton = QtWidgets.QPushButton(self.groupBox_3)
        self.loginpage_backbutton.setGeometry(QtCore.QRect(10, 320, 93, 28))
        self.loginpage_backbutton.setObjectName("loginpage_backbutton")
        self.stackedWidget.addWidget(self.login)
        self.afterloginforADMIN = QtWidgets.QWidget()
        self.afterloginforADMIN.setObjectName("afterloginforADMIN")
        self.groupBox_4 = QtWidgets.QGroupBox(self.afterloginforADMIN)
        self.groupBox_4.setGeometry(QtCore.QRect(320, 110, 441, 391))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.admin_login_eventbutton = QtWidgets.QPushButton(self.groupBox_4)
        self.admin_login_eventbutton.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.admin_login_eventbutton.setObjectName("admin_login_eventbutton")
        self.admin_login_staffbutton = QtWidgets.QPushButton(self.groupBox_4)
        self.admin_login_staffbutton.setGeometry(QtCore.QRect(50, 90, 121, 31))
        self.admin_login_staffbutton.setObjectName("admin_login_staffbutton")
        self.admin_login_inventorybutton = QtWidgets.QPushButton(self.groupBox_4)
        self.admin_login_inventorybutton.setGeometry(QtCore.QRect(50, 140, 121, 31))
        self.admin_login_inventorybutton.setObjectName("admin_login_inventorybutton")
        self.admin_login_venuebutton = QtWidgets.QPushButton(self.groupBox_4)
        self.admin_login_venuebutton.setGeometry(QtCore.QRect(50, 210, 121, 31))
        self.admin_login_venuebutton.setObjectName("admin_login_venuebutton")
        self.admin_login_userbutton = QtWidgets.QPushButton(self.groupBox_4)
        self.admin_login_userbutton.setGeometry(QtCore.QRect(230, 30, 121, 31))
        self.admin_login_userbutton.setObjectName("admin_login_userbutton")
        self.admin_login_clientbutton = QtWidgets.QPushButton(self.groupBox_4)
        self.admin_login_clientbutton.setGeometry(QtCore.QRect(230, 90, 121, 31))
        self.admin_login_clientbutton.setObjectName("admin_login_clientbutton")
        self.label_6 = QtWidgets.QLabel(self.afterloginforADMIN)
        self.label_6.setGeometry(QtCore.QRect(370, 50, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.afterloginforADMIN)
        self.afterloginforSTAFF = QtWidgets.QWidget()
        self.afterloginforSTAFF.setObjectName("afterloginforSTAFF")
        self.label_7 = QtWidgets.QLabel(self.afterloginforSTAFF)
        self.label_7.setGeometry(QtCore.QRect(410, 110, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.afterloginforSTAFF)
        self.groupBox_5.setGeometry(QtCore.QRect(350, 150, 441, 391))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.staff_login_eventbutton = QtWidgets.QPushButton(self.groupBox_5)
        self.staff_login_eventbutton.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.staff_login_eventbutton.setObjectName("staff_login_eventbutton")
        self.staff_login_staffbutton = QtWidgets.QPushButton(self.groupBox_5)
        self.staff_login_staffbutton.setGeometry(QtCore.QRect(50, 90, 121, 31))
        self.staff_login_staffbutton.setObjectName("staff_login_staffbutton")
        self.stackedWidget.addWidget(self.afterloginforSTAFF)
        self.afterloginforINVENTORY = QtWidgets.QWidget()
        self.afterloginforINVENTORY.setObjectName("afterloginforINVENTORY")
        self.label_8 = QtWidgets.QLabel(self.afterloginforINVENTORY)
        self.label_8.setGeometry(QtCore.QRect(440, 110, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.afterloginforINVENTORY)
        self.groupBox_6.setGeometry(QtCore.QRect(390, 180, 441, 391))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.Inventory_login_eventbutton = QtWidgets.QPushButton(self.groupBox_6)
        self.Inventory_login_eventbutton.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.Inventory_login_eventbutton.setObjectName("Inventory_login_eventbutton")
        self.Inventory_login_inventorybutton = QtWidgets.QPushButton(self.groupBox_6)
        self.Inventory_login_inventorybutton.setGeometry(QtCore.QRect(50, 110, 121, 31))
        self.Inventory_login_inventorybutton.setObjectName("Inventory_login_inventorybutton")
        self.stackedWidget.addWidget(self.afterloginforINVENTORY)
        self.afterloginforRECEPTIONIST = QtWidgets.QWidget()
        self.afterloginforRECEPTIONIST.setObjectName("afterloginforRECEPTIONIST")
        self.label_9 = QtWidgets.QLabel(self.afterloginforRECEPTIONIST)
        self.label_9.setGeometry(QtCore.QRect(400, 140, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.afterloginforRECEPTIONIST)
        self.groupBox_7.setGeometry(QtCore.QRect(350, 190, 441, 391))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.R_login_eventbutton = QtWidgets.QPushButton(self.groupBox_7)
        self.R_login_eventbutton.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.R_login_eventbutton.setObjectName("R_login_eventbutton")
        self.R_login_clientbutton = QtWidgets.QPushButton(self.groupBox_7)
        self.R_login_clientbutton.setGeometry(QtCore.QRect(230, 30, 121, 31))
        self.R_login_clientbutton.setObjectName("R_login_clientbutton")
        self.stackedWidget.addWidget(self.afterloginforRECEPTIONIST)
        self.afterloginforEVENTMANAGER = QtWidgets.QWidget()
        self.afterloginforEVENTMANAGER.setObjectName("afterloginforEVENTMANAGER")
        self.label_10 = QtWidgets.QLabel(self.afterloginforEVENTMANAGER)
        self.label_10.setGeometry(QtCore.QRect(320, 160, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.groupBox_8 = QtWidgets.QGroupBox(self.afterloginforEVENTMANAGER)
        self.groupBox_8.setGeometry(QtCore.QRect(290, 200, 441, 391))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.EM_login_eventbutton = QtWidgets.QPushButton(self.groupBox_8)
        self.EM_login_eventbutton.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.EM_login_eventbutton.setObjectName("EM_login_eventbutton")
        self.EM_login_staffbutton = QtWidgets.QPushButton(self.groupBox_8)
        self.EM_login_staffbutton.setGeometry(QtCore.QRect(50, 90, 121, 31))
        self.EM_login_staffbutton.setObjectName("EM_login_staffbutton")
        self.EM_login_inventorybutton = QtWidgets.QPushButton(self.groupBox_8)
        self.EM_login_inventorybutton.setGeometry(QtCore.QRect(50, 140, 121, 31))
        self.EM_login_inventorybutton.setObjectName("EM_login_inventorybutton")
        self.EM_login_venuebutton = QtWidgets.QPushButton(self.groupBox_8)
        self.EM_login_venuebutton.setGeometry(QtCore.QRect(50, 210, 121, 31))
        self.EM_login_venuebutton.setObjectName("EM_login_venuebutton")
        self.stackedWidget.addWidget(self.afterloginforEVENTMANAGER)
        self.optionsfortable = QtWidgets.QWidget()
        self.optionsfortable.setObjectName("optionsfortable")
        self.groupBox_9 = QtWidgets.QGroupBox(self.optionsfortable)
        self.groupBox_9.setGeometry(QtCore.QRect(360, 120, 441, 391))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.user_login_table_viewbutton = QtWidgets.QPushButton(self.groupBox_9)
        self.user_login_table_viewbutton.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.user_login_table_viewbutton.setObjectName("user_login_table_viewbutton")
        self.user_login_table_deletebutton = QtWidgets.QPushButton(self.groupBox_9)
        self.user_login_table_deletebutton.setGeometry(QtCore.QRect(50, 90, 121, 31))
        self.user_login_table_deletebutton.setObjectName("user_login_table_deletebutton")
        self.user_login_table_updatebutton = QtWidgets.QPushButton(self.groupBox_9)
        self.user_login_table_updatebutton.setGeometry(QtCore.QRect(50, 140, 121, 31))
        self.user_login_table_updatebutton.setObjectName("user_login_table_updatebutton")
        self.user_login_table_addbutton = QtWidgets.QPushButton(self.groupBox_9)
        self.user_login_table_addbutton.setGeometry(QtCore.QRect(230, 30, 121, 31))
        self.user_login_table_addbutton.setObjectName("user_login_table_addbutton")
        self.user_login_table_printbutton = QtWidgets.QPushButton(self.groupBox_9)
        self.user_login_table_printbutton.setGeometry(QtCore.QRect(230, 90, 121, 31))
        self.user_login_table_printbutton.setObjectName("user_login_table_printbutton")
        self.label_11 = QtWidgets.QLabel(self.optionsfortable)
        self.label_11.setGeometry(QtCore.QRect(460, 50, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.optionsfortable)
        self.changepassword = QtWidgets.QWidget()
        self.changepassword.setObjectName("changepassword")
        self.stackedWidget.addWidget(self.changepassword)
        self.ADDformforEvent = QtWidgets.QWidget()
        self.ADDformforEvent.setObjectName("ADDformforEvent")
        self.label_12 = QtWidgets.QLabel(self.ADDformforEvent)
        self.label_12.setGeometry(QtCore.QRect(320, 160, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.ADDformforEvent)
        self.ADDformforStaff = QtWidgets.QWidget()
        self.ADDformforStaff.setObjectName("ADDformforStaff")
        self.label_13 = QtWidgets.QLabel(self.ADDformforStaff)
        self.label_13.setGeometry(QtCore.QRect(370, 190, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.ADDformforStaff)
        self.ADDformforInventory = QtWidgets.QWidget()
        self.ADDformforInventory.setObjectName("ADDformforInventory")
        self.label_16 = QtWidgets.QLabel(self.ADDformforInventory)
        self.label_16.setGeometry(QtCore.QRect(380, 240, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.ADDformforInventory)
        self.ADDformforClient = QtWidgets.QWidget()
        self.ADDformforClient.setObjectName("ADDformforClient")
        self.label_14 = QtWidgets.QLabel(self.ADDformforClient)
        self.label_14.setGeometry(QtCore.QRect(360, 250, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.ADDformforClient)
        self.ADDformforVenue = QtWidgets.QWidget()
        self.ADDformforVenue.setObjectName("ADDformforVenue")
        self.label_15 = QtWidgets.QLabel(self.ADDformforVenue)
        self.label_15.setGeometry(QtCore.QRect(290, 260, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.ADDformforVenue)
        self.CreateUserform = QtWidgets.QWidget()
        self.CreateUserform.setObjectName("CreateUserform")
        self.stackedWidget.addWidget(self.CreateUserform)
        self.PRINT = QtWidgets.QWidget()
        self.PRINT.setObjectName("PRINT")
        self.label_17 = QtWidgets.QLabel(self.PRINT)
        self.label_17.setGeometry(QtCore.QRect(400, 210, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.PRINT)
        self.DELETE = QtWidgets.QWidget()
        self.DELETE.setObjectName("DELETE")
        self.label_19 = QtWidgets.QLabel(self.DELETE)
        self.label_19.setGeometry(QtCore.QRect(360, 210, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.stackedWidget.addWidget(self.DELETE)
        self.UPDATE = QtWidgets.QWidget()
        self.UPDATE.setObjectName("UPDATE")
        self.label_20 = QtWidgets.QLabel(self.UPDATE)
        self.label_20.setGeometry(QtCore.QRect(380, 220, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.UPDATE)
        self.VIEW = QtWidgets.QWidget()
        self.VIEW.setObjectName("VIEW")
        self.label_18 = QtWidgets.QLabel(self.VIEW)
        self.label_18.setGeometry(QtCore.QRect(390, 210, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.VIEW)
        self.VIEW_for_EM = QtWidgets.QWidget()
        self.VIEW_for_EM.setObjectName("VIEW_for_EM")
        self.groupBox_2 = QtWidgets.QGroupBox(self.VIEW_for_EM)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 70, 581, 401))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.EM_login_table_printbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.EM_login_table_printbutton.setGeometry(QtCore.QRect(450, 30, 93, 28))
        self.EM_login_table_printbutton.setObjectName("EM_login_table_printbutton")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setGeometry(QtCore.QRect(30, 60, 521, 301))
        self.tableView.setObjectName("tableView")
        self.label_21 = QtWidgets.QLabel(self.VIEW_for_EM)
        self.label_21.setGeometry(QtCore.QRect(360, 20, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.stackedWidget.addWidget(self.VIEW_for_EM)
        S1_Designation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(S1_Designation)
        self.statusbar.setObjectName("statusbar")
        S1_Designation.setStatusBar(self.statusbar)

        self.retranslateUi(S1_Designation)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(S1_Designation)

    def retranslateUi(self, S1_Designation):
        _translate = QtCore.QCoreApplication.translate
        S1_Designation.setWindowTitle(_translate("S1_Designation", "S1_Designation"))
        self.pushButton_ok.setText(_translate("S1_Designation", "ok"))
        self.comboBox_designation.setCurrentText(_translate("S1_Designation", "select user type"))
        self.comboBox_designation.setItemText(0, _translate("S1_Designation", "Admin"))
        self.comboBox_designation.setItemText(1, _translate("S1_Designation", "Receptionist"))
        self.comboBox_designation.setItemText(2, _translate("S1_Designation", "Event Manager"))
        self.comboBox_designation.setItemText(3, _translate("S1_Designation", "Staff Manager"))
        self.comboBox_designation.setItemText(4, _translate("S1_Designation", "Inventory Manager"))
        self.label.setText(_translate("S1_Designation", "Select the Designation"))
        self.label_3.setText(_translate("S1_Designation", "User Id:"))
        self.label_4.setText(_translate("S1_Designation", "Enter Sign-In Details :"))
        self.label_5.setText(_translate("S1_Designation", "Password:"))
        self.pushButton_7.setText(_translate("S1_Designation", "LOGIN"))
        self.comboBox_input_username.setCurrentText(_translate("S1_Designation", "Enter User Id"))
        self.comboBox_input_password.setCurrentText(_translate("S1_Designation", "Enter Password"))
        self.loginpage_backbutton.setText(_translate("S1_Designation", "BACK"))
        self.admin_login_eventbutton.setText(_translate("S1_Designation", "event table"))
        self.admin_login_staffbutton.setText(_translate("S1_Designation", "staff table"))
        self.admin_login_inventorybutton.setText(_translate("S1_Designation", "inventory table"))
        self.admin_login_venuebutton.setText(_translate("S1_Designation", "venue table"))
        self.admin_login_userbutton.setText(_translate("S1_Designation", "user table"))
        self.admin_login_clientbutton.setText(_translate("S1_Designation", "client table"))
        self.label_6.setText(_translate("S1_Designation", "this is after login  page for admin"))
        self.label_7.setText(_translate("S1_Designation", "this is after login  page for staff"))
        self.staff_login_eventbutton.setText(_translate("S1_Designation", "event table"))
        self.staff_login_staffbutton.setText(_translate("S1_Designation", "staff table"))
        self.label_8.setText(_translate("S1_Designation", "this is after login  page for inventory"))
        self.Inventory_login_eventbutton.setText(_translate("S1_Designation", "event table"))
        self.Inventory_login_inventorybutton.setText(_translate("S1_Designation", "inventory table"))
        self.label_9.setText(_translate("S1_Designation", "this is after login  page for receptionist"))
        self.R_login_eventbutton.setText(_translate("S1_Designation", "event table"))
        self.R_login_clientbutton.setText(_translate("S1_Designation", "client table"))
        self.label_10.setText(_translate("S1_Designation", "this is after login  page for event manager"))
        self.EM_login_eventbutton.setText(_translate("S1_Designation", "event table"))
        self.EM_login_staffbutton.setText(_translate("S1_Designation", "staff table"))
        self.EM_login_inventorybutton.setText(_translate("S1_Designation", "inventory table"))
        self.EM_login_venuebutton.setText(_translate("S1_Designation", "venue table"))
        self.user_login_table_viewbutton.setText(_translate("S1_Designation", "VIEW"))
        self.user_login_table_deletebutton.setText(_translate("S1_Designation", "DELETE"))
        self.user_login_table_updatebutton.setText(_translate("S1_Designation", "UPDATE"))
        self.user_login_table_addbutton.setText(_translate("S1_Designation", "ADD"))
        self.user_login_table_printbutton.setText(_translate("S1_Designation", "PRINT"))
        self.label_11.setText(_translate("S1_Designation", "  this is options page\n"
"(not for event manager) "))
        self.label_12.setText(_translate("S1_Designation", "this is ADD form page for event table"))
        self.label_13.setText(_translate("S1_Designation", "this is ADD form page for staff table"))
        self.label_16.setText(_translate("S1_Designation", "this is ADD form page for inventory table"))
        self.label_14.setText(_translate("S1_Designation", "this is ADD form page for client table"))
        self.label_15.setText(_translate("S1_Designation", "this is ADD form page for venue table"))
        self.label_17.setText(_translate("S1_Designation", "this is PRINT page"))
        self.label_19.setText(_translate("S1_Designation", "this is DELETE page"))
        self.label_20.setText(_translate("S1_Designation", "this is UPDATE page"))
        self.label_18.setText(_translate("S1_Designation", "this is VIEW page"))
        self.EM_login_table_printbutton.setText(_translate("S1_Designation", "PRINT"))
        self.label_21.setText(_translate("S1_Designation", "this is VIEW page for EM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    S1_Designation = QtWidgets.QMainWindow()
    ui = Ui_S1_Designation()
    ui.setupUi(S1_Designation)
    S1_Designation.show()
    sys.exit(app.exec_())

