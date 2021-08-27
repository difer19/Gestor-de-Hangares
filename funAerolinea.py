from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys

from PyQt5.uic.uiparser import QtWidgets

class PantallaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciarGui()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Pantalla_funaerolinea.ui', self)
        self.central = self.findChild(QWidget, 'centralwidget')
        self.menu = self.central.findChild(QWidget, 'widget')
        self.main = self.central.findChild(QWidget, "widget_main")
        self.btn_home = self.menu.findChild(QPushButton, 'home')
        self.btn_reservas = self.menu.findChild(QPushButton, 'reservas')
        self.btn_pagos = self.menu.findChild(QPushButton, 'pagos')
        self.btn_aviones = self.menu.findChild(QPushButton, 'aviones')
        self.btn_reportes = self.menu.findChild(QPushButton, 'reportes')
        self.btn_home.clicked.connect(self.homea)
        self.btn_reservas.clicked.connect(self.reservasa)
        self.btn_pagos.clicked.connect(self.pagosa)
        self.btn_aviones.clicked.connect(self.avionesa)
        self.btn_reportes.clicked.connect(self.reportesa)
        self.show()
    
    def homea(self):
        self.btn_home.setEnabled(False)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(True)
        self.btn_reportes.setEnabled(True)
    
    def reservasa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(False)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(True)
        self.btn_reportes.setEnabled(True)
    
    def pagosa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(False)
        self.btn_aviones.setEnabled(True)
        self.btn_reportes.setEnabled(True)
    
    def avionesa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(False)
        self.btn_reportes.setEnabled(True)
        uic.loadUi(r'GUI\Resources\UI\Aviones.ui', self.main)
        

    def reportesa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_pagos.setEnabled(True)
        self.btn_aviones.setEnabled(True)
        self.btn_reportes.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaInicial()
    app.exec_()