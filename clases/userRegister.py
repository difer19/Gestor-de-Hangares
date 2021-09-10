from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QWidget
from PyQt5 import uic
from database.conexion import Conexion 


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
        self.le_password2 = self.findChild(QPushButton, 'lineEdit_3')
        self.cargarCB()

        self.btn_password.clicked.connect(lambda: self.RegistrarUser())
    
    def cargarCB(self):
        pass

    def RegistrarUser(self):
        self.userName = self.le_username.text()
        self.name = self.le_name.text()
        self.cb_afiliacion.currentText()
        self.passw = self.le_password.text()
        self.passw2 = self.le_password2.text()
        Conect = Conexion()
        query = "SELECT username FROM users WHERE username = '%s'" %(self.userName)
        result = Conect.numberResult(query)
        if result == 0 and self.passw == self.passw2:
            # register = "INSERT INTO users (idusers, username, password, afiliacion, nombre) VALUES('%s','%s,'%s,'%s,'%s')"
            # registro
            pass
        else:
            print("campos no coinciden o nombre de usuario ya esta en uso")
        pass

    def RegistroUserDB(self):
        pass