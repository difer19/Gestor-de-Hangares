from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QWidget 
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *


class AvionData(QWidget):
    def __init__(self,  Aerolinea, parent = None):
        super(AvionData, self).__init__(parent)
        self.Aerolinea = Aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\AvionDatos.ui', self)