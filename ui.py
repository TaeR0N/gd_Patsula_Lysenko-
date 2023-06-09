from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: rgb(250, 100, 200);")
        MainWindow.resize(1350, 800)
        MainWindow.move(300, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 60, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 320, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 410, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(890, 320, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(890, 410, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(320, 230, 81, 31))
        self.spinBox_2.setRange(-100, 100)
        self.spinBox_2.setValue(1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(320, 320, 81, 31))
        self.spinBox_3.setRange(-100, 100)
        self.spinBox_3.setValue(1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(320, 410, 81, 31))
        self.spinBox_4.setRange(-100, 100)
        self.spinBox_4.setValue(1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setObjectName("spinBox_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(960, 220, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(960, 310, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(960, 400, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(710, 500, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(960, 490, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 660, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 660, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1020, 660, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение квадратных уравнений"))
        self.label.setText(_translate("MainWindow", "Квадратное уравнение имеет вид: ax^2 + bx + c = 0"))
        self.label_2.setText(_translate("MainWindow", "Введите a != 0:"))
        self.label_3.setText(_translate("MainWindow", "Введите b:"))
        self.label_4.setText(_translate("MainWindow", "Введите c:"))
        self.label_5.setText(_translate("MainWindow", "D ="))
        self.label_6.setText(_translate("MainWindow", "x1 ="))
        self.label_7.setText(_translate("MainWindow", "x2 ="))
        self.label_8.setText(_translate("MainWindow", "Количество корней ="))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.pushButton_2.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить"))

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: rgb(156, 212, 255);")
        MainWindow.resize(420, 270)
        MainWindow.move(800, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение квадратных уравнений"))
        self.label.setText(_translate("MainWindow", "Данные записаны в файл!"))
        self.pushButton.setText(_translate("MainWindow", "ОК"))
