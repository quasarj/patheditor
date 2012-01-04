

import sys
from PySide.QtCore import * 
from PySide.QtGui import * 

from test_ui import Ui_Dialog

#################################################################### 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 

#################################################################### 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        #QWidget.__init__(self, *args) 
        super(MyWindow, self).__init__(*args)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # create table
        list_data = [1,2,3,4]
        lm = MyListModel(list_data, self)
        
        # set the model
        self.ui.listView.setModel(lm)

    def accept(self):
        print self.ui.listView.model().listdata
    
    def reject(self):
        pass

#################################################################### 
class MyListModel(QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == Qt.DisplayRole:
            return self.listdata[index.row()]
        else: 
            return None

####################################################################
if __name__ == "__main__": 
    main()