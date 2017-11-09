from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout,
                             QTextEdit, QMainWindow, QVBoxLayout, QPushButton, QDialog, QPlainTextEdit)
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import (pyqtSignal, QPoint, Qt, QSize)

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        gl = QGridLayout()
        gl.setSizeConstraint(QGridLayout.SetFixedSize)
        txt = QTextEdit()
        font = QFont()
        font.setFamily('Lucida')
        font.setPixelSize(34)
        for r in range(0,5):
            for c in range(0,5):
                ti = QPlainTextEdit()
                ti.setTabChangesFocus(True)
                ti.setFont(font)
                gl.addWidget(ti, r, c)
        self.setLayout(gl)

    def setup_game_board(self) -> QGridLayout:
        """make a matrix of text boxes
        :arg none"""

        texts = list()
        gl = QGridLayout()
        for r in range(0,5):
            for c in range(0,5):
                ti = QTextEdit()
                gl.addWidget(ti, r, c)
                #texts.append({str(r+c):ti})
        return gl


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
