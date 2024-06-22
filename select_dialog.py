from designs.select_dialog_design import Ui_greeting_dialog

from main_menu import MainWindow

import cv2, os

from PySide6 import QtWidgets, QtGui


class StartWindow(QtWidgets.QDialog, Ui_greeting_dialog):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('practice2024/assets/icon.png'))

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
        # "Прогреваем" камеру, чтобы снимок не был тёмным
        for i in range(30):
            cap.read()
        # Делаем снимок
        ret, frame = cap.read()
        # Записываем в файл
        cv2.imwrite('camera_photo.png', frame)
        # Отключаем камеру
        cap.release()
        # запускаем следующее окно
        self.open_main_window()

    def open_main_window(self, file: str):
        self.main_window = MainWindow(file)
        self.main_window.show()
        self.hide()

