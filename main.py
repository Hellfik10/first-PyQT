import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            a = randrange(10, 100)
            qp.setBrush(QColor(255, 0, 0))
            # Рисуем прямоугольник заданной кистью
            qp.drawEllipse(self.x(), self.y(), a, a)

    def mousePressEvent(self, event):
        # Создаем объект QPainter для рисования
        self.do_paint = True




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())