import sys
from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox

from dialog import Ui_MainWindow
import envars

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def do_something(self):
        print "I'm doing something!"

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
            envars.set_path(items)
            envars.broadcast_change()
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

    def moveup(self):
        # swap the current item's text with the item above it
        currentRow = self.ui.pathList.currentRow()
        if currentRow <= 0:
            return
        
        tempItem = self.ui.pathList.item(currentRow).text()
        self.ui.pathList.item(currentRow).setText(self.ui.pathList.item(currentRow - 1).text())
        self.ui.pathList.item(currentRow - 1).setText(tempItem)
        self.ui.pathList.setCurrentRow(currentRow - 1)
        
        print "Moved up"
    
    
    def movedown(self):
        # swap the current item's text with the item below it
        currentRow = self.ui.pathList.currentRow()
        if currentRow >= self.ui.pathList.count() - 1:
            return
        
        tempItem = self.ui.pathList.item(currentRow).text()
        self.ui.pathList.item(currentRow).setText(self.ui.pathList.item(currentRow + 1).text())
        self.ui.pathList.item(currentRow + 1).setText(tempItem)
        self.ui.pathList.setCurrentRow(currentRow + 1)
        
        print "Moved down"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    #setup the data

    paths = envars.get_path()
    for p in paths:
        myapp.ui.pathList.addItem(p)
    
    
    
    myapp.show()
    sys.exit(app.exec_())
