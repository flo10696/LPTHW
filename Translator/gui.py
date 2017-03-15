# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QGridLayout, QTextEdit, QLineEdit, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui

class Gui(QWidget):

    def __init__(self, givenController):

        super(Gui, self).__init__()

        self.controller = givenController


    def initUI(self):

        #create Labels:
        panelsize = 300
        # first Label

        self.first = QLabel(u"1 time")
        self.first.setFixedSize(panelsize, panelsize)


        self.first.setAutoFillBackground(True)
        firstPalette = self.first.palette()
        firstPalette.setColor(self.first.backgroundRole(), QColor(66, 133, 244))
        firstPalette.setColor(self.first.foregroundRole(), QColor(255, 255, 255))
        self.first.setPalette(firstPalette)

        self.first.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")




        # second Label

        self.second = QLabel('2 times')
        self.second.setFixedSize(panelsize, panelsize)

        self.second.setAutoFillBackground(True)
        secondPalette = self.second.palette()
        secondPalette.setColor(self.second.backgroundRole(), QColor(250, 187, 6))
        secondPalette.setColor(self.second.foregroundRole(), QColor(255, 255, 255))
        self.second.setPalette(secondPalette)

        self.second.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        #third Label

        self.third = QLabel('3 times')
        self.third.setFixedSize(panelsize, panelsize)

        self.third.setAutoFillBackground(True)
        thirdPalette = self.third.palette()
        thirdPalette.setColor(self.third.backgroundRole(), QColor(52, 168, 82))
        thirdPalette.setColor(self.third.foregroundRole(), QColor(255, 255, 255))
        self.third.setPalette(thirdPalette)

        self.third.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        # fourth Label

        self.fourth = QLabel('4 times')
        self.fourth.setFixedSize(panelsize, panelsize)

        self.fourth.setAutoFillBackground(True)
        fourthPalette = self.fourth.palette()
        fourthPalette.setColor(self.fourth.backgroundRole(), QColor(234, 67, 53))
        fourthPalette.setColor(self.fourth.foregroundRole(), QColor(255, 255, 255))
        self.fourth.setPalette(fourthPalette)

        self.fourth.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        #fivth Label

        self.fivth = QLabel('5 times')
        self.fivth.setFixedSize(panelsize, panelsize)

        self.fivth.setAutoFillBackground(True)
        fivthPalette = self.fivth.palette()
        fivthPalette.setColor(self.fivth.backgroundRole(), QColor(66, 133, 244))
        fivthPalette.setColor(self.fivth.foregroundRole(), QColor(255, 255, 255))
        self.fivth.setPalette(fivthPalette)

        self.fivth.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        # sixth Label

        self.sixth = QLabel('6 times')
        self.sixth.setFixedSize(panelsize, panelsize)

        self.sixth.setAutoFillBackground(True)
        sixthPalette = self.sixth.palette()
        sixthPalette.setColor(self.sixth.backgroundRole(), QColor(250, 187, 6))
        sixthPalette.setColor(self.sixth.foregroundRole(), QColor(255, 255, 255))
        self.sixth.setPalette(sixthPalette)

        self.sixth.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        # seventh Label

        self.seventh = QLabel('7 times')
        self.seventh.setFixedSize(panelsize, panelsize)

        self.seventh.setAutoFillBackground(True)
        seventhPalette = self.seventh.palette()
        seventhPalette.setColor(self.seventh.backgroundRole(), QColor(52, 168, 82))
        seventhPalette.setColor(self.seventh.foregroundRole(), QColor(255, 255, 255))
        self.seventh.setPalette(seventhPalette)

        self.seventh.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        # eigthth Label

        self.eighth = QLabel('8 times')
        self.eighth.setFixedSize(panelsize, panelsize)

        self.eighth.setAutoFillBackground(True)
        eighthPalette = self.eighth.palette()
        eighthPalette.setColor(self.eighth.backgroundRole(), QColor(234, 67, 53))
        eighthPalette.setColor(self.eighth.foregroundRole(), QColor(255, 255, 255))
        self.eighth.setPalette(eighthPalette)

        self.eighth.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        # nineth Label

        self.nineth = QLabel('9 times')
        self.nineth.setFixedSize(panelsize, panelsize)

        self.nineth.setAutoFillBackground(True)
        ninethPalette = self.nineth.palette()
        ninethPalette.setColor(self.nineth.backgroundRole(), QColor(66, 133, 244))
        ninethPalette.setColor(self.nineth.foregroundRole(), QColor(255, 255, 255))
        self.nineth.setPalette(ninethPalette)

        self.nineth.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        #tenth Label

        self.tenth = QLabel('10 times')
        self.tenth.setFixedSize(panelsize, panelsize)

        self.tenth.setAutoFillBackground(True)
        tenthPalette = self.tenth.palette()
        tenthPalette.setColor(self.tenth.backgroundRole(), QColor(250, 187, 6))
        tenthPalette.setColor(self.tenth.foregroundRole(), QColor(255, 255, 255))
        self.tenth.setPalette(tenthPalette)

        self.tenth.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        # output Label

        self.output = QLabel('final output')
        self.output.setFixedSize(panelsize, panelsize)

        self.output.setAutoFillBackground(True)
        outputPalette = self.output.palette()
        outputPalette.setColor(self.output.backgroundRole(), QColor(52, 168, 82))
        outputPalette.setColor(self.output.foregroundRole(), QColor(255, 255, 255))
        self.output.setPalette(outputPalette)

        self.output.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")


        # create inputWindow

        self.inputWindow = QLineEdit()
        self.inputWindow.setFixedSize(250, 100)
        self.inputWindow.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Helvetica;")

        self.inputButton = QPushButton("Translate!")
        self.inputButton.setFixedSize(250, 80)
        self.inputButton.clicked.connect(self.translate)









        #create Grid small

        inputGrid = QGridLayout()
        inputGrid.setSpacing(20)

        inputGrid.addWidget(self.inputWindow, 0, 0)
        inputGrid.addWidget(self.inputButton, 1, 0)




        # create Grid big

        grid = QGridLayout()
        grid.setSpacing(0)



        # set Locations

        grid.addWidget(self.first, 1, 3)
        grid.addWidget(self.second, 2, 3)
        grid.addWidget(self.third, 3, 3)
        grid.addWidget(self.fourth, 3, 2)
        grid.addWidget(self.fivth, 3, 1)
        grid.addWidget(self.sixth, 3, 0)
        grid.addWidget(self.seventh, 2, 0)
        grid.addWidget(self.eighth, 1, 0)
        grid.addWidget(self.nineth, 1, 1)
        grid.addWidget(self.tenth, 1, 2)
        grid.addWidget(self.output, 2, 2)

        grid.addItem(inputGrid, 2, 1)




        self.setLayout(grid)


        self.setAutoFillBackground(True)
        selfPalette = self.palette()
        selfPalette.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(selfPalette)



        self.setGeometry(600, 600, 650, 600)
        self.show()


        self.labels = [self.first, self.second, self.third, self.fourth, self.fivth, self.sixth, self.seventh, self.eighth, self.nineth, self.tenth, self.output]

        for x in range(0,11):
            self.labels[x].setWordWrap(True)

    def update(self, fieldNumber, text):

        self.labels[fieldNumber].setText(text)
        self.show()


    def translate(self):

        self.update(0, "1 time")
        for x in range(1, 10):
            text = str(x + 1) + " times"
            self.update(x, text)
        self.update(10, "final output")


        if(self.inputWindow.text() != ''):
            readText = self.inputWindow.text()
            self.controller.translate(readText)
