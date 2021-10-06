from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion 
from datetime import *
from clases.dialog import *
from PyQt5.QtGui import QIntValidator


class ReservarHangar2(QWidget):
    def __init__(self, parent = None):
        super(ReservarHangar2, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        self.update()
        uic.loadUi(r'GUI\Resources\UI\ReservasRe2.ui', self)
        self.cb_aerolineas = self.findChild(QComboBox, 'comboBox')
        self.tb_aviones = self.findChild(QTableWidget, 'tableWidget_2')
        self.tb_hangares = self.findChild(QTableWidget, 'tableWidget')
        self.le_dayIn = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_MesIn = self.findChild(QLineEdit, 'lineEdit')
        self.le_yearIn = self.findChild(QLineEdit, 'lineEdit_3')
        self.le_dayFin = self.findChild(QLineEdit, 'lineEdit_4')
        self.le_MesFin = self.findChild(QLineEdit, 'lineEdit_6')
        self.le_yearFin = self.findChild(QLineEdit, 'lineEdit_5')
        self.btn_reservar = self.findChild(QPushButton, 'pushButton')

        self.le_dayIn.setValidator(QIntValidator())
        self.le_MesIn.setValidator(QIntValidator())
        self.le_yearIn.setValidator(QIntValidator())
        self.le_dayFin.setValidator(QIntValidator())
        self.le_MesFin.setValidator(QIntValidator())
        self.le_yearFin.setValidator(QIntValidator())
        
        self.cargarCB()
        self.cargarTable_hangares()
        self.cargarTable_aviones()

        self.cb_aerolineas.currentIndexChanged.connect(lambda: self.cambiarTablaA())
        self.btn_reservar.clicked.connect(lambda: self.reservarHa())

    def reservarHa(self):
        if self.tb_aviones.selectedIndexes() == [] and self.tb_hangares.selectedIndexes() == []:
            return False
        if self.validacion() == False:
            Dialog("Campos sin fijar")
            return False
        strIni = self.le_dayIn.text()+"/"+self.le_MesIn.text()+"/"+self.le_yearIn.text()
        strFin = self.le_dayFin.text()+"/"+self.le_MesFin.text()+"/"+self.le_yearFin.text()
        self.fechaInicial = datetime.strptime(strIni, '%d/%m/%Y')
        self.fechaFinal = datetime.strptime(strFin, '%d/%m/%Y')
        if self.fechaFinal > self.fechaInicial and self.fechaFinal > datetime.today() and self.fechaInicial > datetime.today():
            self.idAvion =  self.tb_aviones.selectedIndexes()[0].data()
            Area =  self.tb_aviones.selectedIndexes()[2].data()
            self.idHangar =  self.tb_hangares.selectedIndexes()[0].data()
            Capacidad =  self.tb_hangares.selectedIndexes()[1].data()
            if int(Capacidad) < int(Area):
                Dialog("El hangar no es \n adecuado para ese avion")
            elif self.disponibilidadH() == True:
                reservar = Conexion()
                idReserva = reservar.ejecutar_SQL("SELECT idReservas FROM Reservas").fetchall[0][0] + 1
                reserva = "INSERT INTO Reservas (idReservas, fecha_inicial, fecha_final, idAvion, idhangar) VALUES ('%s','%s','%s','%s','%s')" %(idReserva, strIni, strFin, self.idAvion, self.idHangar)
                delta = self.fechaFinal - self.fechaInicial
                valor_factura = int(Capacidad)*20000*(delta.days)
                factura  = "INSERT INTO Facturas (idFacturas, Valor, fecha_pago, idReserva, Estado) VALUES ('%s','%s','%s','%s','%s');" %(idReserva, valor_factura, "Null", idReserva, "No Pagado")
                reservar.insertarDatos(reserva)
                reservar.insertarDatos(factura)
                reservar.cerrar_conexion()
                self.le_dayIn.clear()
                self.le_MesIn.clear()
                self.le_yearIn.clear()
                self.le_dayFin.clear()
                self.le_MesFin.clear()
                self.le_yearFin.clear()
                Dialog2("El hangar fue reservado")
            else:
                Dialog("No se puede hacer \n la reserva")
        else:
            Dialog("fechas invalidas")
    
    def disponibilidadH(self):
        dispon = Conexion()
        query = "SELECT fecha_inicial, fecha_final FROM Reservas WHERE idAvion = '%s' OR idhangar = '%s'" %(self.idAvion, self.idHangar)
        if dispon.numberResult(query) == 0:
            return True
        else:
            reservas = dispon.ejecutar_SQL(query).fetchall()
            count = 0
            for reserva in reservas:
                initDate = datetime.strptime(str(reserva[0]), '%d/%m/%Y')
                FinishDate = datetime.strptime(str(reserva[1]), '%d/%m/%Y')
                if self.fechaInicial > initDate and self.fechaInicial < FinishDate:
                    count += 1
                elif self.fechaFinal > initDate and self.fechaFinal < FinishDate:
                    count += 1
            if count == 0:
                return True
            else:
                dispon.cerrar_conexion()
                return False

    def cambiarTablaA(self):
        self.cargarTable_aviones()
    
    def cargarCB(self):
        self.cb_aerolineas.clear()
        aerolineas = Conexion()
        cursor = aerolineas.ejecutar_SQL("SELECT NombreAerolinea FROM Aerolineas")
        for Aerolinea in cursor.fetchall():
            self.cb_aerolineas.addItem(Aerolinea[0])
        aerolineas.cerrar_conexion()

    def cargarTable_aviones(self):
        avionCon = Conexion()
        idA = avionCon.ejecutar_SQL("SELECT idAerolineas FROM Aerolineas WHERE NombreAerolinea = '%s'" %(self.cb_aerolineas.currentText()))
        idAerolinea = idA.fetchall()
        idAs = ""
        for af in idAerolinea:
                idAs = af
        query = "SELECT idAvion, modelo, area FROM Aviones WHERE idAerolineas = '%s'" %(idAs)
        aviones = avionCon.ejecutar_SQL(query)
        numberA = avionCon.numberResult(query)
        self.tb_aviones.setRowCount(numberA)
        i = 0
        for avion in aviones:
            self.tb_aviones.setItem(i, 0, QTableWidgetItem(avion[0]))
            self.tb_aviones.setItem(i, 1, QTableWidgetItem(avion[1]))
            self.tb_aviones.setItem(i, 2, QTableWidgetItem(str(avion[2])))
            i += 1
        avionCon.cerrar_conexion()

    def cargarTable_hangares(self):
        hangarCon = Conexion()
        hangares = hangarCon.ejecutar_SQL("SELECT * FROM Hangares")
        numberH = hangarCon.numberResult("SELECT * FROM Hangares")
        self.tb_hangares.setRowCount(numberH)
        i = 0
        for hangar in hangares:
            self.tb_hangares.setItem(i, 0, QTableWidgetItem(hangar[0]))
            self.tb_hangares.setItem(i, 1, QTableWidgetItem(str(hangar[1])))
            self.tb_hangares.setItem(i, 2, QTableWidgetItem(hangar[2]))
            i += 1
        hangarCon.cerrar_conexion()
    
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