from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion
from datetime import *


class PagarRe(QWidget):
    def __init__(self, aerolina, parent = None):
        super(PagarRe, self).__init__(parent)
        self.Aerolinea = aerolina
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        self.update()
        uic.loadUi(r'GUI\Resources\UI\PagarRe.ui', self)
        self.tb_facturas = self.findChild(QTableWidget, 'tableWidget')
        self.btn_pagar = self.findChild(QPushButton, 'pushButton_2')

        self.cargarTable()

        self.btn_pagar.clicked.connect(lambda: self.pagarH())
    
    def cargarTable(self):
        ResCon = Conexion()
        idA = ResCon.ejecutar_SQL("SELECT idAerolineas FROM Aerolineas WHERE NombreAerolinea = '%s'" %(self.Aerolinea))
        idAerolinea = idA.fetchall()
        idAs = int(idAerolinea[0][0])
        query = """SELECT  Facturas.idFacturas, Facturas.Valor, Facturas.Estado FROM Facturas 
                JOIN Reservas ON Facturas.idReserva = idReservas
                JOIN Aviones ON Reservas.idAvion = Aviones.idAvion JOIN
                Aerolineas ON Aviones.idAerolineas = Aerolineas.idAerolineas
                Where Estado = 'No Pagado'
                and Aerolineas.idAerolineas = '%s'""" %(idAs)
        facturas = ResCon.ejecutar_SQL(query)
        numberA = ResCon.numberResult(query)
        self.tb_facturas.setRowCount(numberA)
        i = 0
        for factura  in facturas:
            self.tb_facturas.setItem(i, 0, QTableWidgetItem(str(factura[0])))
            self.tb_facturas.setItem(i, 1, QTableWidgetItem(str(factura[1])))
            self.tb_facturas.setItem(i, 2, QTableWidgetItem(factura[2]))
            i += 1
        ResCon.cerrar_conexion()

    def pagarH(self):
        idFactura = self.tb_facturas.selectedIndexes()[0].data()
        today = datetime.today().strftime('%d-%m-%Y')
        pagar = Conexion()
        query = "UPDATE Facturas SET Estado = 'Pagado', fecha_pago= '%s' WHERE idFacturas ='%s'" %(today, idFactura)
        pagar.insertarDatos(query)
        pagar.cerrar_conexion()
        self.cargarTable()
