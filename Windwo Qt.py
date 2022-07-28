from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Log")
        self.setGeometry(360,281,360,281)
        self.Setbutton()
        self.quiteApp()

    def Setbutton(self):
        btn=QPushButton("Clicked This", self)
        btn.move(30,40)
        btn.clicked.connect(self.quiteApp)


    def quiteApp (self):
        msg=QMessageBox.question(self,"Conformation","DO you want contionous", QMessageBox.Yes|QMessageBox.No)

        if msg==QMessageBox.Yes:
            myapp.quit()
        elif msg ==QMessageBox.No:
            pass

myapp=QApplication()
window=Window()
window.show()

myapp.exec_()
sys.exit(0)