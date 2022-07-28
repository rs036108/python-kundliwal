from PySide2.QtWidgets import *
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import *

import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 ")
        self.setGeometry(500,400,500,400)
        self.setIcon()
        self.stButton()
        self.quiteApp()
    def setIcon(self):
        appIcon =QIcon("iconp.png")
        self.setWindowIcon(appIcon)

    def stButton(self):
        btns = QPushButton("Quit", self)
        btns.move(50,100)
        btns.clicked.connect(self.quiteApp)

    def quiteApp(self):
        userInfo=QMessageBox.question(self,"Confirmation","Do You want Quit",QMessageBox.Yes| QMessageBox.No)

        if userInfo==QMessageBox.Yes:
            myapp.quit()
        elif userInfo==QMessageBox.No:
            pass

myapp=QApplication(sys.argv)
window=Window()
window.show()

myapp.exec_()
sys.exit(0)