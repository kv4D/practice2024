import sys


from PySide6.QtWidgets import QApplication

import select_dialog


def main():
    app = QApplication(sys.argv)
    window = select_dialog.StartWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
