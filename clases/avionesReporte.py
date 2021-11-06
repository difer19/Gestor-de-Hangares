from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class ReporteAviones(QWidget):
    def __init__(self, Aerolinea, parent = None):
        super(ReporteAviones, self).__init__(parent)
        self.iniciarGui()
        self.Aerolinea = Aerolinea
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReporteAviones.ui', self)
        self.btn_rep = self.findChild(QPushButton, 'pushButton')
        self.tb_rep = self.findChild(QTableWidget, 'tableWidget')

        self.btn_rep.clicked.connect(lambda: self.genRep())
    
    def genRep(self):
        avionesCon = Conexion()
        query = ("""SELECT * FROM Aviones join Aerolineas on Aviones.IdAerolineas = Aerolineas.idAerolineas
                where NombreAerolinea = '%s' """)%(self.Aerolinea)
        aviones = avionesCon.ejecutar_SQL(query)
        number = avionesCon.numberResult(query)
        self.tb_rep.setRowCount(number)
        i = 0
        for avion in aviones:
            self.tb_rep.setItem(i, 0, QTableWidgetItem(str(avion[0])))
            self.tb_rep.setItem(i, 1, QTableWidgetItem(str(avion[1])))
            self.tb_rep.setItem(i, 2, QTableWidgetItem(str(avion[2])))
            self.tb_rep.setItem(i, 3, QTableWidgetItem(str(avion[3])))
            self.tb_rep.setItem(i, 4, QTableWidgetItem(str(avion[4])))
            self.tb_rep.setItem(i, 5, QTableWidgetItem(str(avion[5])))
            self.tb_rep.setItem(i, 6, QTableWidgetItem(str(avion[6])))
            self.tb_rep.setItem(i, 7, QTableWidgetItem(str(avion[7])))
            self.tb_rep.setItem(i, 8, QTableWidgetItem(str(avion[8])))
            i += 1
        avionesCon.cerrar_conexion()