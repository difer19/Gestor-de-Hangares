from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QWidget 
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *


class AerolineaData(QWidget):
    def __init__(self, parent = None):
        super(AerolineaData, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\aerolineaDatos.ui', self)
        self.le_nombreAerolinea = self.findChild(QLineEdit, 'lineEdit')
        self.cb_aerolineas = self.findChild(QComboBox, 'comboBox')
        self.btn_vis = self.findChild(QPushButton, 'pushButton')
        self.btn_mod = self.findChild(QPushButton, 'pushButton_3')
        self.btn_save = self.findChild(QPushButton, 'pushButton_2')

        self.le_nombreAerolinea.setEnabled(False)

        self.cargarCB()
        self.btn_vis.clicked.connect(lambda: self.AerolineaV())
        self.btn_mod.clicked.connect(lambda: self.AerolineaM())
        self.btn_save.clicked.connect(lambda: self.AerolineaSave())
    
    def cargarCB(self):
        self.cb_aerolineas.clear()
        aerolineas = Conexion()
        cursor = aerolineas.ejecutar_SQL("SELECT NombreAerolinea FROM Aerolineas")
        for Aerolinea in cursor.fetchall():
            self.cb_aerolineas.addItem(Aerolinea[0])
        aerolineas.cerrar_conexion()
    
    def AerolineaV(self):
        self.le_nombreAerolinea.setText(self.cb_aerolineas.currentText())
    
    def AerolineaM(self):
        if self.le_nombreAerolinea.isEnabled() == False:
            self.le_nombreAerolinea.setEnabled(True)
            self.btn_mod.setText("Cancelar Modificacion")
        else:
            self.le_nombreAerolinea.setEnabled(False)
            self.btn_mod.setText("Modificar Datos")
            self.AerolineaV()
    
    def AerolineaSave(self):
        if not self.le_nombreAerolinea.text().strip():
            Dialog("Campos Vacios")
            return False
        aeroCon = Conexion()
        query = "UPDATE Aerolineas SET NombreAerolinea = '%s' WHERE NombreAerolinea = '%s'" %(self.le_nombreAerolinea.text(), self.cb_aerolineas.currentText())
        aeroCon.insertarDatos(query)
        self.cargarCB()
        self.AerolineaM()
        Dialog2("Modificion exitosa")

    
    
    
