# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 461)
        Form.setMinimumSize(QtCore.QSize(706, 461))
        Form.setMaximumSize(QtCore.QSize(706, 461))
        self.label_copyright = QtWidgets.QLabel(Form)
        self.label_copyright.setGeometry(QtCore.QRect(640, 440, 61, 20))
        self.label_copyright.setObjectName("label_copyright")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(110, 90, 493, 271))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.list_files = QtWidgets.QListWidget(self.widget)
        self.list_files.setObjectName("list_files")
        self.gridLayout.addWidget(self.list_files, 2, 0, 1, 2)
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 3, 0, 1, 1)
        self.btn_rename = QtWidgets.QPushButton(self.widget)
        self.btn_rename.setObjectName("btn_rename")
        self.gridLayout.addWidget(self.btn_rename, 3, 1, 1, 1)
        self.btn_choose = QtWidgets.QPushButton(self.widget)
        self.btn_choose.setObjectName("btn_choose")
        self.gridLayout.addWidget(self.btn_choose, 1, 0, 1, 2)
        self.label_infos = QtWidgets.QLabel(self.widget)
        self.label_infos.setObjectName("label_infos")
        self.gridLayout.addWidget(self.label_infos, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_copyright.setText(_translate("Form", "Thomas Lys"))
        self.btn_cancel.setText(_translate("Form", "Annuler"))
        self.btn_rename.setText(_translate("Form", "Renommer les fichiers"))
        self.btn_choose.setText(_translate("Form", "Choisir des fichiers"))
        self.label_infos.setText(_translate("Form", "Format de fichier accepté : BATmode220__2023-11-27_02-42-31_0001954.wav"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())