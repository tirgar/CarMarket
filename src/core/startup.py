from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import  QApplication

from src.gui.windows.pages.signin import SignUpWindow


class StartUp:

    def __init__(self):
        self.app = QApplication(sys_argv)
        self.gui_main = SignUpWindow()

    def start_app(self):
        self.gui_main.execute_app()
        sys_exit(self.app.exec_())
