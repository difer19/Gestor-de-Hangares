from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys

from PyQt5.uic.uiparser import QtWidgets

class PantallaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciarGui()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Pantalla_administradorHangares.ui', self)
        self.central = self.findChild(QWidget, 'centralwidget')
        self.menu = self.central.findChild(QWidget, 'widget')
        self.btn_home = self.menu.findChild(QPushButton, 'home')
        self.btn_reservas = self.menu.findChild(QPushButton, 'reservas')
        self.btn_aerolineas = self.menu.findChild(QPushButton, 'aerolineas')
        self.btn_hangares = self.menu.findChild(QPushButton, 'hangares')
        self.btn_reportes = self.menu.findChild(QPushButton, 'reportes')
        self.btn_home.clicked.connect(self.homea)
        self.btn_reservas.clicked.connect(self.reservasa)
        self.btn_aerolineas.clicked.connect(self.aerolineasa)
        self.btn_hangares.clicked.connect(self.hangaresa)
        self.btn_reportes.clicked.connect(self.reportesa)
        self.show()
    
    def homea(self):
        self.btn_home.setEnabled(False)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(True)
        self.btn_reportes.setEnabled(True)
    
    def reservasa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(False)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(True)
        self.btn_reportes.setEnabled(True)
    
    def aerolineasa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(False)
        self.btn_hangares.setEnabled(True)
        self.btn_reportes.setEnabled(True)
    
    def hangaresa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(False)
        self.btn_reportes.setEnabled(True)

    def reportesa(self):
        self.btn_home.setEnabled(True)
        self.btn_reservas.setEnabled(True)
        self.btn_aerolineas.setEnabled(True)
        self.btn_hangares.setEnabled(True)
        self.btn_reportes.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaInicial()
    app.exec_()