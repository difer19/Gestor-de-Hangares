from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion 


class PagarRe(QWidget):
    def __init__(self, parent = None):
        super(PagarRe, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        self.update()
        uic.loadUi(r'GUI\Resources\UI\PagarRe.ui', self)