# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog_test.ui'
#
# Created: Thu Dec 15 14:22:02 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 413)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listView = QtGui.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(30, 20, 431, 301))
        self.listView.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.listView.setDragEnabled(True)
        self.listView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.listView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listView.setObjectName("listView")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

