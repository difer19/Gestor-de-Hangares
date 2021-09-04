from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.uic.uiparser import QtWidgets

class HangarRegister(QWidget):
    def __init__(self, parent = None):
        super(HangarRegister, self).__init__(parent)
        self.iniciarGui()
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'GUI\Resources\UI\HangarRegister.ui', self)