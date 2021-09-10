from clases.login import PantallaLogin
from clases.administrador import PantallaAdministrador
from clases.funAerolinea import FunAerolinea
from PyQt5.QtWidgets import QApplication
import sys


class Launcher:
    def __init__(self):
        pass
    
    def iniciarLogin(self):
        app = QApplication(sys.argv)
        self.Login = PantallaLogin()
        app.exec_()
        return self.Login.User

    def iniciarAdministrador(self):
        app = QApplication(sys.argv)
        self.Administrador = PantallaAdministrador()
        app.exec_()

    def iniciarFunAerolinea(self, aerolinea):
        app = QApplication(sys.argv)
        self.funAero = FunAerolinea(aerolinea)
        app.exec_()

            