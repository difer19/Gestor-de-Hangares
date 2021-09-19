from PyQt5.QtWidgets import QLineEdit, QPushButton, QTableWidget, QWidget, QTableWidgetItem
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *


class AerolineaRegister(QWidget):
    def __init__(self, parent = None):
        super(AerolineaRegister, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\AerolineaRegister.ui', self)
        self.le_nombreAerolinea = self.findChild(QLineEdit, 'lineEdit_2')
        self.btn_Register = self.findChild(QPushButton, 'pushButton')
        self.tb_aerolineas = self.findChild(QTableWidget, 'tableWidget')
        self.btn_DelAe = self.findChild(QPushButton, 'pushButton_2')

        self.cargarTable()

        self.btn_Register.clicked.connect(lambda: self.RegistrarAerolinea())
        self.btn_DelAe.clicked.connect(lambda: self.EliminarAerolinea())

    def cargarTable(self):
        aeroCon = Conexion()
        aerolineas = aeroCon.ejecutar_SQL("SELECT * FROM Aerolineas")
        numberA = aeroCon.numberResult("SELECT * FROM Aerolineas")
        self.tb_aerolineas.setRowCount(numberA)
        i = 0
        for aerolinea in aerolineas:
            self.tb_aerolineas.setItem(i, 0, QTableWidgetItem(str(aerolinea[0])))
            self.tb_aerolineas.setItem(i, 1, QTableWidgetItem(aerolinea[1]))
            i += 1
        aeroCon.cerrar_conexion()

    def RegistrarAerolinea(self):
        if not self.le_nombreAerolinea.text().strip():
            Dialog("Campos Vacios")
            return False
        nombre = self.le_nombreAerolinea.text().strip().lower()
        Register = Conexion()
        Id = Register.numberResult("SELECT * FROM "+"Aerolineas") + 1
        query = "SELECT * FROM Aerolineas WHERE NombreAerolinea = '%s'" %(nombre)
        if Register.numberResult(query) == 0:
            insert = "INSERT INTO Aerolineas (idAerolineas, NombreAerolinea) VALUES ('%s','%s');" %(Id, nombre)
            Register.insertarDatos(insert)
            self.le_nombreAerolinea.clear()
            Dialog2("La aerolinea se \n ingreso exitosamente")
        else:
            Dialog("Esta aerolinea ya esta \n en la base de datos")
        Register.cerrar_conexion()
        self.cargarTable()
    
    def EliminarAerolinea(self):
        # Eliminar una aerolinea conlleva eliminar todos sus usuarios, aviones asociados
        if self.tb_aerolineas.selectedIndexes() == []:
            return False
        idDel = self.tb_aerolineas.selectedIndexes()[0].data()
        nameDel = self.tb_aerolineas.selectedIndexes()[1].data()
        delA = Conexion()
        delA.insertarDatos("DELETE FROM Aerolineas WHERE idAerolineas = '%s'" %(idDel))
        delA.insertarDatos("DELETE FROM users WHERE afiliacion = '%s'" %(nameDel))
        delA.insertarDatos("DELETE FROM Aviones WHERE IdAerolineas = '%s'" %(idDel))
        delA.cerrar_conexion()
        self.cargarTable()
        Dialog2("La aerolinea se \n elimino exitosamente")

        


        

