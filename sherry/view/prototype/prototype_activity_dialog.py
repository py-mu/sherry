# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_info_waring_error.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 537)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bar = QtWidgets.QWidget(Form)
        self.bar.setObjectName("bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_bar_app_logo = QtWidgets.QPushButton(self.bar)
        self.btn_bar_app_logo.setText("")
        self.btn_bar_app_logo.setObjectName("btn_bar_app_logo")
        self.horizontalLayout.addWidget(self.btn_bar_app_logo)
        self.btn_bar_title = QtWidgets.QPushButton(self.bar)
        self.btn_bar_title.setObjectName("btn_bar_title")
        self.horizontalLayout.addWidget(self.btn_bar_title)
        spacerItem = QtWidgets.QSpacerItem(607, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_bar_close = QtWidgets.QPushButton(self.bar)
        self.btn_bar_close.setText("")
        self.btn_bar_close.setObjectName("btn_bar_close")
        self.horizontalLayout.addWidget(self.btn_bar_close)
        self.verticalLayout.addWidget(self.bar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 192, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.dialog_show_info = QtWidgets.QLabel(self.widget)
        self.dialog_show_info.setObjectName("dialog_show_info")
        self.horizontalLayout_3.addWidget(self.dialog_show_info)
        spacerItem3 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.widget)
        spacerItem4 = QtWidgets.QSpacerItem(20, 192, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.btn_dialog_yes = QtWidgets.QPushButton(self.widget_2)
        self.btn_dialog_yes.setText("")
        self.btn_dialog_yes.setObjectName("btn_dialog_yes")
        self.horizontalLayout_2.addWidget(self.btn_dialog_yes)
        self.btn_dialog_no = QtWidgets.QPushButton(self.widget_2)
        self.btn_dialog_no.setText("")
        self.btn_dialog_no.setObjectName("btn_dialog_no")
        self.horizontalLayout_2.addWidget(self.btn_dialog_no)
        spacerItem6 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_bar_title.setText(_translate("Form", "????????????"))
        self.dialog_show_info.setText(_translate("Form", "????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
