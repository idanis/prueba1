# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_V2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DiagnosticoCovid19(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(615, 521)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 571, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.loading = QtWidgets.QLabel(self.tab)
        self.loading.setEnabled(True)
        self.loading.setGeometry(QtCore.QRect(320, 220, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loading.setFont(font)
        self.loading.setObjectName("loading")
        self.labelPregunta = QtWidgets.QLabel(self.tab)
        self.labelPregunta.setGeometry(QtCore.QRect(10, 170, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPregunta.setFont(font)
        self.labelPregunta.setObjectName("labelPregunta")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 50, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelPregunta_2 = QtWidgets.QLabel(self.tab)
        self.labelPregunta_2.setGeometry(QtCore.QRect(10, 30, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPregunta_2.setFont(font)
        self.labelPregunta_2.setObjectName("labelPregunta_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 80, 231, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sexo = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sexo.setObjectName("sexo")
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sexo)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(280, 80, 261, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.edad = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.edad.setObjectName("edad")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edad)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.enviar = QtWidgets.QPushButton(self.tab)
        self.enviar.setEnabled(True)
        self.enviar.setGeometry(QtCore.QRect(320, 310, 161, 41))
        self.enviar.setCheckable(True)
        self.enviar.setAutoDefault(False)
        self.enviar.setObjectName("enviar")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 251, 211))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.fiebre = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fiebre.setFont(font)
        self.fiebre.setChecked(False)
        self.fiebre.setObjectName("fiebre")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.fiebre)
        self.tos = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tos.setFont(font)
        self.tos.setObjectName("tos")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.tos)
        self.dificultad_respiratoria = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.dificultad_respiratoria.setObjectName("dificultad_respiratoria")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.dificultad_respiratoria)
        self.fatiga = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.fatiga.setObjectName("fatiga")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.fatiga)
        self.odinofagia = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.odinofagia.setObjectName("odinofagia")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.odinofagia)
        self.dolor_cabeza = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.dolor_cabeza.setObjectName("dolor_cabeza")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.dolor_cabeza)
        self.rinorrea = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.rinorrea.setObjectName("rinorrea")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.rinorrea)
        self.diarrea = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.diarrea.setObjectName("diarrea")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.diarrea)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(10, 190, 541, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtWidgets.QWidget()
        #self.tab_2.setObjectName("tab_2")
        #self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Diagnostico COVID"))
        self.loading.setText(_translate("Dialog", ""))
        self.labelPregunta.setText(_translate("Dialog", "¿Presenta algunos de estos sintomas?"))
        self.labelPregunta_2.setText(_translate("Dialog", "Caracterizacion"))
        self.sexo.setItemText(0, _translate("Dialog", "Femenino"))
        self.sexo.setItemText(1, _translate("Dialog", "Masculino"))
        self.label.setText(_translate("Dialog", "Sexo"))
        self.label_2.setText(_translate("Dialog", "Edad"))
        self.enviar.setText(_translate("Dialog", "Diagnosticar"))
        self.fiebre.setText(_translate("Dialog", "Fiebre"))
        self.tos.setText(_translate("Dialog", "Tos"))
        self.dificultad_respiratoria.setText(_translate("Dialog", "Dificultad Respiratoria"))
        self.fatiga.setText(_translate("Dialog", "Fatiga"))
        self.odinofagia.setText(_translate("Dialog", "Odinofagia"))
        self.dolor_cabeza.setText(_translate("Dialog", "Dolor de cabeza"))
        self.rinorrea.setText(_translate("Dialog", "Rinorrea"))
        self.diarrea.setText(_translate("Dialog", "Diarrea"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Caracterización y Sintamología"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
