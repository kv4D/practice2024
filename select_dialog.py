import os

from designs.select_dialog_design import Ui_greeting_dialog

from main_menu import MainWindow
from camera_error_dialog import CameraErrorDialog

import cv2

from PySide6 import QtWidgets, QtGui, QtCore


class StartWindow(QtWidgets.QDialog, Ui_greeting_dialog):
    def __init__(self):
        super().__init__()
        self.camera_error_window = None
        self.main_window = None
        self.setupUi(self)
        self.save_path = os.path.abspath('user_data')

        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        self.use_file.clicked.connect(self.browse_files)
        self.create_file.clicked.connect(self.make_photo)

    def browse_files(self):
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите .png или .jpeg файл", filter="Images ("
                                                                                                        "*.png *.jpg)")

        if directory[0]:
            self.open_main_window(directory[0][0])

    def make_photo(self):
        # Включаем первую камеру
        cap = cv2.VideoCapture(0)
        # Если камера не сработала
        if not cap.isOpened():
            self.open_camera_error_window()
        else:
            # "Прогреваем" камеру, чтобы снимок не был тёмным
            for i in range(30):
                cap.read()

            # Делаем снимок
            ret, frame = cap.read()

            # Записываем в файл
            is_success, frame_arr = cv2.imencode(".png", frame)
            frame_arr.tofile(self.save_path + r'\camera.png', format='png')
            
            # Отключаем камеру
            cap.release()

            # запускаем следующее окно
            self.open_main_window(self.save_path + r'\camera.png')

    def open_main_window(self, file: str):
        self.main_window = MainWindow(file)
        self.main_window.show()
        self.hide()

    def open_camera_error_window(self):
        self.camera_error_window = CameraErrorDialog()
        self.camera_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.camera_error_window.show()
