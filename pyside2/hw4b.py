import sys
from PySide2 import QtWidgets, QtCore

if __name__ == '__main__':
    qApp = QtWidgets.QApplication(sys.argv)

    mainWidget = QtWidgets.QWidget()
    mainWidget.setMinimumSize(800, 600)
    mainLayout = QtWidgets.QGridLayout(mainWidget)

    blue = QtWidgets.QWidget(mainWidget)
    blue.setStyleSheet('background-color: blue')
    blue.setFixedSize(100, 100)
    edit = QtWidgets.QTextEdit(mainWidget)

    mainLayout.addWidget(edit, 0, 0)
    mainLayout.addWidget(blue, 0, 1)

    mainWidget.show()
    sys.exit(qApp.exec_())