from clases.reprReserva import ReprReserva
from clases.reservarh1 import ReservarHangar1
from clases.reporteReservas import ReporteReservas
from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget
from PyQt5 import uic


class Reservas(QWidget):
    def __init__(self, aerolinea, parent = None):
        super(Reservas, self).__init__(parent)
        self.aerolinea = aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Reservas.ui', self)
        self.btn_Reserva = self.findChild(QPushButton, 'Reserva')
        self.btn_Reprogramar = self.findChild(QPushButton, 'Reprogramar')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteReservas')
        self.main = self.findChild(QStackedWidget, 'stackedWidget')

        self.ReservarW = ReservarHangar1(self.aerolinea)
        self.Repr = ReprReserva(self.aerolinea)
        self.ReservaR = ReporteReservas(self.aerolinea)

        self.main.addWidget(QWidget())
        self.main.addWidget(self.ReservarW)
        self.main.addWidget(self.Repr)
        self.main.addWidget(self.ReservaR)
        
        self.btn_Reserva.clicked.connect(self.ReservaB)
        self.btn_Reprogramar.clicked.connect(self.ReprogramarB)
        self.btn_reporte.clicked.connect(self.reporteB)
    
    def reload(self):
        self.main.widget(1).cargarTable_aviones()
    
    def ReservaB(self):
        self.btn_Reserva.setEnabled(False)
        self.btn_Reprogramar.setEnabled(True)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(1)

    def ReprogramarB(self):
        self.btn_Reserva.setEnabled(True)
        self.btn_Reprogramar.setEnabled(False)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(2)
        self.main.widget(2).cargarTable()
    
    def reporteB(self):
        self.btn_Reserva.setEnabled(True)
        self.btn_Reprogramar.setEnabled(True)
        self.btn_reporte.setEnabled(False)
        self.main.setCurrentIndex(3)