from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUI(object):
    def setupUi(self, JarvisUI):
        JarvisUI.setObjectName("JarvisUI")
        JarvisUI.resize(1447, 835)
        self.centralwidget = QtWidgets.QWidget(JarvisUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, -90, 1521, 1021))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 0, 781, 481))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Iron_Template_1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-160, 130, 731, 531))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("__1.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, -40, 511, 281))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("initial.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 650, 401, 181))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Health_Template.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 480, 661, 341))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("B.G_Template_1.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 750, 151, 71))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 750, 151, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        JarvisUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(JarvisUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisUI)

    def retranslateUi(self, JarvisUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisUI.setWindowTitle(_translate("JarvisUI", "MainWindow"))
        self.pushButton.setText(_translate("JarvisUI", "EXIT"))
        self.pushButton_2.setText(_translate("JarvisUI", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisUI()
    ui.setupUi(JarvisUI)
    JarvisUI.show()
    sys.exit(app.exec_())