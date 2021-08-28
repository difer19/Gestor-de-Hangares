from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys

from PyQt5.uic.uiparser import QtWidgets

class Aviones(QWidget):
    def __init__(self, parent = None):
        super(Aviones, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Aviones.ui', self)
        self.btn_RE = self.findChild(QPushButton, 'RegistrarAvion')
        self.btn_datos = self.findChild(QPushButton, 'DatosAvion')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteAvion')
        
        self.btn_RE.clicked.connect(self.REb)
        self.btn_datos.clicked.connect(self.datosB)
        self.btn_reporte.clicked.connect(self.reporteB)

    def REb(self):
        self.btn_RE.setEnabled(False)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(True)

    def datosB(self):
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(False)
        self.btn_reporte.setEnabled(True)
    
    def reporteB(self):
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(False)
    