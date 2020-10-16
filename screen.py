from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication  
import sys
import screen_search
import screen_selector
import screen_manager


class ScreenSelector(QtWidgets.QMainWindow, screen_selector.Ui_W_selector):
    def __init__(self, parent=None):
        super(ScreenSelector, self).__init__(parent)
        self.setupUi(self)

class ScreenSearch(QtWidgets.QMainWindow, screen_search.Ui_W_search):
    def __init__(self, parent=None):
        super(ScreenSearch, self).__init__(parent)
        self.setupUi(self)

class ScreenManager(QtWidgets.QMainWindow, screen_manager.Ui_Manager):
    def __init__(self, parent=None):
        super(ScreenManager, self).__init__(parent)
        self.setupUi(self)

def Selector():
    app_selector = QApplication(sys.argv)
    form_selector = ScreenSelector()
    form_selector.show()
    app_selector.exec_()

def Search():
    app_search = QApplication(sys.argv)
    form_search = ScreenSearch()
    form_search.show()
    app_search.exec_()

def Manager():
    app_search = QApplication(sys.argv)
    form_search = ScreenManager()
    form_search.show()
    app_search.exec_()
