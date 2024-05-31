import sys
import random


from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Household menu app")
        self.setFixedSize(QSize(600, 900))  # opens to this size
        self.setMinimumSize(QSize(300, 300))  # specifies smallest size
        self.setMaximumSize(QSize(900, 1200))  # specifies largest size


        # TODO: heavy rotation, light rotation, etc.
        self.menu = (
            "chx garlic",
            "chx artichoke",
            "taco salad",
            "chili",
            "meatloaf",
            "kofta",
            "curry",
            "chx piccata",
            "saus & onion",
            "stir fry",
            "tenderloin",
            "pork chops",
            "pork shoulders",
            "ATK chx thighs",
            "greek chx",
            "chx tenders",
            "chx tort. soup",
            "fried chx",
            "pork ribs",
            "bacon parm",
            "mac & cheese",
            "lentil salad",
            "lentil loaf",
            "pork & broc.",
            "crustless chx. pot pie",
        )
        self.menu_picks: list = []
        while len(self.menu_picks) < 6:
            self.menu_picks.append(random.choice(self.menu))

        self.lineedit = QLineEdit()
        self.lineedit.setMaxLength(10)
        self.lineedit.setPlaceholderText(str(self.menu_picks))

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)

        self.setCentralWidget(self.lineedit)

    def return_pressed(self):
        print("Return pressed!")
        self.lineedit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.lineedit.selectedText())

    def text_changed(self, text):
        print("Text changed...")
        print(text)

    def text_edited(self, text):
        print("Text edited...")
        print(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
