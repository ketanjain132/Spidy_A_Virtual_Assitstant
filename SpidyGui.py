from jarvisUI import Ui_JarvisUI
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import final2
import sys
from jarvisUI import Ui_JarvisUI

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        final2.TaskExecution()

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.spidy_ui = Ui_JarvisUI()
        
        self.spidy_ui.setupUi(self)

        self.spidy_ui.pushButton_2.clicked.connect(self.startFunc)

        self.spidy_ui.pushButton.clicked.connect(self.close)

    def startFunc(self):

        movie  = QtGui.QMovie("Iron_Template_1.gif")
        self.spidy_ui.label_2.setMovie(movie)
        movie.start()

        label_3 = QtGui.QMovie("__1.gif")
        self.spidy_ui.label_3.setMovie(label_3)
        label_3.start()

        label_4 = QtGui.QMovie("initial.gif")
        self.spidy_ui.label_4.setMovie(label_4)
        label_4.start()
 
        label_5 = QtGui.QMovie("Health_Template.gif")
        self.spidy_ui.label_5.setMovie(label_5)
        label_5.start()
 
        # label_6 = QtGui.QMovie("B.G_Template_1.gif")
        # self.spidy_ui.label.setMovie(label_6)
        # label_6.start()

        startFunctions.start()

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()

exit(Gui_App.exec_())