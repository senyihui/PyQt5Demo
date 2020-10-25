from PyQt5 import QtCore, QtGui, QtWidgets
import NewInterface, sys


class myDialog(NewInterface.Ui_MainWindow):  # 继承自UI_Diglog类，注意我把UI_Dialog放在了untitled.py中，如果你把这个类放在了XXX.py文件中，就应该是XXX.UI_Dialog
    def __init__(self, Dialog):
        super().setupUi(Dialog)  # 调用父类的setupUI函数



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)  # 注意把类名修改为myDialog
    # ui.setupUi(MainWindow)  myDialog类的构造函数已经调用了这个函数，这行代码可以删去
    MainWindow.show()
    sys.exit(app.exec_())