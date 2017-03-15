# -*- coding: utf-8 -*-

from PyQt5 import QtGui

class SetSelectionTestDlg(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel("äöü")
        label_mit_umlaute = QtGui.QLabel(u"äöü")
        layout.addWidget(label)
        layout.addWidget(label_mit_umlaute)
        self.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sstd = SetSelectionTestDlg()
    result = sstd.exec_()
