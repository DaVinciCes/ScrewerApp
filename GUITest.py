from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(500,100,500,500)
        self.setWindowTitle("Test")
        self.initUI()
    def initUI(self): 
        self.label=QtWidgets.QLabel(self)
        self.label.setText("Ejemplo")
        self.label.move(50,50)
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("Press")
        self.b1.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText("Botón presionado!!!! Listoooooo V3")
        self.updatewin()
    def updatewin(self):
        self.label.adjustSize()
        


def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
