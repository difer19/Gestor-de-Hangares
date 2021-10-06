from clases.dialog import Dialog, Dialog2
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion 


class UserRegister(QWidget):
    def __init__(self, parent = None):
        super(UserRegister, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        self.update()
        uic.loadUi(r'GUI\Resources\UI\UserRegister.ui', self)
        self.le_username = self.findChild(QLineEdit, 'lineEdit_4')
        self.le_name = self.findChild(QLineEdit, 'lineEdit')
        self.cb_afiliacion = self.findChild(QComboBox, 'comboBox')
        self.le_password = self.findChild(QLineEdit, 'lineEdit_2')
        self.btn_password = self.findChild(QPushButton, 'pushButton')
        self.le_password2 = self.findChild(QLineEdit, 'lineEdit_3')
        self.tb_users = self.findChild(QTableWidget, 'tableWidget')
        self.btn_delUser = self.findChild(QPushButton, 'pushButton_2')

        self.cargarCB()
        self.cargarTable()

        self.btn_password.clicked.connect(lambda: self.RegistrarUser())
        self.btn_delUser.clicked.connect(lambda: self.DeleteUser())
        
    
    def cargarTable(self):
        users = Conexion()
        usuarios = users.ejecutar_SQL("SELECT idusers, username, nombre, afiliacion FROM users")
        userNumber = users.numberResult("SELECT idusers, username, nombre, afiliacion FROM users")
        self.tb_users.setRowCount(userNumber)
        i = 0
        for user in usuarios:
            self.tb_users.setItem(i, 0, QTableWidgetItem(str(user[0])))
            self.tb_users.setItem(i, 1, QTableWidgetItem(user[1]))
            self.tb_users.setItem(i, 2, QTableWidgetItem(user[2]))
            self.tb_users.setItem(i, 3, QTableWidgetItem(user[3]))
            i += 1
        users.cerrar_conexion()


    def cargarCB(self):
        self.cb_afiliacion.addItem("aeropuerto el campanero")
        aerolineas = Conexion()
        cursor = aerolineas.ejecutar_SQL("SELECT NombreAerolinea FROM Aerolineas")
        for Aerolinea in cursor.fetchall():
            self.cb_afiliacion.addItem(Aerolinea[0])
        aerolineas.cerrar_conexion()

    def RegistrarUser(self):
        if self.validarCamposVacios() == False:
            Dialog("Campos Vacios")
            return False
        self.cargarCB()
        userName = self.le_username.text()
        name = self.le_name.text().lower()
        afiliacion = self.cb_afiliacion.currentText()
        self.passw = self.le_password.text()
        self.passw2 = self.le_password2.text()
        Conect = Conexion()
        query = "SELECT username FROM users WHERE username = '%s'" %(userName)
        result = Conect.numberResult(query)
        if result == 0 and self.passw == self.passw2:
            idUser = Conect.ejecutar_SQL("select max(idusers) FROM users").fetchall()[0][0] + 1
            register = "INSERT INTO users (idusers, username, password, afiliacion, nombre) VALUES ('%s','%s','%s','%s','%s')" %(idUser, userName, self.passw, afiliacion, name )
            Conect.insertarDatos(register)
            self.le_username.clear()
            self.le_name.clear()
            self.le_password.clear()
            self.le_password2.clear()
            Dialog2("El usuario fue registrado")
        else:
            Dialog("campos no coinciden \n o el nombre de usuario \n ya esta en uso")
        Conect.cerrar_conexion()
        self.cargarTable()

    def DeleteUser(self):
        if self.tb_users.selectedIndexes() == []:
            return False
        idDel = self.tb_users.selectedIndexes()[0].data()
        delU = Conexion()
        delU.insertarDatos("DELETE FROM users WHERE idusers = '%s'" %(idDel))
        self.cargarTable()
        delU.cerrar_conexion()
        Dialog2("El usuario fue eliminado")
    
    def validarCamposVacios(self):
        count = 0
        if not self.le_username.text().strip():
            count += 1
        if not self.le_name.text().strip():
            count += 1
        if not self.le_password.text().strip():
            count += 1
        if not self.le_password2.text().strip():
            count += 1
        if count == 0:
            return True
        return False

