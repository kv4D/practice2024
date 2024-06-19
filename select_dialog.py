from designs.select_dialog_design import Ui_greeting_dialog

import cv2

from PySide6 import QtWidgets, QtGui


class StartWindow(QtWidgets.QDialog, Ui_greeting_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('practice2024/assets/icon.png'))

        self.use_file.clicked.connect(self.browse_files)
        self.create_file.clicked.connect(self.make_photo)

    def browse_files(self):
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите .png или .jpeg файл", filter="Images ("
                                                                                                        "*.png *.jpg)")

        if directory[0]:
            print("good")
            # запускаем следующее окно


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

