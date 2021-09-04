from PyQt5.QtWidgets import QPushButton, QWidget, QStackedWidget
from PyQt5 import uic
from PyQt5.uic.uiparser import QtWidgets
from clases.hangarRegister import HangarRegister


class Hangares(QWidget):
    def __init__(self, parent = None):
        super(Hangares, self).__init__(parent)
        self.iniciarGui()
        self.show()

    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Hangares.ui', self)
        self.btn_RE = self.findChild(QPushButton, 'RegistrarHangar')
        self.btn_datos = self.findChild(QPushButton, 'DatosHangar')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteHangar')
        self.main = self.findChild(QStackedWidget, 'stackedWidget')
        
        self.HangarR = HangarRegister()
        self.main.addWidget(QWidget())
        self.main.addWidget(self.HangarR)

        self.btn_RE.clicked.connect(self.REb)
        self.btn_datos.clicked.connect(self.datosB)
        self.btn_reporte.clicked.connect(self.reporteB)
    
    def REb(self):
        self.btn_RE.setEnabled(False)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(1)
        
    def datosB(self):
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(False)
        self.btn_reporte.setEnabled(True)
    
    def reporteB(self):
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(False)
    
    