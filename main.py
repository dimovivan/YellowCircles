import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.aaa)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawcircle(qp)
            qp.end()

    def drawcircle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(10, 300)
        qp.drawEllipse(randint(100, 700), randint(100, 700), x, x)

    def aaa(self):
        self.do_paint = True
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())