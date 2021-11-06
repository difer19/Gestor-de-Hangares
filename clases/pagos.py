from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
from clases.pagarRe import PagarRe
from clases.reportePagos import ReportePagos


class Pagos(QWidget):
    def __init__(self, aerolinea, parent = None):
        super(Pagos, self).__init__(parent)
        self.aerolinea = aerolinea
        self.iniciarGui()
        self.show()

    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Pagos.ui', self)
        self.btn_Pago = self.findChild(QPushButton, 'RealizarPago')
        self.btn_reporte = self.findChild(QPushButton, 'ReportePagos')
        self.main = self.findChild(QStackedWidget, 'stackedWidget')

        self.PagarW = PagarRe(self.aerolinea)
        self.PagosRe = ReportePagos(self.aerolinea)

        self.main.addWidget(QWidget())
        self.main.addWidget(self.PagarW)
        self.main.addWidget(self.PagosRe)

        self.btn_Pago.clicked.connect(self.pagoB)
        self.btn_reporte.clicked.connect(self.reporteB)
    
    def update(self):
        self.main.widget(1).cargarTable()

    def pagoB(self):
        self.btn_Pago.setEnabled(False)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(1)
    
    def reporteB(self):
        self.btn_Pago.setEnabled(True)
        self.btn_reporte.setEnabled(False)
        self.main.setCurrentIndex(2)
