# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReporteAerolineas.ui'
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
        Form.resize(1056, 647)
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.pushButton)

        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(500, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(167, 40))

        self.verticalLayout_2.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.tableWidget_2 = QTableWidget(self.widget)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tableWidget_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Reporte de Aerolineas", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Aerolineas", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Generar / Actualizar Reporte", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Aerolinea", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Aerolinea", None));
        self.label_3.setText(QCoreApplication.translate("Form", u"Reporte de Estadisticas", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Generar / Actualizar Reporte", None))
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Aerolinea", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Cantidad / Valor", None));
    # retranslateUi

