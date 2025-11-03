import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class FirstWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button1 = QtWidgets.QPushButton("")
        self.button2 = QtWidgets.QPushButton("")
        self.button3 = QtWidgets.QPushButton("")
        self.button4 = QtWidgets.QPushButton("")
        self.button5 = QtWidgets.QPushButton("")
        self.button6 = QtWidgets.QPushButton("")
        self.button7 = QtWidgets.QPushButton("")
        self.button8 = QtWidgets.QPushButton("")
        self.button9 = QtWidgets.QPushButton("")
        self.text = QtWidgets.QLabel ("Hello World",alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.button1, 0, 0)
        self.layout.addWidget(self.button2, 0, 1)
        self.layout.addWidget(self.button3, 0, 2)
        self.layout.addWidget(self.button4, 1, 0)
        self.layout.addWidget(self.button5, 1, 1)
        self.layout.addWidget(self.button6, 1, 2)
        self.layout.addWidget(self.button7, 2, 0)
        self.layout.addWidget(self.button8, 2, 1)
        self.layout.addWidget(self.button9, 2, 2)

        #self.button1.clicked.connect(self.magic)
    
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = FirstWidget()
    widget.resize(200,200)
    widget.show()

    sys.exit(app.exec())