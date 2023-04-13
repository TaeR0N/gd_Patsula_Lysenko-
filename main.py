import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow, Ui_MainWindow3

class QuadraticEquation(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuadraticEquation, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculation)
        self.ui.pushButton_2.clicked.connect(self.exit)
        self.ui.pushButton_3.clicked.connect(self.write_file)

    def calculation(self):
        a = int(self.ui.spinBox_2.text())
        b = int(self.ui.spinBox_3.text())
        c = int(self.ui.spinBox_4.text())
        if a != 0:
            d = b ** 2 - 4 * a * c
            if d > 0:
                x1 = round((-b + d ** 0.5) / (2 * a), 2)
                x2 = round((-b - d ** 0.5) / (2 * a), 2)
                number = 2
            elif d == 0:
                x1 = round((-b) / (2 * a), 2)
                x2 = "нет"
                number = 1
            else:
                x1 = "нет"
                x2 = "нет"
                number = 0
            self.ui.textBrowser.setText(str(d))
            self.ui.textBrowser_2.setText(str(x1))
            self.ui.textBrowser_3.setText(str(x2))
            self.ui.textBrowser_4.setText(str(number))
        else:
            d = "нет"
            x1 = "нет"
            x2 = "нет"
            number = "нет"
            self.ui.textBrowser.setText(str(d))
            self.ui.textBrowser_2.setText(str(x1))
            self.ui.textBrowser_3.setText(str(x2))
            self.ui.textBrowser_4.setText(str(number))

        with open('info.txt', 'w', encoding='utf-8') as file:
            file.write("Значение a: " + str(a) + "\n")
            file.write("Значение b: " + str(b) + "\n")
            file.write("Значение c: " + str(c) + "\n")
            file.write("Дискриминант: " + str(d) + "\n")
            file.write("Корень 1: " + str(x1) + "\n")
            file.write("Корень 2: " + str(x2) + "\n")
            file.write("Количество корней: " + str(number))

    def exit(self):
        sys.exit()

    def back(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculation)
        self.ui.pushButton_2.clicked.connect(self.exit)
        self.ui.pushButton_3.clicked.connect(self.write_file)

    def write_file(self):
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.back)

app = QtWidgets.QApplication([])
application = QuadraticEquation()
application.show()
sys.exit(app.exec())