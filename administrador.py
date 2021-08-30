from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
import sys
from reservas import Reservas
from aerolineas import Aerolineas
from hangares import Hangares
from usuarios import Usuarios

class PantallaAdministrador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciarGui()
        
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Pantalla_administradorHangares.ui', self)
        self.central = self.findChild(QWidget, 'centralwidget')
        self.menu = self.central.findChild(QWidget, 'widget')
        self.main = self.central.findChild(QStackedWidget, 'stackedWidget_2')
        self.btn_home = self.menu.findChild(QPushButton, 'home')
        self.btn_reservas = self.menu.findChild(QPushButton, 'reservas')
        self.btn_aerolineas = self.menu.findChild(QPushButton, 'aerolineas')
        self.btn_hangares = self.menu.findChild(QPushButton, 'hangares')
        self.btn_usuarios = self.menu.findChild(QPushButton, 'usuarios')

        self.ReservasW = Reservas()
        self.AerolineasW = Aerolineas()
        self.HangaresW = Hangares()
        self.UsuariosW = Usuarios()

        self.main.addWidget(QWidget())
        self.main.addWidget(self.ReservasW)
        self.main.addWidget(self.AerolineasW)
        self.main.addWidget(self.HangaresW)
        self.main.addWidget(self.UsuariosW)

        self.btn_home.clicked.connect(self.homea)
        self.btn_reservas.clicked.connect(self.reservasa)
        self.btn_aerolineas.clicked.connect(self.aerolineasa)
        self.btn_hangares.clicked.connect(self.hangaresa)
        self.btn_usuarios.clicked.connect(self.usuariosa)
        self.show()
    
    def homea(self):
        self.btn_home.setEnabled(False)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(True)
        self.btn_usuarios.setEnabled(True)
        self.main.setCurrentIndex(0)

    def reservasa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(False)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(True)
        self.btn_usuarios.setEnabled(True)
        self.main.setCurrentIndex(1)
    
    def aerolineasa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(False)
        self.btn_hangares.setEnabled(True)
        self.btn_usuarios.setEnabled(True)
        self.main.setCurrentIndex(2)
    
    def hangaresa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(False)
        self.btn_usuarios.setEnabled(True)
        self.main.setCurrentIndex(3)

    def usuariosa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(True)
        self.btn_usuarios.setEnabled(False)
        self.main.setCurrentIndex(4)