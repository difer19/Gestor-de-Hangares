from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QWidget, QTableWidgetItem
from PyQt5 import uic
from database.conexion import Conexion


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
            self.tb_hangares.setItem(i, 3, QTableWidgetItem(hangar[3]))
            i += 1
        hangarCon.cerrar_conexion()

    def RegistrarHangar(self):
        idHangar = self.le_idHangar.text()
        Capacidad = int(self.le_Capacidad.text())
        Ubicacion = str(self.le_Ubicacion.text())
        HangarR = Conexion()
        valid = HangarR.numberResult("SELECT idHangar FROM Hangares WHERE idHangar = '%s' or Ubicacion = '%s'" %(idHangar, Ubicacion)) 
        if valid == 0:
            insert = "INSERT INTO Hangares (idHangar, Capacidad, Ubicacion, Estado) VALUES ('%s', '%s', '%s', '%s')" %(idHangar, Capacidad, Ubicacion, "Libre")
            HangarR.insertarDatos(insert)
            self.le_idHangar.clear()
            self.le_Capacidad.clear()
            self.le_Ubicacion.clear()
        else:
            print("datos no validos")
        HangarR.cerrar_conexion()
        self.cargarTable()
    
    def EliminarHangar(self):
        idDel = self.tb_hangares.selectedIndexes()[0].data()
        status = self.tb_hangares.selectedIndexes()[3].data()
        if status == "Ocupado":
            print("no se puede eliminar este hangar")
        else:
            delU = Conexion()
            delU.insertarDatos("DELETE FROM Hangares WHERE idHangar = '%s'" %(idDel))
            delU.cerrar_conexion
        self.cargarTable()
        