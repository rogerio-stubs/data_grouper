from functools import partial
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication, QWidget, QToolButton, QLabel, QPushButton
from controller import controller

class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        self.buttons = []
        index = controller.get_client()
        for key, value in index.items():
            self.buttons.append(QPushButton(value, self))
            self.buttons[-1].clicked.connect(partial(self.client_id, data=key))
            layout.addWidget(self.buttons[-1])

    def client_id(self, data=""):
        print(f"data {data}")
        controller.insert_client(data)
        self.close()


