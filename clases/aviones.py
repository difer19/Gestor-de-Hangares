from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
from clases.avionRegister import AvionRegister
from clases.dataAvion import AvionData


class Aviones(QWidget):
    def __init__(self, Aerolinea, parent = None):
        super(Aviones, self).__init__(parent)
        self.Aerolinea = Aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Aviones.ui', self)
        self.btn_RE = self.findChild(QPushButton, 'RegistrarAvion')
        self.btn_datos = self.findChild(QPushButton, 'DatosAvion')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteAvion')
        self.main = self.findChild(QStackedWidget, 'stackedWidget')

        self.avionR = AvionRegister(self.Aerolinea)
        self.avionD = AvionData(self.Aerolinea)

        self.main.addWidget(QWidget())
        self.main.addWidget(self.avionR)
        self.main.addWidget(self.avionD)
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
        self.main.widget(1).cargarTable()

    def datosB(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(False)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(2)
        self.main.widget(2).cargarCB()
    
    def reporteB(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(False)
        self.main.setCurrentIndex(3)
    