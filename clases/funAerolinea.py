from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
from clases.reservas import Reservas
from clases.pagos import Pagos
from clases.aviones import Aviones


class FunAerolinea(QMainWindow):
    def __init__(self, aerolinea):
        super().__init__()
        self.aerolinea = aerolinea
        self.iniciarGui()

    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Pantalla_funaerolinea.ui', self)
        self.central = self.findChild(QWidget, 'centralwidget')
        self.menu = self.central.findChild(QWidget, 'widget')
        self.main = self.central.findChild(QStackedWidget, "stackedWidget_main")
        self.btn_home = self.menu.findChild(QPushButton, 'home')
        self.btn_reservas = self.menu.findChild(QPushButton, 'reservas')
        self.btn_pagos = self.menu.findChild(QPushButton, 'pagos')
        self.btn_aviones = self.menu.findChild(QPushButton, 'aviones')
        
        self.ReservasW = Reservas(self.aerolinea)
        self.PagosW = Pagos(self.aerolinea)
        self.AvionesW = Aviones(self.aerolinea)

        self.main.addWidget(QWidget())
        self.main.addWidget(self.ReservasW)
        self.main.addWidget(self.PagosW)
        self.main.addWidget(self.AvionesW)
        
        self.btn_home.clicked.connect(self.homea)
        self.btn_reservas.clicked.connect(self.reservasa)
        self.btn_pagos.clicked.connect(self.pagosa)
        self.btn_aviones.clicked.connect(self.avionesa)
        self.show()
    
    def homea(self):
        self.btn_home.setEnabled(False)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(True)
        self.main.setCurrentIndex(0)
    
    def reservasa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(False)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(True)
        self.main.setCurrentIndex(1)
    
    def pagosa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(False)
        self.btn_aviones.setEnabled(True)
        self.main.setCurrentIndex(2)
        self.main.widget(2).update()
    
    def avionesa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(False) 
        self.main.setCurrentIndex(3)
