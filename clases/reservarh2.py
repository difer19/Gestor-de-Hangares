from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion 


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
        
        self.cargarCB()
        self.cargarTable_hangares()
        self.cargarTable_aviones()

        self.cb_aerolineas.currentIndexChanged.connect(lambda: self.cambiarTablaA())

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
            self.tb_hangares.setItem(i, 3, QTableWidgetItem(hangar[3]))
            i += 1
        hangarCon.cerrar_conexion()