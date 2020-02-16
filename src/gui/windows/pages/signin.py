from PyQt5 import Qt
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QWidget, QHBoxLayout
)

from src.gui.styles.pages.signin_style import *


class SignUpWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout()
        self.__init_ui__()

    def __init_ui__(self):
        self.setWindowTitle("Car_Market")
        self.setAccessibleName(sign_in_window_style[0])
        self.setStyleSheet(sign_in_window_style[1])
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addStretch(0)
        self.setLayout(self.main_layout)

        self.__input__()

    def __input__(self):
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.addStretch(0)

        self.user_name_line_edit = QLineEdit()
        self.user_name_line_edit.setPlaceholderText("User Name")
        self.user_name_line_edit.setContentsMargins(0, 0, 0, 0)
        self.user_name_line_edit.setAccessibleName(user_name_line_edit_style[0])
        self.user_name_line_edit.setStyleSheet(user_name_line_edit_style[1])

        self.password_line_edit = QLineEdit()
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setContentsMargins(0, 0, 0, 0)
        self.password_line_edit.setAccessibleName(password_line_edit_style[0])
        self.password_line_edit.setStyleSheet(password_line_edit_style[1])

        v_layout.addWidget(self.user_name_line_edit)
        v_layout.addWidget(self.password_line_edit)
        self.main_layout.addLayout(v_layout)







