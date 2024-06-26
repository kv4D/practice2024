import os
import cv2
import numpy

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QMainWindow

from degree_dialog import DegreeDialog
from line_dialog import LineDialog

from designs.main_menu_design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, picture: str):
        super().__init__()
        self.line_dialog = None
        self.degree_dialog = None
        self.setupUi(self, picture)
        self.source_picture = picture
        self.current_picture = picture
        self.save_path = os.path.abspath('user_data')

        # установка иконки окна
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        # для выбора с помощью optionBox
        self.optionBox.currentTextChanged.connect(self.set_photo)

        # для работы с опциями верхней панели
        self.add_sharpness.triggered.connect(self.add_sharpness_to_pic)
        self.paint_line.triggered.connect(self.open_line_dialog)
        self.change_angle.triggered.connect(self.open_degree_dialog)

    def set_photo(self):
        if self.optionBox.currentText() == 'Оригинальное изображение':
            self.picture.setPixmap(
                QtGui.QPixmap(self.source_picture).scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
            self.current_picture = self.source_picture

        elif self.optionBox.currentText() == 'Красный канал изображения':
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            red_pic = cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)[:, :, 2]

            is_success, red_pic_arr = cv2.imencode(".png", red_pic)
            red_pic_arr.tofile(self.save_path + r'\red.png', format='png')

            self.picture.setPixmap(
                QtGui.QPixmap(self.save_path + r'\red.png').scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
            self.current_picture = self.save_path + r'\red.png'

        elif self.optionBox.currentText() == 'Синий канал изображения':
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            blue_pic = cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)[:, :, 0]

            is_success, blue_pic_arr = cv2.imencode(".png", blue_pic)
            blue_pic_arr.tofile(self.save_path + r'\blue.png', format='png')

            self.picture.setPixmap(
                QtGui.QPixmap(self.save_path + r'\blue.png').scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
            self.current_picture = self.save_path + r'\blue.png'

        elif self.optionBox.currentText() == 'Зеленый канал изображения':
            src_file = open(self.source_picture, "rb")
            picture_arr = numpy.frombuffer(src_file.read(), dtype=numpy.uint8)
            green_pic = cv2.imdecode(picture_arr, cv2.IMREAD_COLOR)[:, :, 1]

            is_success, green_pic_arr = cv2.imencode(".png", green_pic)
            green_pic_arr.tofile(self.save_path + r'\green.png', format='png')

            self.picture.setPixmap(
                QtGui.QPixmap(self.save_path + r'\green.png').scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
            self.current_picture = self.save_path + r'\green.png'

    def add_sharpness_to_pic(self):
        sharp_filter = numpy.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

        try:
            pic_to_edit = open(self.current_picture, "rb")
            picture_arr = numpy.frombuffer(pic_to_edit.read(), dtype=numpy.uint8)
            sharpen_picture = cv2.filter2D(cv2.imdecode(picture_arr, cv2.IMREAD_COLOR), ddepth=-1, kernel=sharp_filter)

            is_success, sharpen_picture_arr = cv2.imencode(".png", sharpen_picture)
            sharpen_picture_arr.tofile(self.save_path + r'\sharpen.png', format='png')

            self.picture.setPixmap(
                QtGui.QPixmap(self.save_path + r'\sharpen.png').scaled(self.picture.width(), self.picture.height())
            )
            self.picture.setScaledContents(True)
            self.current_picture = self.save_path + r'\sharpen.png'
        except Exception:
            print("Возникла ошибка")

    def paint_line_on_pic(self):
        pass

    def change_angle_of_pic(self):
        pass

    def open_degree_dialog(self):
        self.degree_dialog = DegreeDialog(self)
        self.degree_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.degree_dialog.show()

    def open_line_dialog(self):
        self.line_dialog = LineDialog(self)
        self.line_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.line_dialog.show()

