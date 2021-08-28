from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys

from PyQt5.uic.uiparser import QtWidgets

class Pagos(QWidget):
    def __init__(self, parent = None):
        super(Pagos, self).__init__(parent)
        self.iniciarGui()
        self.show()

    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Pagos.ui', self)
        self.btn_Pago = self.findChild(QPushButton, 'RealizarPago')
        self.btn_reporte = self.findChild(QPushButton, 'ReportePagos')
        self.btn_Pago.clicked.connect(self.pagoB)
        self.btn_reporte.clicked.connect(self.reporteB)

    def pagoB(self):
        self.btn_Pago.setEnabled(False)
        self.btn_reporte.setEnabled(True)
    
    def reporteB(self):
        self.btn_Pago.setEnabled(True)
        self.btn_reporte.setEnabled(False)
