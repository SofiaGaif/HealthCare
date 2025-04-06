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
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
        self.exp = exp
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_w, win_h)
        self.move(win_x, win_y)
    def initUI(self):
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def results(self):
        self.index = (4*(self.exp.t1+self.exp.t2+self.exp.t3)-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 11 <= self.index <= 14.9:
                return txt_res2
            elif 6 <= self.index <= 10.9:
                return txt_res3
            elif 0.5 <= self.index <= 5.9:
                return txt_res4
            else:
                return txt_res5
        elif 13 <= self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif 12.5 <= self.index <= 16.4:
                return txt_res2
            elif 7.5 <= self.index <= 12.4:
                return txt_res3
            elif 2 <= self.index <= 7.4:
                return txt_res4
            else:
                return txt_res5
        elif 11 <= self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif 14 <= self.index <= 17.9:
                return txt_res2
            elif 9 <= self.index <= 13.9:
                return txt_res3
            elif 3.5 <= self.index <= 8.9:
                return txt_res4
            else:
                return txt_res5
        elif 9 <= self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif 15.5 <= self.index <= 19.4:
                return txt_res2
            elif 10.5 <= self.index <= 15.4:
                return txt_res3
            elif 5 <= self.index <= 10.4:
                return txt_res4
            else:
                return txt_res5
        elif 7 <= self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif 17 <= self.index <= 20.9:
                return txt_res2
            elif 12 <= self.index <= 16.9:
                return txt_res3
            elif 6.5 <= self.index <= 11.9:
                return txt_res4
            else:
                return txt_res5
