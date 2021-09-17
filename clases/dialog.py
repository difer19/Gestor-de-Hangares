from PyQt5.QtWidgets import QLabel, QDialog
from PyQt5 import uic


class Dialog(QDialog):
    def __init__(self, text):
        super(Dialog, self).__init__()
        self.setWindowTitle("Error")
        self.text = text
        self.cargarUi()
        self.exec()
    
    def cargarUi(self):
        uic.loadUi(r'GUI\Resources\UI\Dialog.ui', self)
        self.lb_message = self.findChild(QLabel, 'label_2')
        self.lb_message.setText(self.text)
    
class Dialog2(QDialog):
    def __init__(self, text):
        super(Dialog2, self).__init__()
        self.setWindowTitle("")
        self.text = text
        self.cargarUi()
        self.exec()
    
    def cargarUi(self):
        uic.loadUi(r'GUI\Resources\UI\Dialog2.ui', self)
        self.lb_message = self.findChild(QLabel, 'label_2')
        self.lb_message.setText(self.text)