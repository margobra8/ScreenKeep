# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenkeep.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resx/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_header = QtWidgets.QLabel(self.centralwidget)
        self.title_header.setGeometry(QtCore.QRect(90, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title_header.setFont(font)
        self.title_header.setObjectName("title_header")
        self.logo_img = QtWidgets.QLabel(self.centralwidget)
        self.logo_img.setGeometry(QtCore.QRect(40, 10, 41, 41))
        self.logo_img.setText("")
        self.logo_img.setPixmap(QtGui.QPixmap("resx/refresh.png"))
        self.logo_img.setScaledContents(True)
        self.logo_img.setObjectName("logo_img")
        self.control_box = QtWidgets.QGroupBox(self.centralwidget)
        self.control_box.setGeometry(QtCore.QRect(10, 60, 241, 141))
        self.control_box.setObjectName("control_box")
        self.min_selector = QtWidgets.QSpinBox(self.control_box)
        self.min_selector.setGeometry(QtCore.QRect(101, 21, 81, 21))
        self.min_selector.setMinimum(1)
        self.min_selector.setMaximum(10)
        self.min_selector.setObjectName("min_selector")
        self.min_info_1 = QtWidgets.QLabel(self.control_box)
        self.min_info_1.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.min_info_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.min_info_1.setObjectName("min_info_1")
        self.min_info_name = QtWidgets.QLabel(self.control_box)
        self.min_info_name.setGeometry(QtCore.QRect(180, 20, 51, 21))
        self.min_info_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.min_info_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.min_info_name.setObjectName("min_info_name")
        self.status_info = QtWidgets.QLabel(self.control_box)
        self.status_info.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.status_info.setObjectName("status_info")
        self.status_state = QtWidgets.QLabel(self.control_box)
        self.status_state.setGeometry(QtCore.QRect(100, 50, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.status_state.setFont(font)
        self.status_state.setObjectName("status_state")
        self.close_btn = QtWidgets.QPushButton(self.control_box)
        self.close_btn.setGeometry(QtCore.QRect(10, 100, 221, 28))
        self.close_btn.setObjectName("close_btn")
        self.hide_btn = QtWidgets.QPushButton(self.control_box)
        self.hide_btn.setGeometry(QtCore.QRect(10, 70, 221, 28))
        self.hide_btn.setObjectName("hide_btn")
        self.dev_info = QtWidgets.QLabel(self.centralwidget)
        self.dev_info.setGeometry(QtCore.QRect(20, 260, 221, 51))
        self.dev_info.setWordWrap(True)
        self.dev_info.setObjectName("dev_info")
        self.ver_info = QtWidgets.QLabel(self.centralwidget)
        self.ver_info.setGeometry(QtCore.QRect(20, 320, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ver_info.setFont(font)
        self.ver_info.setObjectName("ver_info")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScreenKeep"))
        self.title_header.setText(_translate("MainWindow", "ScreenKeep"))
        self.control_box.setTitle(_translate("MainWindow", "Control"))
        self.min_info_1.setText(_translate("MainWindow", "Refrescar cada"))
        self.min_info_name.setText(_translate("MainWindow", "minutos"))
        self.status_info.setText(_translate("MainWindow", "La utilidad está"))
        self.status_state.setText(_translate("MainWindow", "activada"))
        self.close_btn.setText(_translate("MainWindow", "Cerrar"))
        self.hide_btn.setText(_translate("MainWindow", "Ocultar a la bandeja del sistema"))
        self.dev_info.setText(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ScreenKeep desarrollado por</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Marcos Gómez</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://margobra8.ml/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://margobra8.ml/</span></a></p></body></html>"))
        self.ver_info.setText(_translate("MainWindow", "versión 1.0.0"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())