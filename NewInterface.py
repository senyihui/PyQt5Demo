# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 761, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.LeftLayout_2 = QtWidgets.QVBoxLayout()
        self.LeftLayout_2.setContentsMargins(5, 5, 5, 5)
        self.LeftLayout_2.setObjectName("LeftLayout_2")
        self.DeptListView_2 = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.DeptListView_2.setObjectName("DeptListView_2")
        self.LeftLayout_2.addWidget(self.DeptListView_2)
        self.MainLayout.addLayout(self.LeftLayout_2)
        self.MiddleLayout_2 = QtWidgets.QVBoxLayout()
        self.MiddleLayout_2.setContentsMargins(5, 5, 5, 5)
        self.MiddleLayout_2.setObjectName("MiddleLayout_2")
        self.GeneralListView = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.GeneralListView.setObjectName("GeneralListView")
        self.MiddleLayout_2.addWidget(self.GeneralListView)
        self.PosListView = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.PosListView.setObjectName("PosListView")
        self.MiddleLayout_2.addWidget(self.PosListView)
        self.MiddleLayout_2.setStretch(0, 2)
        self.MiddleLayout_2.setStretch(1, 3)
        self.MainLayout.addLayout(self.MiddleLayout_2)
        self.RightGridLayout = QtWidgets.QGridLayout()
        self.RightGridLayout.setObjectName("RightGridLayout")
        self.MainLayout.addLayout(self.RightGridLayout)
        self.MainLayout.setStretch(0, 2)
        self.MainLayout.setStretch(1, 3)
        self.MainLayout.setStretch(2, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
