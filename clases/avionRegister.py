from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QTextEdit, QWidget
from PyQt5 import uic
from database.conexion import Conexion


class AvionRegister(QWidget):
    def __init__(self,  Aerolinea, parent = None):
        super(AvionRegister, self).__init__(parent)
        self.Aerolinea = Aerolinea
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\AvionRegister.ui', self)
        self.le_id = self.findChild(QLineEdit, 'lineEdit')
        self.le_modelo = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_peso = self.findChild(QLineEdit, 'lineEdit_3')
        self.le_Capacidad = self.findChild(QLineEdit, 'lineEdit_6')
        self.le_numMot = self.findChild(QLineEdit, 'lineEdit_5')
        self.le_area = self.findChild(QLineEdit, 'lineEdit_4')
        self.tx_descripcion = self.findChild(QTextEdit, 'textEdit')
        self.cb_tipo = self.findChild(QComboBox, 'comboBox')
        self.cb_tipoPr = self.findChild(QComboBox, 'comboBox_2')
        self.btn_AvionReg = self.findChild(QPushButton, 'pushButton')

        self.CBUpdate()

        self.btn_AvionReg.clicked.connect(lambda: self.AvionRegM())

    def CBUpdate(self):
        self.cb_tipo.addItem("Pasajeros")
        self.cb_tipo.addItem("Carga")
        self.cb_tipoPr.addItem("Helices")
        self.cb_tipoPr.addItem("Turbina")
        self.cb_tipoPr.addItem("Reaccion")

    def AvionRegM(self):
        Id = self.le_id.text()
        modelo = self.le_modelo.text()
        peso =  self.le_peso.text()
        capacidad = self.le_Capacidad.text()
        numMot = int(self.le_numMot.text())
        area = int(self.le_area.text())
        descripcion = self.tx_descripcion.toPlainText()
        tipo = self.cb_tipo.currentText()
        tipoPro = self.cb_tipoPr.currentText()

        AvionR = Conexion()
        Valid = AvionR.numberResult("SELECT * FROM Aviones WHERE idAvion = '%s'" %(Id))
        if Valid == 0:
            idA = AvionR.ejecutar_SQL("SELECT idAerolineas FROM Aerolineas WHERE NombreAerolinea = '%s'" %(self.Aerolinea))
            idAerolinea = idA.fetchall()
            idAs = int(idAerolinea[0][0])
            insert = "INSERT INTO Aviones (idAvion, modelo, peso_nominal, tipo, tipoPropulsion, num_motores, capacidad, descripcion, area, idAerolineas)"
            insert = insert+ "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(Id, modelo, peso, tipo, tipoPro, numMot, capacidad, descripcion, area, idAs)
            AvionR.insertarDatos(insert)
            self.le_id.clear()
            self.le_modelo.clear()
            self.le_peso.clear()
            self.le_Capacidad.clear()
            self.le_numMot.clear()
            self.le_area.clear()
            self.tx_descripcion.setText("")
        else:
            print("ID ya esta en uso")
        AvionR.cerrar_conexion()

        
        