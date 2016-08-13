import sys


from PyQt5 import QtWidgets
from PyQt5 import QtGui


class welcome(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QtWidgets.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('resx/windows.png'))

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = welcome()
    sys.exit(app.exec_())
