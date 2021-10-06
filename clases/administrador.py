from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
from clases.aerolineas import Aerolineas
from clases.hangares import Hangares
from clases.home import Home
from clases.usuarios import Usuarios
from clases.reservarh2 import ReservarHangar2


class PantallaAdministrador(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
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

        self.homeP = Home(self.username)
        self.ReservasW = ReservarHangar2()
        self.AerolineasW = Aerolineas()
        self.HangaresW = Hangares()
        self.UsuariosW = Usuarios()

        self.main.addWidget(self.homeP)
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
        self.main.widget(1).cargarTable_hangares()
        self.main.widget(1).cargarCB()
    
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
        self.main.widget(4).reload()