
import sys
from UI.gen import mainwindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    # __init__ is used for pythonic OOP, used as obj constructor, initializes obj attributes.
    # self repr instance of class, used to access attr & methods of class, binds attr with given arg
    # self points to curent obj, 1st param of method is the instance method is called on (weird)
    def __init__(self):
        
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = mainwindow.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec()
        
