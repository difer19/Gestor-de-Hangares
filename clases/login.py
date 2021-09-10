from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QWidget
from PyQt5 import uic
from database.conexion import Conexion

class Usuario:
    def __init__(self, name, afiliacion, password):
        self.name = name
        self.afiliacion = afiliacion
        self.password = password
    
    def __str__(self):
        return str(self.name) + " " +str(self.password) + " " +str(self.afiliacion)

class Login(QWidget):
    def __init__(self):
        super().__init__()
    
    def iniciarGui(self, background):
        uic.loadUi(r'GUI\Resources\UI\Login_UI.ui', background)
        self.btn_login = background.findChild(QPushButton, 'login_Button')
        self.le_UserID = background.findChild(QLineEdit, 'id_User')
        self.le_Password = background.findChild(QLineEdit, 'pass')
        self.lb_alert = background.findChild(QLabel, 'label')
        background.show()
        
class PantallaLogin(QMainWindow):
    def __init__(self):
        self.status = False
        super().__init__()
        self.iniciarGui()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\PantallaInicial_UI.ui', self)
        self.w1 = self.findChild(QWidget, "form_widget")
        self.Login1 = Login()
        self.Login1.iniciarGui(self.w1)
        self.Login1.btn_login.clicked.connect(lambda: self.autentificacion())
        self.show()
     
    def autentificacion(self):
        userName = self.Login1.le_UserID.text()
        Password = self.Login1.le_Password.text()
        LoginC = Conexion()
        query = "SELECT password FROM users WHERE username = '%s' and password = '%s'" %(userName, Password)
        result = LoginC.numberResult(query)
        if result == 0:
            self.Login1.lb_alert.setText("Datos Invalidos")
            print("incorrecto")
        else:
            query2 = "SELECT afiliacion FROM users WHERE username = '%s' and password = '%s'" %(userName, Password)
            afiliacion = LoginC.ejecutar_SQL(query2)
            resultado = afiliacion.fetchall()
            for af in resultado:
                afiliacion = af
            self.User = Usuario(userName, afiliacion, Password)
            self.status = True
            print("correcto")
            self.close()
        LoginC.cerrar_conexion()

    def closeEvent(self, event):
        if self.status == False:
            self.destroy()
        return QMainWindow.closeEvent(self, event)


