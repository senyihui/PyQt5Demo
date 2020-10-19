import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QTextEdit,
                             QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp, QMenu)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class example(QMainWindow):     # QWidget
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Arial', 13))

        # 中间区域是文本编辑区域
        # textEdit = QTextEdit()
        # self.setCentralWidget(textEdit)

        # quit button
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(220, 190)

        # normal button
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # file menu
        exitAct = QAction(QIcon('web.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')  # 快捷键
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        # status bar
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAct)

        # 工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        # view menu(可勾选菜单) 有问题
        viewmenu = menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewmenu.addAction(viewStatAct)

        # 子菜单
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        fileMenu.addMenu(impMenu)

        # basic setting
        self.setGeometry(300, 300, 300, 220)
        self.center()
        self.setWindowTitle('test')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    # 关闭时确认对话框
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you going to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    # 窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cmenu = QMenu(self)
        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Test')
    # w.show()
    ex = example()
    sys.exit(app.exec_())

