# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brubclock.ui'
#
# Created: Tue Sep  3 18:55:51 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 436)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clock = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(200)
        font.setWeight(50)
        font.setBold(False)
        self.clock.setFont(font)
        self.clock.setStyleSheet("color: rgb(0, 170, 0);")
        self.clock.setScaledContents(True)
        self.clock.setAlignment(QtCore.Qt.AlignCenter)
        self.clock.setObjectName("clock")
        self.horizontalLayout.addWidget(self.clock)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.clock.setText(QtGui.QApplication.translate("MainWindow", "12:12 AB", None, QtGui.QApplication.UnicodeUTF8))

