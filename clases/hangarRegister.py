from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget
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

        self.btn_HangarR.clicked.connect(lambda: self.RegistrarHangar())
    
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