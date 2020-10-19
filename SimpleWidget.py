from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Simple Widget')
        self.initUI()

    def initUI(self):
        # set label
        self.label = QtWidgets.QLabel(self)
        self.label.setText('This is a label')
        self.label.move(10, 50)

        # set button
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(200, 10)
        self.btn.setText('Click me')
        self.btn.clicked.connect(lambda: self.show_popup())

        # set line edit
        self.input = QLineEdit(self)
        self.input.setGeometry(10, 10, 180, 30)

    def btnClicked(self):
        self.label.setText('btn has been clicked')
        self.label.adjustSize()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Something wrong')
        msg.setText('not found')
        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()


def window():
    # init
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    window()