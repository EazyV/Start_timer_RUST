from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QMenu, QAction, qApp
import sys
from ui import Ui_MainWindow
import os
import time



class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("AutoStart")
        self.ui.ip_text.setPlaceholderText('Введите ip сервера')
        self.ui.lineEdit.setPlaceholderText('Время в минутах')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirHomeIcon))
        self.ui.pushButton.clicked.connect(self.steam)

    def steam(self):
        ip = "start steam://connect/"
        output_ip = self.ui.ip_text.text()
        time_sec = self.ui.lineEdit.text()
        t = 60
        time.sleep(int(time_sec) * t)
        os.system(ip + str(output_ip))


app = QtWidgets.QApplication([])
application = Main()
application.show()
sys.exit(app.exec_())
