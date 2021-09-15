from clases.aerolineas import Aerolineas
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion 


class ReservarHangar1(QWidget):
    def __init__(self, aerolinea, parent = None, ):
        super(ReservarHangar1, self).__init__(parent)
        self.Aerolinea = aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        self.update()
        uic.loadUi(r'GUI\Resources\UI\ReservasRe.ui', self)
        self.tb_aviones = self.findChild(QTableWidget, 'tableWidget_2')
        self.tb_hangares = self.findChild(QTableWidget, 'tableWidget')

        self.cargarTable_aviones()
        self.cargarTable_hangares()
    
    def cargarTable_aviones(self):
        avionCon = Conexion()
        idA = avionCon.ejecutar_SQL("SELECT idAerolineas FROM Aerolineas WHERE NombreAerolinea = '%s'" %(self.Aerolinea))
        idAerolinea = idA.fetchall()
        idAs = int(idAerolinea[0][0])
        query = "SELECT idAvion, modelo, area FROM Aviones WHERE idAerolineas = '%s'" %(idAs)
        aviones = avionCon.ejecutar_SQL(query)
        numberA = avionCon.numberResult(query)
        self.tb_aviones.setRowCount(numberA)
        i = 0
        for avion in aviones:
            self.tb_aviones.setItem(i, 0, QTableWidgetItem(avion[0]))
            self.tb_aviones.setItem(i, 1, QTableWidgetItem(avion[1]))
            self.tb_aviones.setItem(i, 3, QTableWidgetItem(str(avion[2])))
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
            self.tb_hangares.setItem(i, 3, QTableWidgetItem(hangar[3]))
            i += 1
        hangarCon.cerrar_conexion()