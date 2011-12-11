import sys
from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox

from dialog import Ui_Dialog

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def accept(self):
        """save the path var and exit"""

        items = []
        for i in xrange(self.ui.pathList.count()):
            items.append(self.ui.pathList.item(i).text())
        print items

        box = QMessageBox()
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setText("Are you sure you want to save?")
        ret = box.exec_()

        if ret == QMessageBox.Yes:
            QtGui.QApplication.exit()


    def reject(self):
        """exit the applicaiton if the user is sure"""

        box = QMessageBox()
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setText("Are you sure you want to exist?")
        ret = box.exec_()

        if ret == QMessageBox.Yes:
            QtGui.QApplication.exit()

    def itemclick(self):
        currentItemText = self.ui.pathList.currentItem().text()
        self.ui.lineEdit.setText(currentItemText)

    def additem(self):
        print "Add item"
        myapp.ui.pathList.addItem("New Entry")

    def removeitem(self):
        """delete the item at the current row"""

        print "Remove Item" 
        currentRow = self.ui.pathList.currentRow()
        self.ui.pathList.takeItem(currentRow)

    def saveitem(self):
        print "Save Item"
        self.ui.pathList.currentItem().setText(self.ui.lineEdit.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    #setup the data
    paths = [r"c:\windows", 
            r"c:\python27", 
            r"c:\pypy",
            "dummy a",
            "dummy b",
            "dummy c",
            "dummy d",
            "dummy e",
            "dummy f",
            "dummy g",
            "dummy h",
            "dummy i",
            "dummy j"] 
  
    for p in paths:
        myapp.ui.pathList.addItem(p)
    
    
    
    myapp.show()
    sys.exit(app.exec_())
