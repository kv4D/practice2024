import os.path

import cv2
import numpy

from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow

from designs.main_menu_design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, picture: str):
        super().__init__()
        self.setupUi(self, picture)
        self.source_picture = picture
        self.current_picture = picture

        self.setWindowIcon(QtGui.QIcon('practice2024/assets/icon.png'))

        # для выбора с помощью optionbox
        self.optionBox.currentTextChanged.connect(self.set_photo)

        # для работы с опциями верхней панели
        self.add_sharpness.triggered.connect(self.add_sharpness_to_pic)
        self.paint_line.triggered.connect(self.do_smt)
        self.change_angle.triggered.connect(self.do_smt)

    def set_photo(self):
        if self.optionBox.currentText() == 'Оригинальное изображение':
            self.picture.setPixmap(
                QtGui.QPixmap(self.source_picture).scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
        elif self.optionBox.currentText() == 'Красный канал изображения':
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            red_pic = cv2.imwrite('red.png', cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)[:, :, 2])

            #self.picture.setPixmap(
           #     QtGui.QPixmap(red_pic).scaled(self.picture.width(), self.picture.height())
           # )
            self.picture.setScaledContents(True)
        elif self.optionBox.currentText() == 'Синий канал изображения':
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            blue_pic = cv2.imwrite('blue.png', cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)[:, :, 0])

            self.picture.setPixmap(

            )
            self.picture.setScaledContents(True)
        elif self.optionBox.currentText() == 'Зеленый канал изображения':
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            green_pic = cv2.imwrite('green.png', cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)[:, :, 1])

            self.picture.setPixmap(

            )
            self.picture.setScaledContents(True)

    def do_smt(self):
        print('да')

    def add_sharpness_to_pic(self):
        sharp_filter = numpy.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

        try:
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            sharpen_picture = cv2.filter2D(cv2.imdecode(picture_arr, cv2.IMREAD_COLOR), ddepth=-1, kernel=sharp_filter)
            cv2.imwrite('sharpen.png', sharpen_picture)

            self.picture.setPixmap(
                QtGui.QPixmap('sharpen.png').scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
            self.current_picture = 'sharpen.png'
        except Exception:
            print("Возникла ошибка")

    def paint_line_on_pic(self):
        pass

    def change_angle_of_pic(self):
        pass
