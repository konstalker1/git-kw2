import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.flag:
            qp.setBrush(QColor(*[250, 250, 0]))
            size = randint(10, 200)
            x, y = randint(10, 500), randint(10, 500)
            qp.drawEllipse(x, y, size, size)
            self.flag = False
        qp.end()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
