from login import PantallaLogin
from administrador import PantallaAdministrador
from PyQt5.QtWidgets import QApplication
import sys


class Launcher:
    def __init__(self):
        pass
    
    def iniciarLogin(self):
        app = QApplication(sys.argv)
        self.Login = PantallaLogin()
        app.exec_()
        return self.Login.lg

    def iniciarAdministrador(self):
        app = QApplication(sys.argv)
        self.Administrador = PantallaAdministrador()
        app.exec_()
    

    
