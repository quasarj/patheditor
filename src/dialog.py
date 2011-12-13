# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Dec 13 16:54:43 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 518)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathList = QtGui.QListWidget(self.centralwidget)
        self.pathList.setMinimumSize(QtCore.QSize(251, 241))
        self.pathList.setObjectName("pathList")
        self.horizontalLayout.addWidget(self.pathList)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(91, 271))
        self.frame_2.setMaximumSize(QtCore.QSize(91, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.cmdDown = QtGui.QPushButton(self.frame_2)
        self.cmdDown.setGeometry(QtCore.QRect(10, 50, 41, 28))
        self.cmdDown.setObjectName("cmdDown")
        self.cmdUp = QtGui.QPushButton(self.frame_2)
        self.cmdUp.setGeometry(QtCore.QRect(10, 10, 41, 28))
        self.cmdUp.setObjectName("cmdUp")
        self.cmdDelete = QtGui.QPushButton(self.frame_2)
        self.cmdDelete.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.cmdDelete.setObjectName("cmdDelete")
        self.cmdAdd = QtGui.QPushButton(self.frame_2)
        self.cmdAdd.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.cmdAdd.setObjectName("cmdAdd")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(529, 70))
        self.frame.setMaximumSize(QtCore.QSize(529, 70))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cmdSave = QtGui.QPushButton(self.frame)
        self.cmdSave.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.cmdSave.setObjectName("cmdSave")
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(170, 10, 229, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MainWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MainWindow.reject)
        QtCore.QObject.connect(self.pathList, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), MainWindow.itemclick)
        QtCore.QObject.connect(self.cmdAdd, QtCore.SIGNAL("clicked()"), MainWindow.additem)
        QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL("clicked()"), MainWindow.removeitem)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), MainWindow.saveitem)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Path Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDown.setText(QtGui.QApplication.translate("MainWindow", "▼", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdUp.setText(QtGui.QApplication.translate("MainWindow", "▲", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))

