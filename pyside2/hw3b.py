# hello world 3, third example
from PyQt5.QtWidgets import *  # ug, the example does import *
app = QApplication([])
button = QPushButton('Click')

def on_button_clicked():  # callback
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)  # publish-subscribe
button.show()
app.exec_()
