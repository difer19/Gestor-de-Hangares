from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class ReporteHangares(QWidget):
    def __init__(self, parent = None):
        super(ReporteHangares, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\ReporteHangares.ui', self)
        self.btn_rep = self.findChild(QPushButton, 'pushButton')
        self.tb_rep = self.findChild(QTableWidget, 'tableWidget')

        self.btn_rep.clicked.connect(lambda: self.genRep())

    def genRep(self):
        hangarCon = Conexion()
        hangares = hangarCon.ejecutar_SQL("""
                                select Hangares.idHangar, Capacidad, Ubicacion, 
                                count(Hangares.idHangar) as Reservas from Hangares join Reservas on Hangares.idHangar = Reservas.idhangar
                                group by 1
                                union select 'Total' AS idHangar, sum(T1.Capacidad) as Capacidad, '' as Ubicacion, sum(T1.Reservas) as Reservas
                                from (select Hangares.idHangar, Capacidad, Ubicacion, count(Hangares.idHangar) as Reservas 
                                from Hangares join Reservas on Hangares.idHangar = Reservas.idhangar group by 1) as T1 """)
        numberH = hangarCon.numberResult("""
                                select Hangares.idHangar, Capacidad, Ubicacion, 
                                count(Hangares.idHangar) as Reservas from Hangares join Reservas on Hangares.idHangar = Reservas.idhangar
                                group by 1
                                union select 'Total' AS idHangar, sum(T1.Capacidad) as Capacidad, '' as Ubicacion, sum(T1.Reservas) as Reservas
                                from (select Hangares.idHangar, Capacidad, Ubicacion, count(Hangares.idHangar) as Reservas 
                                from Hangares join Reservas on Hangares.idHangar = Reservas.idhangar group by 1) as T1 """)
        
        self.tb_rep.setRowCount(numberH)
        i = 0
        for hangar in hangares:
            self.tb_rep.setItem(i, 0, QTableWidgetItem(hangar[0]))
            self.tb_rep.setItem(i, 1, QTableWidgetItem(str(hangar[1])))
            self.tb_rep.setItem(i, 2, QTableWidgetItem(hangar[2]))
            self.tb_rep.setItem(i, 3, QTableWidgetItem(str(hangar[3])))
            i += 1
        hangarCon.cerrar_conexion()
