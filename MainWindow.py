from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout,
                             QTextEdit, QMainWindow, QVBoxLayout, QPushButton, QDialog, QPlainTextEdit,
                             QGraphicsScene, QGraphicsView, QGraphicsItem)
from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.QtCore import (pyqtSignal, QPoint, Qt, QSize, QRectF, QTimer)
from random import randint


class Board(QGraphicsItem):
    BoundingRect = QRectF(0, 0, 300, 300)
    def __init__(self):
        super(Board, self).__init__()
        self.color = QColor(235, 80, 65)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000/33)
        self.colors = [QColor('red'), QColor('green'), QColor('blue')]

    def boundingRect(self):
        return Board.BoundingRect

    def paint(self, painter: QPainter, option, widget):
        painter.setBrush(self.color)
        for r in range(0, 6):
            for c in range(0, 6):
                painter.drawRect(50*r, 50*c,50, 50)


    def isUnderMouse(self):
        self.color = QColor(40, 55, 210)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if event.button() == Qt.LeftButton:
            self.color = self.colors[randint(0, len(self.colors)-1)]


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    board = Board()
    scene.addItem(board)
    scene.setSceneRect( -300, -300, 600, 600)
    scene.setItemIndexMethod(QGraphicsScene.NoIndex)
    view = QGraphicsView(scene)
    view.setMaximumSize(600, 600)
    view.setSizeAdjustPolicy(QGraphicsView.AdjustIgnored)
    view.setRenderHint(QPainter.Antialiasing)
    # view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    # view.setDragMode(QGraphicsView.ScrollHandDrag)
    view.setWindowTitle("Matrix Memory")
    view.resize(400, 300)
    view.show()
    sys.exit(app.exec_())
