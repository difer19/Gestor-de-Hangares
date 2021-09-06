from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QWidget
from PyQt5 import uic


class UserRegister(QWidget):
    def __init__(self, parent = None):
        super(UserRegister, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\UserRegister.ui', self)
        self.le_username = self.findChild(QLineEdit, 'lineEdit_4')
        self.le_name = self.findChild(QLineEdit, 'lineEdit')
        self.cb_afiliacion = self.findChild(QComboBox, 'comboBox')
        self.le_password = self.findChild(QLineEdit, 'lineEdit_2')
        self.btn_password = self.findChild(QPushButton, 'pushButton')
        self.btn_password.clicked.connect(lambda: self.RegistrarUser())
    
    def cargarCB(self):
        pass

    def RegistrarUser(self):
        pass
