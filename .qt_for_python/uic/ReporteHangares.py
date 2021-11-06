# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReporteHangares.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1086, 626)
        Form.setStyleSheet(u"QWidget\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: #6357B7;\n"
"    border-radius: 15px;\n"
"    font: 14pt \"Bahnschrift\";\n"
"}\n"
"\n"
"QPushButton:Pressed\n"
"{\n"
"    background-color: #C397E4;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    color: #6357B7;\n"
"    background-color: white;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    color: #6357B7;\n"
"    background-color: white;\n"
"    border : 2px solid #6357B7;\n"
"    border-radius: 15px;\n"
"    font: 10pt \"Bahnschrift\";\n"
"    border: 1px solid #6357B7;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #6357B7;\n"
"    font: 12pt \"Bahnschrift\";\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    border: 1px solid #6357B7;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	color: #6357B7;\n"
"    font: 12pt \"Bahnschrift\";\n"
"}\n"
""
                        "\n"
"QTextEdit\n"
"{\n"
"    color: #6357B7;\n"
"    background-color: white;\n"
"    border : 2px solid #6357B7;\n"
"    border-radius: 15px;\n"
"    font: 14pt \"Bahnschrift\";\n"
"    border: 1px solid #6357B7;\n"
"    padding: 13px;\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"	color: #6357B7;\n"
"    font: 12pt \"Bahnschrift\";\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 40))

        self.verticalLayout.addWidget(self.pushButton)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Reporte de Hangares", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Generar / Actualizar Reporte", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Hangar", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Capacidad", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Ubicacion", None));
    # retranslateUi

