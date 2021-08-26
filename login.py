from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5 import uic
import sys

from PyQt5.uic.uiparser import QtWidgets

class PantallaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciarGui()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\PantallaInicial_UI.ui', self)
        self.w1 = self.findChild(QWidget, "form_widget")
        self.w2 = self.findChild(QWidget, "Logo_Widget")
        uic.loadUi(r'GUI\Resources\UI\Login_UI.ui', self.w1)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaInicial()
    app.exec_()