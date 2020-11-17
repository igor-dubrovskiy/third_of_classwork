import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QImage
from random import randint

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 331)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(160, 300, 101, 31))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "кнопка"))

        
class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(255, 255, 255))
        self.btn.clicked.connect(self.click)
        self.show()

    def click(self):
        self.paint = QPainter(self.image)
        self.ellips()

    def paintEvent(self, e):
        paint = QPainter(self)
        paint.drawImage(0, 0, self.image)

    def ellips(self):
        x, y = [randint(10, 400) for i in range(2)]
        w = randint(10, 100)
        paint = QPainter(self)
        paint.drawImage(0, 0, self.image)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.paint.setBrush(QColor(r, g, b))
        self.paint.drawEllipse(x, y, w, w)
        self.update()


app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())
