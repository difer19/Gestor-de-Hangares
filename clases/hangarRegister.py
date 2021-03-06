from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QWidget, QTableWidgetItem
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *
from PyQt5.QtGui import QIntValidator

class HangarRegister(QWidget):
    def __init__(self, parent = None):
        super(HangarRegister, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\HangarRegister.ui', self)
        self.le_idHangar = self.findChild(QLineEdit, 'lineEdit')
        self.le_Capacidad = self.findChild(QLineEdit, 'lineEdit_4')
        self.le_Ubicacion = self.findChild(QLineEdit,'lineEdit_2')
        self.btn_HangarR = self.findChild(QPushButton, 'pushButton')
        self.tb_hangares = self.findChild(QTableWidget, 'tableWidget')
        self.btn_delHangar = self.findChild(QPushButton, 'pushButton_2')
        self.le_Capacidad.setValidator(QIntValidator())
        
        self.cargarTable()

        self.btn_HangarR.clicked.connect(lambda: self.RegistrarHangar())
        self.btn_delHangar.clicked.connect(lambda: self.EliminarHangar())
    
    def cargarTable(self):
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

    def RegistrarHangar(self):
        if self.validacion() == False:
            Dialog("Campos Vacios")
            return False
        idHangar = self.le_idHangar.text().strip()
        Capacidad = int(self.le_Capacidad.text())
        Ubicacion = str(self.le_Ubicacion.text())
        HangarR = Conexion()
        valid = HangarR.numberResult("SELECT idHangar FROM Hangares WHERE idHangar = '%s' or Ubicacion = '%s'" %(idHangar, Ubicacion)) 
        if valid == 0:
            insert = "INSERT INTO Hangares (idHangar, Capacidad, Ubicacion) VALUES ('%s', '%s', '%s')" %(idHangar, Capacidad, Ubicacion)
            HangarR.insertarDatos(insert)
            self.le_idHangar.clear()
            self.le_Capacidad.clear()
            self.le_Ubicacion.clear()
            Dialog2("Hangar registrado \n correctamente")
        else:
            Dialog("Los datos no \n son validos")
        HangarR.cerrar_conexion()
        self.cargarTable()
    
    def EliminarHangar(self):
        if self.tb_hangares.selectedIndexes() == []:
            return False
        idDel = self.tb_hangares.selectedIndexes()[0].data()
        status = self.statusHangar(idDel)
        if status == False:
            Dialog("no se puede eliminar \n este hangar")
        else:
            delU = Conexion()
            delU.insertarDatos("DELETE FROM Hangares WHERE idHangar = '%s'" %(idDel))
            delU.cerrar_conexion
            Dialog2("El hangar ha sido \n eliminado")
        self.cargarTable()
    
    def statusHangar(self, idHangar):
        stat = Conexion()
        query = "SELECT * FROM Reservas WHERE idhangar = '%s'" %(idHangar)
        numberH = stat.numberResult(query)
        stat.cerrar_conexion()
        if numberH == 0:
            return True
        else:
            return False 
    
    def validacion(self):
        count = 0
        if not self.le_idHangar.text().strip():
            count += 1
        if not self.le_Capacidad.text().strip():
            count += 1
        if not self.le_Ubicacion.text().strip():
            count += 1
        if count == 0:
            return True
        return False
        