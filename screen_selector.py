from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QTimer

import controller as ct

class Ui_W_selector(object):
    def setupUi(self, W_selector):
        W_selector.setObjectName("W_selector")
        W_selector.resize(714, 33)
        self.centralwidget = QtWidgets.QWidget(W_selector)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        W_selector.setCentralWidget(self.centralwidget)
        self.position_x = 0
        self.position_y = 0

        self.retranslateUi(W_selector)
        QtCore.QMetaObject.connectSlotsByName(W_selector)

        self.open_att(W_selector)

    def retranslateUi(self, W_selector):
        _translate = QtCore.QCoreApplication.translate
        W_selector.setWindowTitle(_translate("W_selector", "MainWindow"))

    def open_att(self, W_selector):
        index = ct.get_name()
        p_x, p_y = ct.get_position()
        width = len(index) * 100
        W_selector.resize(width, 33)
        # W_selector.move(p_x, p_y) # Paliativo
        for element in index:
            newBtn = QPushButton(element, self)
            newBtn.move(self.position_x, self.position_y)
            newBtn.show()
            self.position_x += 100
