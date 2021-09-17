from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
from clases.aerolineaRegister import AerolineaRegister


class Aerolineas(QWidget):
    def __init__(self, parent = None):
        super(Aerolineas, self).__init__(parent)
        self.iniciarGui()
        self.show
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Aerolineas.ui', self)
        self.btn_RE = self.findChild(QPushButton, 'RegistrarAerolinea')
        self.btn_datos = self.findChild(QPushButton, 'Datos')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteAerolinea')
        self.main = self.findChild(QStackedWidget, 'stackedWidget')

        self.AeroR = AerolineaRegister()
        
        self.main.addWidget(QWidget())
        self.main.addWidget(self.AeroR)
        self.main.addWidget(QWidget())
        self.main.addWidget(QWidget())

        self.btn_RE.clicked.connect(self.REb)
        self.btn_datos.clicked.connect(self.datosB)
        self.btn_reporte.clicked.connect(self.reporteB)
    
    def REb(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(False)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(1)

    def datosB(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(False)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(2)
    
    def reporteB(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(False)
        self.main.setCurrentIndex(3)
