import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import time
from FontCompare import *
# Import the interface class
import main_ui
 
class MainApp(QMainWindow, main_ui.Ui_MainWindow):
    """ The second parent must be Ui_<obj. name of main widget class>. \
      If confusing, simply open up ImageViewer.py and get the class \
      name used. I'd named mine as mainWindow and hence the use. """
    Testfilepath = ""
    Standardfilepath = ""
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        # This is because Python does not automatically
        # call the parent's constructor.
        self.setupUi(self)
        self.connectActions()
 
    def connectActions(self):
        self.executeButton.clicked.connect(self.printMessage)
        self.loadTestpushButton.clicked.connect(self.OpenTestFile)
        self.loadStandardpushButton.clicked.connect(self.OpenStandardFile)

    def main(self):
        self.show()

    def OpenTestFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Test File')
        if fontforge.open(filename):
            QMessageBox.about(self, "Success", "The file was loaded successfully!")
            self.Testfilepath = filename
            self.testfilepath.setText(filename)
            return
        else:
            QMessageBox.about(self, "Error", "The file could not be loaded!\n Please try again")

    def OpenStandardFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Standard File'))
        if fontforge.open(filename):
            QMessageBox.about(self, "Success", "The file was loaded successfully!")
            self.Standardfilepath = filename
            self.standardfilepath.setText(filename)
            return
        else:
            QMessageBox.about(self, "Error", "The file could not be loaded!\n Please try again")


    def printMessage(self):
        start = time.clock()
        fontA = fontforge.open(self.Testfilepath)
        fontB = fontforge.open(self.Standardfilepath)
        fc=FontCompare()
        count=0
        scores = fc.font_compare(fontA,fontB,(0x901,0x970))
        total=len(scores)
        for gltuple in scores:
            self.MessageBox.append(str(gltuple))
            count+=gltuple[1]
        elapsed = (time.clock() - start)
        self.MessageBox.append("The total score was "+str(count))
        self.MessageBox.append("The execution time was "+str(elapsed))
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.main()
    app.exec_()
