from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

import database as data

class Ui_W_search(object):
    def setupUi(self, W_search):
        W_search.setObjectName("W_search")
        W_search.resize(714, 201)
        self.centralwidget = QtWidgets.QWidget(W_search)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.btn_close.setObjectName("btn_close")
        self.label_answer = QtWidgets.QLabel(self.centralwidget)
        self.label_answer.setGeometry(QtCore.QRect(20, 120, 611, 61))
        self.label_answer.setText("")
        self.label_answer.setObjectName("label_answer")
        self.text_search = QtWidgets.QTextEdit(self.centralwidget)
        self.text_search.setGeometry(QtCore.QRect(20, 30, 611, 71))
        self.text_search.setObjectName("text_search")
        self.btn_seach = QtWidgets.QPushButton(self.centralwidget)
        self.btn_seach.setGeometry(QtCore.QRect(630, 60, 75, 23))
        self.btn_seach.setObjectName("btn_seach")
        W_search.setCentralWidget(self.centralwidget)

        self.retranslateUi(W_search)
        self.btn_seach.clicked.connect(self.send_search)
        # self.btn_close.clicked.connect(self.end_application)
        QtCore.QMetaObject.connectSlotsByName(W_search)

    def retranslateUi(self, W_search):
        _translate = QtCore.QCoreApplication.translate
        W_search.setWindowTitle(_translate("W_search", "MainWindow"))
        self.btn_close.setText(_translate("W_search", "Finalizar"))
        self.btn_seach.setText(_translate("W_search", "Procurar"))

    def send_search(self):
        my_text = self.text_search.toPlainText()
        self.receiving_research(my_text)

    def receiving_research(self, my_text):
        self.label_answer.setText(my_text)
