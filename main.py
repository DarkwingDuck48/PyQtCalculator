#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, math
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QLCDNumber)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Установки геометрии окна и слоя
        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(300,300,300,350)
        self.setWindowTitle('Calculator')

        # Красивый экран
        lcd = QLCDNumber(self)
        grid.addWidget(lcd,0,0,1,0)

        M_plus = QPushButton('M+')
        M_minus = QPushButton('M-')
        M_C = QPushButton('MC')
        AC = QPushButton('AC')
        grid.addWidget(M_plus,1,0)
        grid.addWidget(M_minus,1,1)
        grid.addWidget(M_C,1,2)
        grid.addWidget(AC,1,3)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())