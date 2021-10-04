from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget
from PyQt5 import uic
from clases.userRegister import UserRegister 


class Usuarios(QWidget):
    def __init__(self, parent = None):
        super(Usuarios, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\Usuarios.ui', self)
        self.btn_RE = self.findChild(QPushButton, 'RegistrarUsuario')
        self.btn_datos = self.findChild(QPushButton, 'DatosUsuario')
        self.btn_reporte = self.findChild(QPushButton, 'ReporteUsuarios')
        self.main = self.findChild(QStackedWidget, 'stackedWidget')

        self.UserR = UserRegister()
        
        self.main.addWidget(QWidget())
        self.main.addWidget(self.UserR)
        self.main.addWidget(QWidget())
        self.main.addWidget(QWidget())
        
        self.btn_RE.clicked.connect(self.REb)
        self.btn_datos.clicked.connect(self.datosB)
        self.btn_reporte.clicked.connect(self.reporteB)
    
    def reload(self):
        self.main.widget(1).cb_afiliacion.clear()
        self.main.widget(1).cargarCB()
        self.main.widget(1).cargarTable()
    
    def REb(self):
        self.btn_RE.setEnabled(False)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(1)
        
    def datosB(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(False)
        self.btn_reporte.setEnabled(True)
        self.main.setCurrentIndex(2)
    
    def reporteB(self):
        self.main.currentWidget().destroy()
        self.btn_RE.setEnabled(True)
        self.btn_datos.setEnabled(True)
        self.btn_reporte.setEnabled(False)
        self.main.setCurrentIndex(3)