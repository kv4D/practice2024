# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line_dialog_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets


class Ui_line_dialog(object):
    def setupUi(self, line_dialog):
        line_dialog.setObjectName("line_dialog")
        line_dialog.resize(400, 208)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(line_dialog.sizePolicy().hasHeightForWidth())
        line_dialog.setSizePolicy(sizePolicy)
        line_dialog.setMinimumSize(QtCore.QSize(400, 208))
        line_dialog.setMaximumSize(QtCore.QSize(400, 208))
        self.verticalLayout = QtWidgets.QVBoxLayout(line_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setMinimumSize(QtCore.QSize(0, 0))
        self.text.setMaximumSize(QtCore.QSize(382, 100))
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_point_text = QtWidgets.QLabel(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_point_text.sizePolicy().hasHeightForWidth())
        self.start_point_text.setSizePolicy(sizePolicy)
        self.start_point_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.start_point_text.setObjectName("start_point_text")
        self.horizontalLayout_2.addWidget(self.start_point_text)
        self.start_point_x = QtWidgets.QPlainTextEdit(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_point_x.sizePolicy().hasHeightForWidth())
        self.start_point_x.setSizePolicy(sizePolicy)
        self.start_point_x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.start_point_x.setTabChangesFocus(False)
        self.start_point_x.setOverwriteMode(True)
        self.start_point_x.setBackgroundVisible(False)
        self.start_point_x.setObjectName("start_point_x")
        self.horizontalLayout_2.addWidget(self.start_point_x)
        self.start_point_y = QtWidgets.QPlainTextEdit(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_point_y.sizePolicy().hasHeightForWidth())
        self.start_point_y.setSizePolicy(sizePolicy)
        self.start_point_y.setMaximumSize(QtCore.QSize(16777215, 30))
        self.start_point_y.setOverwriteMode(True)
        self.start_point_y.setObjectName("start_point_y")
        self.horizontalLayout_2.addWidget(self.start_point_y)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.end_point_text = QtWidgets.QLabel(line_dialog)
        self.end_point_text.setObjectName("end_point_text")
        self.horizontalLayout_4.addWidget(self.end_point_text)
        self.end_point_x = QtWidgets.QPlainTextEdit(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_point_x.sizePolicy().hasHeightForWidth())
        self.end_point_x.setSizePolicy(sizePolicy)
        self.end_point_x.setMaximumSize(QtCore.QSize(16777215, 30))
        self.end_point_x.setOverwriteMode(True)
        self.end_point_x.setObjectName("end_point_x")
        self.horizontalLayout_4.addWidget(self.end_point_x)
        self.end_point_y = QtWidgets.QPlainTextEdit(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_point_y.sizePolicy().hasHeightForWidth())
        self.end_point_y.setSizePolicy(sizePolicy)
        self.end_point_y.setMaximumSize(QtCore.QSize(16777215, 30))
        self.end_point_y.setOverwriteMode(True)
        self.end_point_y.setObjectName("end_point_y")
        self.horizontalLayout_4.addWidget(self.end_point_y)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.thickness_text = QtWidgets.QLabel(line_dialog)
        self.thickness_text.setObjectName("thickness_text")
        self.horizontalLayout_5.addWidget(self.thickness_text)
        self.thickness = QtWidgets.QPlainTextEdit(line_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thickness.sizePolicy().hasHeightForWidth())
        self.thickness.setSizePolicy(sizePolicy)
        self.thickness.setMaximumSize(QtCore.QSize(16777215, 30))
        self.thickness.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.thickness.setOverwriteMode(True)
        self.thickness.setObjectName("thickness")
        self.horizontalLayout_5.addWidget(self.thickness)
        # spacerItem = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttons = QtWidgets.QDialogButtonBox(line_dialog)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(line_dialog)
        self.buttons.accepted.connect(line_dialog.accept) # type: ignore
        self.buttons.rejected.connect(line_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(line_dialog)

    def retranslateUi(self, line_dialog):
        _translate = QtCore.QCoreApplication.translate
        line_dialog.setWindowTitle(_translate("line_dialog", "Введите данные"))
        self.text.setText(_translate("line_dialog", "<html><head/><body><p align=\"center\">Введите координаты начальной и конечной точки</p><p align=\"center\">и значение толщины линии</p></body></html>"))
        self.start_point_text.setText(_translate("line_dialog", "Координаты начала (X, Y) "))
        self.start_point_x.setPlainText(_translate("line_dialog", "0"))
        self.start_point_y.setPlainText(_translate("line_dialog", "0"))
        self.end_point_text.setText(_translate("line_dialog", "Координаты конца (X, Y)  "))
        self.end_point_x.setPlainText(_translate("line_dialog", "0"))
        self.end_point_y.setPlainText(_translate("line_dialog", "0"))
        self.thickness_text.setText(_translate("line_dialog", "Толщина                   "))
        self.thickness.setPlainText("1")