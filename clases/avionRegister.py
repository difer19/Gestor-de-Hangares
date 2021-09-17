from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTextEdit, QWidget, QTableWidgetItem
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *


class AvionRegister(QWidget):
    def __init__(self,  Aerolinea, parent = None):
        super(AvionRegister, self).__init__(parent)
        self.Aerolinea = Aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\AvionRegister.ui', self)
        self.le_id = self.findChild(QLineEdit, 'lineEdit')
        self.le_modelo = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_peso = self.findChild(QLineEdit, 'lineEdit_3')
        self.le_Capacidad = self.findChild(QLineEdit, 'lineEdit_6')
        self.le_numMot = self.findChild(QLineEdit, 'lineEdit_5')
        self.le_area = self.findChild(QLineEdit, 'lineEdit_4')
        self.tx_descripcion = self.findChild(QTextEdit, 'textEdit')
        self.cb_tipo = self.findChild(QComboBox, 'comboBox')
        self.cb_tipoPr = self.findChild(QComboBox, 'comboBox_2')
        self.btn_AvionReg = self.findChild(QPushButton, 'pushButton')
        self.tb_aviones = self.findChild(QTableWidget, 'tableWidget')
        self.btn_AvionDel = self.findChild(QPushButton, 'pushButton_2')

        self.cargarTable()
        self.CBUpdate()

        self.btn_AvionReg.clicked.connect(lambda: self.AvionRegM())
        self.btn_AvionDel.clicked.connect(lambda: self.AvionDelM())
    
    def cargarTable(self):
        avionCon = Conexion()
        idA = avionCon.ejecutar_SQL("SELECT idAerolineas FROM Aerolineas WHERE NombreAerolinea = '%s'" %(self.Aerolinea))
        idAerolinea = idA.fetchall()
        idAs = int(idAerolinea[0][0])
        query = "SELECT idAvion, modelo, tipo, capacidad FROM Aviones WHERE idAerolineas = '%s'" %(idAs)
        aviones = avionCon.ejecutar_SQL(query)
        numberA = avionCon.numberResult(query)
        self.tb_aviones.setRowCount(numberA)
        i = 0
        for avion in aviones:
            self.tb_aviones.setItem(i, 0, QTableWidgetItem(avion[0]))
            self.tb_aviones.setItem(i, 1, QTableWidgetItem(avion[1]))
            self.tb_aviones.setItem(i, 2, QTableWidgetItem(avion[2]))
            self.tb_aviones.setItem(i, 3, QTableWidgetItem(str(avion[3])))
            i += 1
        avionCon.cerrar_conexion()

    def CBUpdate(self):
        self.cb_tipo.addItem("Pasajeros")
        self.cb_tipo.addItem("Carga")
        self.cb_tipoPr.addItem("Helices")
        self.cb_tipoPr.addItem("Turbina")
        self.cb_tipoPr.addItem("Reaccion")

    def AvionRegM(self):
        if self.validacion() == False:
            Dialog("Campos Vacios")
            return False
        Id = self.le_id.text()
        modelo = self.le_modelo.text()
        peso =  self.le_peso.text()
        capacidad = self.le_Capacidad.text()
        numMot = int(self.le_numMot.text())
        area = int(self.le_area.text())
        descripcion = self.tx_descripcion.toPlainText()
        tipo = self.cb_tipo.currentText()
        tipoPro = self.cb_tipoPr.currentText()

        AvionR = Conexion()
        Valid = AvionR.numberResult("SELECT * FROM Aviones WHERE idAvion = '%s'" %(Id))
        if Valid == 0:
            idA = AvionR.ejecutar_SQL("SELECT idAerolineas FROM Aerolineas WHERE NombreAerolinea = '%s'" %(self.Aerolinea))
            idAerolinea = idA.fetchall()
            idAs = int(idAerolinea[0][0])
            insert = "INSERT INTO Aviones (idAvion, modelo, peso_nominal, tipo, tipoPropulsion, num_motores, capacidad, descripcion, area, idAerolineas)"
            insert = insert+ "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(Id, modelo, peso, tipo, tipoPro, numMot, capacidad, descripcion, area, idAs)
            AvionR.insertarDatos(insert)
            self.le_id.clear()
            self.le_modelo.clear()
            self.le_peso.clear()
            self.le_Capacidad.clear()
            self.le_numMot.clear()
            self.le_area.clear()
            self.tx_descripcion.setText("")
            Dialog2("El avion se registro \n correctamente")
        else:
            Dialog("El id ya esta en uso")
        AvionR.cerrar_conexion()
        self.cargarTable()
    
    def AvionDelM(self):
        idDel = self.tb_aviones.selectedIndexes()[0].data()
        delA = Conexion()
        status = delA.numberResult("SELECT * FROM Reservas WHERE idAvion = '%s'" %(idDel))
        if status == 0:
            delA.insertarDatos("DELETE FROM Aviones WHERE idAvion = '%s'" %(idDel))
            Dialog2("El avion se elimino \n correctamente")
        else:
            Dialog("no se puede eliminar \n este avion")
        delA.cerrar_conexion
        self.cargarTable()
    
    def validacion(self):
        count = 0
        if not self.le_id.text().strip():
            count += 1
        if not self.le_modelo.text().strip():
            count += 1
        if not self.le_peso.text().strip():
            count += 1
        if not self.le_Capacidad.text().strip():
            count += 1
        if not self.le_numMot.text().strip():
            count += 1
        if not self.le_area.text().strip():
            count += 1
        if count == 0:
            return True
        return False

        
        