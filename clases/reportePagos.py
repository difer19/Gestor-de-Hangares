from PyQt5.QtWidgets import QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class ReportePagos(QWidget):
    def __init__(self, Aerolinea, parent = None):
        super(ReportePagos, self).__init__(parent)
        self.iniciarGui()
        self.Aerolinea = Aerolinea
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReportePagos.ui', self)
        self.btn_rep = self.findChild(QPushButton, 'pushButton')
        self.tb_rep = self.findChild(QTableWidget, 'tableWidget')
        self.cb_rep = self.findChild(QComboBox, 'comboBox')

        self.cargarCB()

        self.btn_rep.clicked.connect(lambda: self.genRep())
    
    def cargarCB(self):
        self.cb_rep.addItem("General")
        self.cb_rep.addItem("Pagados")
        self.cb_rep.addItem("No Pagados")

    def genRep(self):
        if self.cb_rep.currentText() == "General":
            repCon = Conexion()
            query = ("""
                        SELECT idFacturas, valor, fecha_pago, Facturas.idFacturas 
                        , Facturas.Estado From Facturas join Reservas
                        on Facturas.idReserva = Reservas.idReservas join Aviones
                        on Reservas.idAvion = Aviones.idAvion join Aerolineas
                        on Aviones.IdAerolineas = Aerolineas.idAerolineas
                        Where Aerolineas.NombreAerolinea = '%s';
                    """)%(self.Aerolinea)
            number = repCon.numberResult(query)
            pagos = repCon.ejecutar_SQL(query)
            repCon.cerrar_conexion()
        elif self.cb_rep.currentText() == "Pagados":
            repCon = Conexion()
            query = ("""
                    SELECT idFacturas, valor, fecha_pago, Facturas.idReserva 
                    , Facturas.Estado From Facturas join Reservas
                    on Facturas.idReserva = Reservas.idReservas join Aviones
                    on Reservas.idAvion = Aviones.idAvion join Aerolineas
                    on Aviones.IdAerolineas = Aerolineas.idAerolineas
                    Where Aerolineas.NombreAerolinea = '%s' and Estado = 'Pagado'
                    union 
                    select 'Total' as idFacturas, sum(T1.valor) as valor
                    , ''  as fecha_pago,  0 as idReservas, '' as Estado
                    from
                    (SELECT idFacturas, valor, fecha_pago, Facturas.idReserva 
                    , Facturas.Estado From Facturas join Reservas
                    on Facturas.idReserva = Reservas.idReservas join Aviones
                    on Reservas.idAvion = Aviones.idAvion join Aerolineas
                    on Aviones.IdAerolineas = Aerolineas.idAerolineas
                    Where Aerolineas.NombreAerolinea = '%s' and Estado = 'Pagado') as T1;
                    """)%(self.Aerolinea, self.Aerolinea)
            pagos = repCon.ejecutar_SQL(query)
            number = repCon.numberResult(query)
            repCon.cerrar_conexion()
        elif self.cb_rep.currentText() == "No Pagados":
            repCon = Conexion()
            query = ("""
                    SELECT idFacturas, valor, fecha_pago, Facturas.idReserva 
                    , Facturas.Estado From Facturas join Reservas
                    on Facturas.idReserva = Reservas.idReservas join Aviones
                    on Reservas.idAvion = Aviones.idAvion join Aerolineas
                    on Aviones.IdAerolineas = Aerolineas.idAerolineas
                    Where Aerolineas.NombreAerolinea = '%s' and Estado = 'No Pagado'
                    union 
                    select 'Total' as idFacturas, sum(T1.valor) as valor
                    , ''  as fecha_pago,  0 as idReservas, '' as Estado
                    from
                    (SELECT idFacturas, valor, fecha_pago, Facturas.idReserva 
                    , Facturas.Estado From Facturas join Reservas
                    on Facturas.idReserva = Reservas.idReservas join Aviones
                    on Reservas.idAvion = Aviones.idAvion join Aerolineas
                    on Aviones.IdAerolineas = Aerolineas.idAerolineas
                    Where Aerolineas.NombreAerolinea = '%s' and Estado = 'No Pagado') as T1;
                    """)%(self.Aerolinea, self.Aerolinea)
            pagos = repCon.ejecutar_SQL(query)
            number = repCon.numberResult(query)
            repCon.cerrar_conexion()
        
        self.tb_rep.setRowCount(number)
        i = 0
        for pago in pagos:
            self.tb_rep.setItem(i, 0, QTableWidgetItem(str(pago[0])))
            self.tb_rep.setItem(i, 1, QTableWidgetItem(str(pago[1])))
            self.tb_rep.setItem(i, 2, QTableWidgetItem(str(pago[2])))
            self.tb_rep.setItem(i, 3, QTableWidgetItem(str(pago[3])))
            self.tb_rep.setItem(i, 4, QTableWidgetItem(str(pago[4])))
            i += 1