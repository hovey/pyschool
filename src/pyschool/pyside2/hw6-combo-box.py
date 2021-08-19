import sys

from PySide2.QtWidgets import QApplication, QComboBox, QHBoxLayout, QWidget


class combodemo(QWidget):
    def __init__(self, parent=None):
        # super(combodemo, self):__init__(parent)
        super().__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItems(["C++", "Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")

    def selectionchange(self, i):
        print("Items in the list follow:")

        for index in range(self.cb.count()):
            print(f"{self.cb.itemText(index)}")

        print(f"Current index {i} selection changed {self.cb.currentText()}")


def main():
    app = QApplication(sys.argv)
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
