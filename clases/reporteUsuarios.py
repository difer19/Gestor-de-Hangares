from PyQt5.QtWidgets import QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class ReporteUsuarios(QWidget):
    def __init__(self, parent = None):
        super(ReporteUsuarios, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReporteUsuarios.ui', self)
        self.btn_rep = self.findChild(QPushButton, 'pushButton')
        self.btn_rep2 = self.findChild(QPushButton, 'pushButton_2')
        self.tb_rep = self.findChild(QTableWidget, 'tableWidget')
        self.tb_rep2 = self.findChild(QTableWidget, 'tableWidget_2')
        self.cb_aerolineas = self.findChild(QComboBox, 'comboBox')

        self.cargarCB()

        self.btn_rep.clicked.connect(lambda: self.genRep())
        self.btn_rep2.clicked.connect(lambda: self.genRep2())
    
    def cargarCB(self):
        self.cb_aerolineas.clear()
        self.cb_aerolineas.addItem("General")
        self.cb_aerolineas.addItem("Aeropuerto el Campanero")
        aerolineas = Conexion()
        cursor = aerolineas.ejecutar_SQL("SELECT NombreAerolinea FROM Aerolineas")
        for Aerolinea in cursor.fetchall():
            self.cb_aerolineas.addItem(Aerolinea[0])
        aerolineas.cerrar_conexion()


    def genRep(self):
        if self.cb_aerolineas.currentText() == "General":
            usuariosCon = Conexion()
            query = ("SELECT * FROM users")
            usuarios = usuariosCon.ejecutar_SQL(query)
            number = usuariosCon.numberResult(query)
            usuariosCon.cerrar_conexion()
        elif self.cb_aerolineas.currentText() == "Aeropuerto el Campanero":
            usuariosCon = Conexion()
            query = ("SELECT * FROM users where afiliacion = 'aeropuerto el campanero'")
            usuarios = usuariosCon.ejecutar_SQL(query)
            number = usuariosCon.numberResult(query)
            usuariosCon.cerrar_conexion()
        else:
            usuariosCon = Conexion()
            query = ("SELECT * FROM users where afiliacion = '%s'")%(self.cb_aerolineas.currentText())
            usuarios = usuariosCon.ejecutar_SQL(query)
            number = usuariosCon.numberResult(query)
            usuariosCon.cerrar_conexion()
        self.tb_rep.setRowCount(number)
        i = 0
        for usuario in usuarios:
            self.tb_rep.setItem(i, 0, QTableWidgetItem(str(usuario[0])))
            self.tb_rep.setItem(i, 1, QTableWidgetItem(str(usuario[1])))
            self.tb_rep.setItem(i, 2, QTableWidgetItem(str(usuario[3])))
            self.tb_rep.setItem(i, 3, QTableWidgetItem(str(usuario[4])))
            i += 1
    

    def genRep2(self):
        usuariosCon2 = Conexion()
        query = ("""
                    SELECT afiliacion, count(afiliacion) as numero FROM users group by 1
                    union select 'Total' as afiliacion, sum(T1.numero) as numero from
                    (SELECT afiliacion, count(afiliacion) as numero FROM users group by 1) as T1;
                """)
        aerolineas = usuariosCon2.ejecutar_SQL(query)
        number2 = usuariosCon2.numberResult(query)
        usuariosCon2.cerrar_conexion
        self.tb_rep2.setRowCount(number2)
        i = 0
        for aerolinea in aerolineas:
            self.tb_rep2.setItem(i, 0, QTableWidgetItem(str(aerolinea[0])))
            self.tb_rep2.setItem(i, 1, QTableWidgetItem(str(aerolinea[1])))
            i += 1
