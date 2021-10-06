from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton, QWidget 
from PyQt5 import uic
from database.conexion import Conexion
from clases.dialog import *


class HangarData(QWidget):
    def __init__(self, parent = None):
        super(HangarData, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\HangarDatos.ui', self)
        self.le_idHangar = self.findChild(QLineEdit, 'lineEdit')
        self.le_Capacidad = self.findChild(QLineEdit, 'lineEdit_2')
        self.le_Ubicacion = self.findChild(QLineEdit,'lineEdit_3')
        self.btn_HangarV = self.findChild(QPushButton, 'pushButton')
        self.btn_HangarM = self.findChild(QPushButton, 'pushButton_3')
        self.btn_Save = self.findChild(QPushButton, 'pushButton_2')
        self.cb_hangares = self.findChild(QComboBox, 'comboBox')

        self.le_Capacidad.setValidator(QIntValidator())

        self.le_idHangar.setEnabled(False)
        self.le_Capacidad.setEnabled(False)
        self.le_Ubicacion.setEnabled(False)

        self.cargarCB()

        self.btn_HangarV.clicked.connect(lambda: self.hangarVis())
        self.btn_HangarM.clicked.connect(lambda: self.hangarMod())
        self.btn_Save.clicked.connect(lambda: self.hangarSave())

    def cargarCB(self):
        self.cb_hangares.clear()
        hangarCon = Conexion()
        idH = hangarCon.ejecutar_SQL("SELECT idHangar FROM Hangares") 
        for hangar in idH.fetchall():
            self.cb_hangares.addItem(hangar[0])
        hangarCon.cerrar_conexion()
    
    def hangarVis(self):
        hangarCon = Conexion()
        idH = hangarCon.ejecutar_SQL("SELECT * FROM Hangares WHERE idHangar = '%s'" %(self.cb_hangares.currentText()))
        datos = idH.fetchall()
        self.le_idHangar.setText(datos[0][0])
        self.le_Capacidad.setText(str(datos[0][1]))
        self.le_Ubicacion.setText(datos[0][2]) 
        hangarCon.cerrar_conexion()

    def hangarMod(self):
        if self.le_Capacidad.isEnabled() == False:
            self.le_Capacidad.setEnabled(True)
            self.le_Ubicacion.setEnabled(True)
            self.btn_HangarM.setText("Cancelar Modificacion")
        else:
            self.le_Capacidad.setEnabled(False)
            self.le_Ubicacion.setEnabled(False)
            self.hangarVis()
            self.btn_HangarM.setText("Modificar Datos")
        
    def hangarSave(self):
        if self.validacion() == False:
            Dialog(" Campos Vacios ")
            return False
        hangarCon = Conexion()
        query = "UPDATE Hangares SET Capacidad = '%s', Ubicacion = '%s' WHERE idHangar = '%s'"%(int(self.le_Capacidad.text()), self.le_Ubicacion.text(), self.le_idHangar.text())
        hangarCon.insertarDatos(query)
        hangarCon.cerrar_conexion()
        Dialog2("Modificacion Exitosa")
        self.hangarMod()

    def validacion(self):
        count = 0
        if not self.le_Capacidad.text().strip():
            count += 1
        if not self.le_Ubicacion.text().strip():
            count += 1
        if count == 0:
            return True
        return False


        
