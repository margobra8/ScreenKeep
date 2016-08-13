import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from screenkeep import Ui_MainWindow
from keypress_m import perform_keypress
from multiprocessing import Process


class ScreenKeepProgram(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        self.keypress_request()
        self.close_btn.clicked.connect(self.keypress_abort())

    def keypress_action(self):
        while True:
            time.sleep(5)
            perform_keypress('o')
            # time.sleep(self.min_selector.value())

    def keypress_request(self):
        do_keypress = Process(target=self.keypress_action)
        do_keypress.daemon = True
        do_keypress.start()

    def keypress_abort(self):
        self.close_btn.setText("nice")
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow
    window.show()
    sys.exit(app.exec_())

