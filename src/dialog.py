# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created: Tue Dec 13 12:56:45 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 518)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 480, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pathList = QtGui.QListWidget(Dialog)
        self.pathList.setGeometry(QtCore.QRect(20, 10, 571, 411))
        self.pathList.setObjectName("pathList")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 430, 571, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.cmdAdd = QtGui.QPushButton(Dialog)
        self.cmdAdd.setGeometry(QtCore.QRect(600, 370, 75, 23))
        self.cmdAdd.setObjectName("cmdAdd")
        self.cmdSave = QtGui.QPushButton(Dialog)
        self.cmdSave.setGeometry(QtCore.QRect(20, 460, 75, 23))
        self.cmdSave.setObjectName("cmdSave")
        self.cmdDelete = QtGui.QPushButton(Dialog)
        self.cmdDelete.setGeometry(QtCore.QRect(600, 400, 75, 23))
        self.cmdDelete.setObjectName("cmdDelete")
        self.cmdUp = QtGui.QPushButton(Dialog)
        self.cmdUp.setGeometry(QtCore.QRect(600, 170, 41, 28))
        self.cmdUp.setObjectName("cmdUp")
        self.cmdDown = QtGui.QPushButton(Dialog)
        self.cmdDown.setGeometry(QtCore.QRect(600, 210, 41, 28))
        self.cmdDown.setObjectName("cmdDown")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.pathList, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), Dialog.itemclick)
        QtCore.QObject.connect(self.cmdAdd, QtCore.SIGNAL("clicked()"), Dialog.additem)
        QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL("clicked()"), Dialog.removeitem)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), Dialog.saveitem)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Path Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdUp.setText(QtGui.QApplication.translate("Dialog", "▲", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDown.setText(QtGui.QApplication.translate("Dialog", "▼", None, QtGui.QApplication.UnicodeUTF8))

