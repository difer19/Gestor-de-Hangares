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
        self.le_password2 = self.findChild(QLineEdit, 'lineEdit_3')
        self.cargarCB()

        self.btn_password.clicked.connect(lambda: self.RegistrarUser())
    
    def cargarCB(self):
        self.cb_afiliacion.addItem("aeropuerto el campanero")
        aerolineas = Conexion()
        cursor = aerolineas.ejecutar_SQL("SELECT NombreAerolinea FROM Aerolineas")
        for Aerolinea in cursor.fetchall():
            self.cb_afiliacion.addItem(Aerolinea[0])
        aerolineas.cerrar_conexion()

    def RegistrarUser(self):
        userName = self.le_username.text()
        name = self.le_name.text().lower()
        afiliacion = self.cb_afiliacion.currentText()
        self.passw = self.le_password.text()
        self.passw2 = self.le_password2.text()
        Conect = Conexion()
        query = "SELECT username FROM users WHERE username = '%s'" %(userName)
        result = Conect.numberResult(query)
        if result == 0 and self.passw == self.passw2:
            idUser = Conect.numberResult("SELECT * FROM users") + 1
            register = "INSERT INTO users (idusers, username, password, afiliacion, nombre) VALUES ('%s','%s','%s','%s','%s')" %(idUser, userName, self.passw, afiliacion, name )
            Conect.insertarDatos(register)
            self.le_username.clear()
            self.le_name.clear()
            self.le_password.clear()
            self.le_password2.clear()
        else:
            print("campos no coinciden o nombre de usuario ya esta en uso")
        Conect.cerrar_conexion()

    def RegistroUserDB(self):
        pass