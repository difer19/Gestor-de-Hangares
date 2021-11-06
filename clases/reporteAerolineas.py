from PyQt5.QtWidgets import QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class ReporteAerolineas(QWidget):
    def __init__(self, parent = None):
        super(ReporteAerolineas, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReporteAerolineas.ui', self)
        self.btn_rep = self.findChild(QPushButton, 'pushButton')
        self.btn_rep2 = self.findChild(QPushButton, 'pushButton_2')
        self.tb_rep = self.findChild(QTableWidget, 'tableWidget')
        self.tb_rep2 = self.findChild(QTableWidget, 'tableWidget_2')
        self.cb_opciones = self.findChild(QComboBox, 'comboBox')

        self.cargarCB()

        self.btn_rep.clicked.connect(lambda: self.genRep())
        self.btn_rep2.clicked.connect(lambda: self.genRep2())
    
    def cargarCB(self):
        self.cb_opciones.addItem("Aviones")
        self.cb_opciones.addItem("Reservas")
        self.cb_opciones.addItem("Pagos")
        self.cb_opciones.addItem("Deudas")
        
    def genRep(self):
        aeroCon = Conexion()
        query = ("SELECT * FROM Aerolineas")
        aerolineas = aeroCon.ejecutar_SQL(query)
        number = aeroCon.numberResult(query)
        aeroCon.cerrar_conexion()
        i = 0
        self.tb_rep.setRowCount(number)
        for aerolinea in aerolineas:
            self.tb_rep.setItem(i, 0, QTableWidgetItem(str(aerolinea[0])))
            self.tb_rep.setItem(i, 1, QTableWidgetItem(str(aerolinea[1])))
            i += 1


    def genRep2(self):
        if self.cb_opciones.currentText() == "Aviones":
            aeroCon = Conexion()
            query = ("""
                        select NombreAerolinea, count(Aviones.idAvion) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas group by 1
                        union select 'Total' as NombreAerolinea, sum(T1.numero) as numero from
                        (select NombreAerolinea, count(Aviones.idAvion) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas group by 1) as T1
                    """)
            aerolineas = aeroCon.ejecutar_SQL(query)
            number = aeroCon.numberResult(query)
            aeroCon.cerrar_conexion()
        elif self.cb_opciones.currentText() == "Reservas":
            aeroCon = Conexion()
            query = ("""
                        select NombreAerolinea, count(Reservas.idReservas) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas join Reservas
                        on Aviones.idAvion = Reservas.idAvion group by 1
                        union select 'Total' as NombreAerolinea, sum(T1.numero) as numero from
                        (select NombreAerolinea, count(Reservas.idReservas) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas join Reservas
                        on Aviones.idAvion = Reservas.idAvion group by 1) as T1
                    """)
            aerolineas = aeroCon.ejecutar_SQL(query)
            number = aeroCon.numberResult(query)
            aeroCon.cerrar_conexion()
        elif self.cb_opciones.currentText() == "Pagos":
            aeroCon = Conexion()
            query = ("""
                        select NombreAerolinea, sum(Facturas.Valor) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas join Reservas
                        on Aviones.idAvion = Reservas.idAvion join Facturas on Reservas.idReservas = Facturas.idReserva
                        where Facturas.Estado = 'Pagado' group by 1
                        union select 'Total' as NombreAerolinea, sum(T1.numero) as numero from
                        (select NombreAerolinea, sum(Facturas.Valor) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas join Reservas
                        on Aviones.idAvion = Reservas.idAvion join Facturas on Reservas.idReservas = Facturas.idReserva
                        where Facturas.Estado = 'Pagado' group by 1) as T1;
                    """)
            aerolineas = aeroCon.ejecutar_SQL(query)
            number = aeroCon.numberResult(query)
            aeroCon.cerrar_conexion()
        elif self.cb_opciones.currentText() == "Deudas":
            aeroCon = Conexion()
            query = ("""
                        select NombreAerolinea, sum(Facturas.Valor) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas join Reservas
                        on Aviones.idAvion = Reservas.idAvion join Facturas on Reservas.idReservas = Facturas.idReserva
                        where Facturas.Estado = 'No Pagado' group by 1
                        union select 'Total' as NombreAerolinea, sum(T1.numero) as numero from
                        (select NombreAerolinea, sum(Facturas.Valor) as numero from Aerolineas
                        join Aviones on Aerolineas.idAerolineas = Aviones.IdAerolineas join Reservas
                        on Aviones.idAvion = Reservas.idAvion join Facturas on Reservas.idReservas = Facturas.idReserva
                        where Facturas.Estado = 'No Pagado' group by 1) as T1;
                    """)
            aerolineas = aeroCon.ejecutar_SQL(query)
            number = aeroCon.numberResult(query)
            aeroCon.cerrar_conexion()
        
        i = 0
        self.tb_rep2.setRowCount(number)
        for aerolinea in aerolineas:
            self.tb_rep2.setItem(i, 0, QTableWidgetItem(str(aerolinea[0])))
            self.tb_rep2.setItem(i, 1, QTableWidgetItem(str(aerolinea[1])))
            i += 1
        
