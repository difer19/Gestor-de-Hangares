from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget 
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *
from datetime import *


class ReprReserva(QWidget):
    def __init__(self, aerolinea, parent = None):
        super(ReprReserva, self).__init__(parent)
        self.aerolinea = aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReprgReserva.ui', self)
        self.tb_reservas = self.findChild(QTableWidget, 'tableWidget')
        self.le_dayIn = self.findChild(QLineEdit, 'lineEdit')
        self.le_MesIn = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_yearIn = self.findChild(QLineEdit, 'lineEdit_3')
        self.le_dayFin = self.findChild(QLineEdit, 'lineEdit_4')
        self.le_MesFin = self.findChild(QLineEdit, 'lineEdit_5')
        self.le_yearFin = self.findChild(QLineEdit, 'lineEdit_6')
       
        self.le_dayIn.setValidator(QIntValidator())
        self.le_MesIn.setValidator(QIntValidator())
        self.le_yearIn.setValidator(QIntValidator())
        self.le_dayFin.setValidator(QIntValidator())
        self.le_MesFin.setValidator(QIntValidator())
        self.le_yearFin.setValidator(QIntValidator())
        
        self.btn_cancelar = self.findChild(QPushButton, 'pushButton')
        self.btn_reprogramar = self.findChild(QPushButton, 'pushButton_2')

        self.cargarTable()

        self.btn_cancelar.clicked.connect(lambda: self.cancelar())
        self.btn_reprogramar.clicked.connect(lambda: self.reprogramar())

    def cargarTable(self):
        reservaCon = Conexion()
        query = """
                    SELECT Reservas.idReservas, Reservas.fecha_inicial, Reservas.fecha_final,
                    Reservas.idAvion, Reservas.idHangar 
                    FROM Reservas JOIN Facturas ON Reservas.idReservas = Facturas.idReserva JOIN
                    Aviones ON Reservas.idAvion = Aviones.idAvion 
                    JOIN Aerolineas ON Aviones.IdAerolineas = Aerolineas.idAerolineas
                    WHERE Facturas.Estado = 'No Pagado' and Aerolineas.NombreAerolinea = '%s';
                """%(self.aerolinea)
        idR = reservaCon.ejecutar_SQL(query).fetchall()
        j = 0
        for reserva in idR:
            fechaInicial = datetime.strptime(reserva[2], '%d/%m/%Y')
            if fechaInicial > datetime.today():
                j += 1
        i = 0
        self.tb_reservas.setRowCount(j)
        for reserva in idR:
            fechaInicial = datetime.strptime(reserva[2], '%d/%m/%Y')
            if fechaInicial > datetime.today():
                self.tb_reservas.setItem(i, 0, QTableWidgetItem(str(reserva[0])))
                self.tb_reservas.setItem(i, 1, QTableWidgetItem(reserva[1]))
                self.tb_reservas.setItem(i, 2, QTableWidgetItem(reserva[2]))
                self.tb_reservas.setItem(i, 3, QTableWidgetItem(reserva[3]))
                self.tb_reservas.setItem(i, 4, QTableWidgetItem(reserva[4]))
                i += 1
        reservaCon.cerrar_conexion()

    def cancelar(self):
        if self.tb_reservas.selectedIndexes() == []:
            return False
        idRF = str(self.tb_reservas.selectedIndexes()[0].data())
        delR = Conexion()
        delR.insertarDatos("DELETE FROM Facturas WHERE idFacturas = '%s'" %(idRF))
        delR.insertarDatos("DELETE FROM Reservas WHERE idReservas = '%s'" %(idRF))
        delR.cerrar_conexion()
        Dialog2("La reserva fue cancelada")
        self.cargarTable()

    def reprogramar(self):
        if self.tb_reservas.selectedIndexes() == []:
            return False
        if self.validacion() == False:
            Dialog("Campos sin fijar")
            return False
        strIni = self.le_dayIn.text()+"/"+self.le_MesIn.text()+"/"+self.le_yearIn.text()
        strFin = self.le_dayFin.text()+"/"+self.le_MesFin.text()+"/"+self.le_yearFin.text()
        self.fechaInicial = datetime.strptime(strIni, '%d/%m/%Y')
        self.fechaFinal = datetime.strptime(strFin, '%d/%m/%Y')
        if self.fechaFinal > self.fechaInicial and self.fechaFinal > datetime.today() and self.fechaInicial > datetime.today():
            if self.disponibilidadH() == True:
                reservar = Conexion()
                reserva = "UPDATE Reservas SET fecha_inicial = '%s', fecha_final = '%s' WHERE idReservas = '%s'" %(strIni, strFin, str(self.tb_reservas.selectedIndexes()[0].data()))
                delta = self.fechaFinal - self.fechaInicial
                Capacidad = reservar.ejecutar_SQL("SELECT Capacidad From Hangares WHERE idHangar = '%s'"%(self.tb_reservas.selectedIndexes()[4].data())).fetchall()
                valor_factura = int(Capacidad[0][0])*20000*(delta.days)
                factura  = "UPDATE Facturas SET Valor = '%s' WHERE idReserva = '%s'"%(valor_factura, int(self.tb_reservas.selectedIndexes()[0].data()))
                reservar.insertarDatos(reserva)
                reservar.insertarDatos(factura)
                reservar.cerrar_conexion()
                self.le_dayIn.clear()
                self.le_MesIn.clear()
                self.le_yearIn.clear()
                self.le_dayFin.clear()
                self.le_MesFin.clear()
                self.le_yearFin.clear()
                Dialog2("Reserva Reprogramada")
                self.cargarTable()
            else:
                Dialog("Fechas invalidas")
        else:
            Dialog("Fechas invalidas")

    
    def disponibilidadH(self):
        dispon = Conexion()
        idAvion = self.tb_reservas.selectedIndexes()[3].data()
        idHangar = self.tb_reservas.selectedIndexes()[4].data()
        query = "SELECT idReservas ,fecha_inicial, fecha_final FROM Reservas WHERE idAvion = '%s' OR idhangar = '%s'" %(idAvion, idHangar)
        if dispon.numberResult(query) == 0:
            return True
        else:
            reservas = dispon.ejecutar_SQL(query).fetchall()
            count = 0
            for reserva in reservas:
                initDate = datetime.strptime(str(reserva[1]), '%d/%m/%Y')
                FinishDate = datetime.strptime(str(reserva[2]), '%d/%m/%Y')
                if self.fechaInicial > initDate and self.fechaInicial < FinishDate:
                    print(reserva[0])
                    if int(reserva[0]) != int(self.tb_reservas.selectedIndexes()[0].data()):
                        count += 1
                elif self.fechaFinal > initDate and self.fechaFinal < FinishDate:
                    print(reserva[0])
                    if int(reserva[0]) != int(self.tb_reservas.selectedIndexes()[0].data()):
                        count += 1
            if count == 0:
                dispon.cerrar_conexion()
                return True
            else:
                dispon.cerrar_conexion()
                return False

    def validacion(self):
        count = 0
        if not self.le_dayIn.text().strip():
            count += 1
        if not self.le_MesIn.text().strip():
            count += 1
        if not self.le_yearIn.text().strip():
            count += 1
        if not self.le_dayFin.text().strip():
            count += 1
        if not self.le_MesFin.text().strip():
            count += 1
        if not self.le_yearFin.text().strip():
            count += 1
        if count == 0:
            return True
        return False
