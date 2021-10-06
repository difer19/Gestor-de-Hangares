from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget 
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *


class Home(QWidget):
    def __init__(self, username, parent = None):
        super(Home, self).__init__(parent)
        self.username = username
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Home.ui', self)
        self.le_username = self.findChild(QLineEdit, 'lineEdit')
        self.le_name = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_afiliacion = self.findChild(QLineEdit, 'lineEdit_3')
        self.le_passw = self.findChild(QLineEdit, 'lineEdit_4')
        self.btn_mod = self.findChild(QPushButton, 'pushButton_3')
        self.btn_save = self.findChild(QPushButton, 'pushButton_2')

        self.chargeData()

        self.le_username.setEnabled(False)
        self.le_name.setEnabled(False)
        self.le_afiliacion.setEnabled(False)
        self.le_passw.setEnabled(False)

        self.btn_mod.clicked.connect(lambda: self.userMod())
        self.btn_save.clicked.connect(lambda: self.userSave())
    
    def chargeData(self):
        userCon = Conexion()
        datos = userCon.ejecutar_SQL("SELECT * FROM users WHERE username = '%s'" %(self.username)) 
        datos = datos.fetchall()
        self.le_username.setText(datos[0][1])
        self.le_name.setText(datos[0][4])
        self.le_afiliacion.setText(datos[0][3])
        self.le_passw.setText(datos[0][2])
        userCon.cerrar_conexion()

    def userMod(self):
        if self.le_username.isEnabled() == False:
            self.le_username.setEnabled(True)
            self.le_name.setEnabled(True)
            self.le_passw.setEnabled(True)
            self.btn_mod.setText("Cancelar Modificacion")
        else:
            self.le_username.setEnabled(False)
            self.le_name.setEnabled(False)
            self.le_passw.setEnabled(False)
            self.btn_mod.setText("Modificar Datos")
            self.chargeData()

    
    def userSave(self):
        if self.validacion() == False:
            Dialog(" Campos Vacios ")
            return False
        userCon = Conexion()
        if self.username != self.le_username.text().strip():
            number = userCon.numberResult("SELECT username FROM users WHERE username = '%s'" %(self.le_username.text()))
            if number != 0 :
                Dialog("El username no esta disponible")
                return False
        query = """
                    UPDATE users SET username = '%s', nombre = '%s', password = '%s'
                    WHERE username = '%s'
                """%(self.le_username.text(), self.le_name.text(), self.le_passw.text(), self.username)
        userCon.insertarDatos(query)
        userCon.cerrar_conexion()
        Dialog2("Modificacion Exitosa")
        self.userMod()


    def validacion(self):
        count = 0
        if not self.le_username.text().strip():
            count += 1
        if not self.le_name.text().strip():
            count += 1
        if not self.le_afiliacion.text().strip():
            count += 1
        if not self.le_passw.text().strip():
            count += 1
        if count == 0:
            return True
        return False

