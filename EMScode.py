from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
#import MySQLdb
from PyQt5.uic import loadUiType
import datetime
from xlrd import *
from xlsxwriter import *

ui,_ = loadUiType('ems.ui')

def start():
    global m
    m = MainApp()
    m.show()

ch1='X'
ch='X'

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        if ((self.stackedWidget.currentIndex() == 0) or (self.stackedWidget.currentIndex() == 1)):
            self.signout_button.setVisible(False)
            self.changepass_button.setVisible(False)

        self.Handel_Buttons()
    

    def Handel_Buttons(self):
        self.pushButton_7.clicked.connect(self.f9)    
        self.pushButton_ok.clicked.connect(self.f8)
#--------------------------------------------------------------------------------------------------------------------------
#below are pushbuttons under afterlogin screens(i.e.,chosing tables by different users)  
        self.admin_login_eventbutton.clicked.connect(self.f10)
        self.admin_login_userbutton.clicked.connect(self.f11)
        self.admin_login_staffbutton.clicked.connect(self.f12)
        self.admin_login_inventorybutton.clicked.connect(self.f13)
        self.admin_login_venuebutton.clicked.connect(self.f14)
        self.admin_login_clientbutton.clicked.connect(self.f15)

        self.staff_login_eventbutton.clicked.connect(self.f16)
        self.staff_login_staffbutton.clicked.connect(self.f17)

        self.Inventory_login_eventbutton.clicked.connect(self.f18)
        self.Inventory_login_inventorybutton.clicked.connect(self.f19)
        
        self.R_login_eventbutton.clicked.connect(self.f20)
        self.R_login_clientbutton.clicked.connect(self.f21)

        self.EM_login_eventbutton.clicked.connect(self.f22)
        self.EM_login_staffbutton.clicked.connect(self.f23)
        self.EM_login_inventorybutton.clicked.connect(self.f24)
        self.EM_login_venuebutton.clicked.connect(self.f25)
#--------------------------------------------------------------------------------------------------------------------------
#below are pushbuttons under options screen for tables(except user table)
        self.user_login_table_viewbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(24))
        self.user_login_table_deletebutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(17))
        self.user_login_table_printbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(16))
        self.user_login_table_updatebutton.clicked.connect(self.f6)
        self.user_login_table_addbutton.clicked.connect(self.f7)
#--------------------------------------------------------------------------------------------------------------------------
#below are pushbuttons under option screen for USER table
        self.admin_login_table_viewbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(24))
        self.admin_login_table_createuserbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(15))
        self.admin_login_table_removeuserbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(17))
        self.admin_login_table_changeUserPassbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(23))
#--------------------------------------------------------------------------------------------------------------------------
#print button on EM-view page
        self.EM_login_table_printbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(16))
#--------------------------------------------------------------------------------------------------------------------------
#all page's back buttons below
        self.loginpage_backbutton.clicked.connect(self.f26)

        self.user_login_table_backbutton.clicked.connect(self.f1)

        self.admin_login_table_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(2))

        self.event_addform_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.staff_addform_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.inventory_addform_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.client_addform_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.venue_addform_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.user_addform_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(8))

        self.print_backbutton.clicked.connect(self.f2)

        self.delete_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))

        self.update_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.updateStaff_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.updateInventory_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.updateClient_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.updateVenue_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))

        self.changeUserPass_backbutton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(8))
        
        self.view_backbutton.clicked.connect(self.f3)

        self.EM_viewpage_backbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
#----------------------------------------------------------------------------------------------------------------------------
#common buttons
        self.signout_button.clicked.connect(self.f4)
   
        self.changepass_button.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(9))

        self.changepass_okbutton.clicked.connect(self.f5)
# ----------------------------------------------------------------------------------------------------------------------------
# all definitions
    def f9(self):
        username = self.comboBox_input_username.currentText()
        password = self.comboBox_input_password.currentText()

        if(username ==  "admin" and password == "admin"):
            global ch1
            ch1 = 'A'
            QMessageBox.information(self,"Login Status", "you are logged in successfully")
            self.stackedWidget.setCurrentIndex(2)

        elif(username ==  "receptionist" and password == "receptionist"):
            ch1='R'
            QMessageBox.information(self,"Login Status", "you are logged in successfully")
            self.stackedWidget.setCurrentIndex(5)
        elif(username ==  "staff" and password == "staff"):
            ch1='S'
            QMessageBox.information(self,"Login Status", "you are logged in successfully")
            self.stackedWidget.setCurrentIndex(3)
        elif(username ==  "eventmanager" and password == "eventmanager"):
            ch1='E'
            QMessageBox.information(self,"Login Status", "you are logged in successfully")
            self.stackedWidget.setCurrentIndex(6)
        elif(username ==  "inventory" and password == "inventory"):
            ch1='I'
            QMessageBox.information(self,"Login Status", "you are logged in successfully")
            self.stackedWidget.setCurrentIndex(4)
        else:
            QMessageBox.warning(self,"Login Status", "Either Username or password is not valid")
        
        self.comboBox_input_username.clearEditText()
        self.comboBox_input_password.clearEditText()
        self.comboBox_input_username.clear()
        self.comboBox_input_password.clear()
        if( (self.stackedWidget.currentIndex() is not 0) and (self.stackedWidget.currentIndex() is not 1) ):
            self.signout_button.setVisible(True)
            self.changepass_button.setVisible(True)

    def f8(self):
        if(self.comboBox_designation.currentText()=="Admin"):
            self.comboBox_input_username.addItem("admin")
            self.comboBox_input_username.addItem("admin1")
            self.comboBox_input_username.addItem("admin2")
            self.stackedWidget.setCurrentIndex(1)
    
        elif(self.comboBox_designation.currentText()=="Receptionist"):
            self.comboBox_input_username.addItem("receptionist")
            self.stackedWidget.setCurrentIndex(1)
    
        elif(self.comboBox_designation.currentText()=="Staff Manager"):
            self.comboBox_input_username.addItem("staff")
            self.stackedWidget.setCurrentIndex(1)
    
        elif(self.comboBox_designation.currentText()=="Event Manager"):
            self.comboBox_input_username.addItem("eventmanager")
            self.stackedWidget.setCurrentIndex(1)
    
        elif(self.comboBox_designation.currentText()=="Inventory Manager"):
            self.comboBox_input_username.addItem("inventory")
            self.stackedWidget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self,"User Type Selection", "choose any one designation")

    def f6(self):
        if(ch=='E'): self.stackedWidget.setCurrentIndex(18)
        elif(ch=='I'): self.stackedWidget.setCurrentIndex(20)
        elif(ch=='S'): self.stackedWidget.setCurrentIndex(19)
        elif(ch=='V'): self.stackedWidget.setCurrentIndex(21)
        elif(ch=='C'): self.stackedWidget.setCurrentIndex(22)
        else:
          QMessageBox.warning(self,"ERROR", "No table is choosed before in afterlogin(tables) screen, which cann't be happen")

    def f7(self):
        if(ch=='E'):
            self.stackedWidget.setCurrentIndex(10)
        elif(ch=='I'):
            self.stackedWidget.setCurrentIndex(12)
        elif(ch=='S'):
            self.stackedWidget.setCurrentIndex(11)
        elif(ch=='V'):
            self.stackedWidget.setCurrentIndex(14)
        elif(ch=='C'):
            self.stackedWidget.setCurrentIndex(13)
        elif(ch=='U'):
            self.stackedWidget.setCurrentIndex(15)
        else:
            QMessageBox.warning(self,"ERROR", "No table is choosed before in afterlogin(tables) screen, which cann't be happen")

    def f1(self):
        if(ch1 =='A'):
            self.stackedWidget.setCurrentIndex(2)
        elif(ch1 =='R'):
            self.stackedWidget.setCurrentIndex(5)
        elif(ch1=='S'):
            self.stackedWidget.setCurrentIndex(3)
        elif(ch1=='E'):
            self.stackedWidget.setCurrentIndex(6)
        elif(ch1=='I'):
            self.stackedWidget.setCurrentIndex(4)
        else:
            QMessageBox.warning(self,"ERROR", "No User is choosed before (in designation screen), which can't be happen")

    def f2(self):
        if(ch=='U'):
            self.stackedWidget.setCurrentIndex(8)
        else:
            self.stackedWidget.setCurrentIndex(7)
 
    def f3(self):
        if(ch=='U'):
            self.stackedWidget.setCurrentIndex(8)
        else:
            self.stackedWidget.setCurrentIndex(7)


    def f4(self):
        self.stackedWidget.setCurrentIndex(0)
        self.signout_button.setVisible(False)
        self.changepass_button.setVisible(False)

    def f5(self):
        self.stackedWidget.setCurrentIndex(0)
        self.signout_button.setVisible(False)
        self.changepass_button.setVisible(False)
    def f10(self):
        global ch
        ch='E'
        self.stackedWidget.setCurrentIndex(7)
    def f11(self):
        global ch
        ch = 'U'
        self.stackedWidget.setCurrentIndex(8)
    def f12(self):
        global ch
        ch='S'
        self.stackedWidget.setCurrentIndex(7)
    def f13(self):
        global ch
        ch = 'I'
        self.stackedWidget.setCurrentIndex(7)
    def f14(self):
        global ch
        ch = 'V'
        self.stackedWidget.setCurrentIndex(7)
    def f15(self):
        global ch
        ch = 'C'
        self.stackedWidget.setCurrentIndex(7)
    def f16(self):
        global ch
        ch = 'E'
        self.stackedWidget.setCurrentIndex(7)
    def f17(self):
        global ch
        ch = 'S'
        self.stackedWidget.setCurrentIndex(7)
    def f18(self):
        global ch
        ch = 'E'
        self.stackedWidget.setCurrentIndex(7)
    def f19(self):
        global ch
        ch = 'I'
        self.stackedWidget.setCurrentIndex(7)
    def f20(self):
        global ch
        ch = 'E'
        self.stackedWidget.setCurrentIndex(7)
    def f21(self):
        global ch
        ch = 'C'
        self.stackedWidget.setCurrentIndex(7)
    def f22(self):
        global ch
        ch = 'E'
        self.stackedWidget.setCurrentIndex(25)
    def f23(self):
        global ch
        ch = 'S'
        self.stackedWidget.setCurrentIndex(25)
    def f24(self):
        global ch
        ch = 'I'
        self.stackedWidget.setCurrentIndex(25)
    def f25(self):
        global ch
        ch = 'V'
        self.stackedWidget.setCurrentIndex(25)
    def f26(self):
        self.comboBox_input_username.clearEditText()
        self.comboBox_input_password.clearEditText()
        self.comboBox_input_username.clear()
        self.comboBox_input_password.clear()
        self.stackedWidget.setCurrentIndex(0)
#----------------------------------------------------------------------------------------------------------------------------
# def main():
#    app = QApplication(sys.argv)
#    window = start()
#    app.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = start()
    app.exec_()