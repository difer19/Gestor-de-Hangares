from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class ReporteReservas(QWidget):
    def __init__(self, Aerolinea, parent = None):
        super(ReporteReservas, self).__init__(parent)
        self.iniciarGui()
        self.Aerolinea = Aerolinea
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReporteReservas.ui', self)
        self.btn_rep = self.findChild(QPushButton, 'pushButton')
        self.tb_rep = self.findChild(QTableWidget, 'tableWidget')
    
        self.btn_rep.clicked.connect(lambda: self.genRep())
    
    def genRep(self):
        reservasCon = Conexion()
        query = ("""
                SELECT Reservas.idReservas, Reservas.fecha_inicial, Reservas.fecha_final, 
                Reservas.idAvion, Reservas.idhangar, Facturas.Valor
                FROM Reservas JOIN Facturas ON Reservas.idReservas = Facturas.idReserva JOIN
                Aviones ON Reservas.idAvion = Aviones.idAvion 
                JOIN Aerolineas ON Aviones.IdAerolineas = Aerolineas.idAerolineas
                WHERE Facturas.Estado = 'No Pagado' and Aerolineas.NombreAerolinea = '%s'
                """)%(self.Aerolinea)
        reservas = reservasCon.ejecutar_SQL(query)
        number = reservasCon.numberResult(query)
        self.tb_rep.setRowCount(number)
        i = 0
        for reserva in reservas:
            self.tb_rep.setItem(i, 0, QTableWidgetItem(str(reserva[0])))
            self.tb_rep.setItem(i, 1, QTableWidgetItem(str(reserva[1])))
            self.tb_rep.setItem(i, 2, QTableWidgetItem(str(reserva[2])))
            self.tb_rep.setItem(i, 3, QTableWidgetItem(str(reserva[3])))
            self.tb_rep.setItem(i, 4, QTableWidgetItem(str(reserva[4])))
            self.tb_rep.setItem(i, 5, QTableWidgetItem(str(reserva[5])))
            i += 1
        reservasCon.cerrar_conexion()