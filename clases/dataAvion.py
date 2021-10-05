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
        self.cb_avion = self.findChild(QComboBox, 'comboBox')
        self.le_id = self.findChild(QLineEdit, 'lineEdit')
        self.le_modelo = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_peso = self.findChild(QLineEdit, 'lineEdit_3')
        self.le_Capacidad = self.findChild(QLineEdit, 'lineEdit_5')
        self.le_numMot = self.findChild(QLineEdit, 'lineEdit_6')
        self.le_area = self.findChild(QLineEdit, 'lineEdit_4')
        self.cb_tipo = self.findChild(QComboBox, 'comboBox_2')
        self.cb_tipoPr = self.findChild(QComboBox, 'comboBox_3')
        self.btn_vis = self.findChild(QPushButton, 'pushButton')
        self.btn_mod = self.findChild(QPushButton, 'pushButton_3')
        self.btn_save = self.findChild(QPushButton, 'pushButton_2')

        self.le_peso.setValidator(QIntValidator())
        self.le_Capacidad.setValidator(QIntValidator())
        self.le_numMot.setValidator(QIntValidator())
        self.le_area.setValidator(QIntValidator())
        
        self.le_id.setEnabled(False)
        self.le_modelo.setEnabled(False)
        self.le_peso.setEnabled(False)
        self.le_Capacidad.setEnabled(False)
        self.le_numMot.setEnabled(False)
        self.le_area.setEnabled(False)
        self.cb_tipo.setEnabled(False)
        self.cb_tipoPr.setEnabled(False)

        self.cargarCB()
        self.CBUpdate()

        self.btn_vis.clicked.connect(lambda: self.avionVis())
        self.btn_mod.clicked.connect(lambda: self.avionMod())
        self.btn_save.clicked.connect(lambda: self.avionSave())
    
    def CBUpdate(self):
        self.cb_tipo.addItem("Pasajeros")
        self.cb_tipo.addItem("Carga")
        self.cb_tipoPr.addItem("Helices")
        self.cb_tipoPr.addItem("Turbina")
        self.cb_tipoPr.addItem("Reaccion")

    def cargarCB(self):
        self.cb_avion.clear()
        avionCon = Conexion()
        idA = avionCon.ejecutar_SQL("SELECT idAvion FROM Aerolineas JOIN Aviones ON Aviones.idAerolineas = Aerolineas.idAerolineas WHERE NombreAerolinea = '%s'"%(self.Aerolinea))
        for avion in idA.fetchall():
            self.cb_avion.addItem(avion[0])
        avionCon.cerrar_conexion()
    
    def avionVis(self):
        avionCon = Conexion()
        avion = avionCon.ejecutar_SQL("SELECT * FROM Aviones WHERE idAvion = '%s'" %(self.cb_avion.currentText()))
        datos = avion.fetchall()
        self.le_id.setText(str(datos[0][0]))
        self.le_modelo.setText(str(datos[0][1]))
        self.le_peso.setText(str(datos[0][2]))
        self.le_Capacidad.setText(str(datos[0][6]))
        self.le_numMot.setText(str(datos[0][8]))
        self.le_area.setText(str(datos[0][5]))
        self.cb_tipo.setCurrentText(str(datos[0][3]))
        self.cb_tipoPr.setCurrentText(str(datos[0][4]))
        avionCon.cerrar_conexion()
    
    def avionMod(self):
        if self.le_modelo.isEnabled() == False:
            self.le_modelo.setEnabled(True)
            self.le_peso.setEnabled(True)
            self.le_Capacidad.setEnabled(True)
            self.le_numMot.setEnabled(True)
            self.le_area.setEnabled(True)
            self.cb_tipo.setEnabled(True)
            self.cb_tipoPr.setEnabled(True)
            self.btn_mod.setText("Cancelar Modificacion")
        else:
            self.le_modelo.setEnabled(False)
            self.le_peso.setEnabled(False)
            self.le_Capacidad.setEnabled(False)
            self.le_numMot.setEnabled(False)
            self.le_area.setEnabled(False)
            self.cb_tipo.setEnabled(False)
            self.cb_tipoPr.setEnabled(False)
            self.btn_mod.setText("Modificar Datos")
            self.avionVis()
    
    def avionSave(self):
        if self.validacion() == False:
            Dialog("Campos Vacios")
            return False
        avionCon = Conexion()
        query = """
                    UPDATE Aviones SET modelo = '%s', peso_nominal = '%s', tipo = '%s', tipoPropulsion = '%s'
                    , num_motores = '%s', capacidad = '%s', area = '%s' WHERE idAvion = '%s'
                """%(self.le_modelo.text(), int(self.le_peso.text()), self.cb_tipo.currentText(), self.cb_tipoPr.currentText(), int(self.le_area.text()), int(self.le_Capacidad.text()), int(self.le_numMot.text()), self.cb_avion.currentText())
        avionCon.insertarDatos(query)
        self.avionMod()
        Dialog2("Modificion exitosa")

    def validacion(self):
        count = 0
        if not self.le_modelo.text().strip():
            count += 1
        if not self.le_peso.text().strip():
            count += 1
        if not self.le_Capacidad.text().strip():
            count += 1
        if not self.le_numMot.text().strip():
            count += 1
        if not self.le_area.text().strip():
            count += 1
        if count == 0:
            return True
        return False
