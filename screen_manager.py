from PyQt5 import QtCore, QtGui, QtWidgets

import manager as mn

class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.resize(469, 198)
        self.centralwidget = QtWidgets.QWidget(Manager)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 40, 211, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_finish = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_finish.setObjectName("btn_finish")
        self.horizontalLayout.addWidget(self.btn_finish)
        Manager.setCentralWidget(self.centralwidget)

        self.retranslateUi(Manager)
        self.btn_start.clicked.connect(self.start)
        self.btn_finish.clicked.connect(self.finish)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        _translate = QtCore.QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "Manager"))
        self.btn_start.setText(_translate("Manager", "Start"))
        self.btn_finish.setText(_translate("Manager", "Finish"))

    def start(self):
        mn.start()

    def finish(self):
        mn.finish()
        