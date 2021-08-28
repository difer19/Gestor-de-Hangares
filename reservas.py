from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys

from PyQt5.uic.uiparser import QtWidgets

class Reservas(QWidget):
    def __init__(self, parent = None):
        super(Reservas, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Reservas.ui', self)
        self.btn_Reserva = self.findChild(QPushButton, 'Reserva')
        self.btn_Reprogramar = self.findChild(QPushButton, 'Reprogramar')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteReservas')
        
        self.btn_Reserva.clicked.connect(self.ReservaB)
        self.btn_Reprogramar.clicked.connect(self.ReprogramarB)
        self.btn_reporte.clicked.connect(self.reporteB)
    
    def ReservaB(self):
        self.btn_Reserva.setEnabled(False)
        self.btn_Reprogramar.setEnabled(True)
        self.btn_reporte.setEnabled(True)

    def ReprogramarB(self):
        self.btn_Reserva.setEnabled(True)
        self.btn_Reprogramar.setEnabled(False)
        self.btn_reporte.setEnabled(True)
    
    def reporteB(self):
        self.btn_Reserva.setEnabled(True)
        self.btn_Reprogramar.setEnabled(True)
        self.btn_reporte.setEnabled(False)