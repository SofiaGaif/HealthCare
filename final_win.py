from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
        self.exp = exp
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)
    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = TestWin()
        self.hide()