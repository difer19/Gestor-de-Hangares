from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class AerolineaRegister(QWidget):
    def __init__(self, parent = None):
        super(AerolineaRegister, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\AerolineaRegister.ui', self)
        self.le_nombreAerolinea = self.findChild(QLineEdit, 'lineEdit_2')
        self.btn_Register = self.findChild(QPushButton, 'pushButton')

        self.btn_Register.clicked.connect(lambda: self.RegistrarAerolinea())

    def RegistrarAerolinea(self):
        nombre = self.le_nombreAerolinea.text().lower()
        Register = Conexion()
        Id = Register.numberResult("SELECT * FROM "+"Aerolineas") + 1
        query = "SELECT * FROM Aerolineas WHERE NombreAerolinea = '%s'" %(nombre)
        if Register.numberResult(query) == 0:
            insert = "INSERT INTO Aerolineas (idAerolineas, NombreAerolinea) VALUES ('%s','%s');" %(Id, nombre)
            Register.insertarDatos(insert)
            self.le_nombreAerolinea.clear()
        else:
            print("Aerolinea ya esta en la bd")
        Register.cerrar_conexion()


        

