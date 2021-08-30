from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys
from PyQt5.uic.uiparser import QtWidgets


class log:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        return str(self.x)+","+str(self.y)

class Login(QWidget):
    def __init__(self):
        super().__init__()
    
    def iniciarGui(self, background):
        uic.loadUi(r'GUI\Resources\UI\Login_UI.ui', background)
        self.btn_login = background.findChild(QPushButton, 'login_Button')
        background.show()
        
class PantallaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciarGui()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\PantallaInicial_UI.ui', self)
        self.w1 = self.findChild(QWidget, "form_widget")
        self.w2 = self.findChild(QWidget, "Logo_Widget")
        self.Login1 = Login()
        self.Login1.iniciarGui(self.w1)
        self.Login1.btn_login.clicked.connect(lambda: self.mi1())
        self.show()
    
    def mi1(self):
        self.close()

    def closeEvent(self, event):
        self.lg = log(1,2)
        return QMainWindow.closeEvent(self, event)


