from designs.main_menu_design import Ui_MainWindow

import cv2

from PySide6.QtWidgets import QMainWindow, QComboBox
from PySide6 import QtGui


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, picture: str):
        super().__init__()
        self.setupUi(self, picture)
        self.source_picture = picture

        self.setWindowIcon(QtGui.QIcon('practice2024/assets/icon.png'))

        # для выбора с помощью optionbox
        self.optionBox.currentTextChanged.connect(self.set_photo)

    def set_photo(self):
        if self.optionBox.currentText() == 'Оригинальное изображение':
            self.picture.setPixmap(
                QtGui.QPixmap(self.source_picture).scaled(self.picture.width(), self.picture.height()))
            self.picture.setScaledContents(True)
