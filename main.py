import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.img_index = 0
        self.lbl_img = QLabel()
        self.img_list = ['']
        self.initUI()

    def initUI(self):
        file_name = ''
        pixmap = QPixmap(file_name)
        self.lbl_img.setPixmap(pixmap)
        self.lbl_img.move(0, 0)
        self.setMenu()
        self.setButton()
        self.setWindowTitle('Dataset Filter')
        self.setGeometry(100, 100, 1200, 800)
        self.show()

    def setButton(self):
        prev_btn = QPushButton('Prev', self)
        prev_btn.resize(prev_btn.sizeHint())
        prev_btn.move(20, 400)
        next_btn = QPushButton('Next', self)
        next_btn.resize(next_btn.sizeHint())
        next_btn.clicked.connect(self.btnNext_clicked)
        next_btn.move(1100, 400)

    def setMenu(self):
        menubar = self.menuBar()
        selectFolder = QAction('File', self)
        selectFolder.triggered.connect(self.getFileList)
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(qApp.quit)
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(selectFolder)
        filemenu.addAction(exitAction)

    def getFileList(self):
        fname = QFileDialog.getExistingDirectory(self, "Select Directory")
        file_list = os.listdir(fname)
        file_list_jpg = [os.path.join(fname, file) for file in file_list if file.endswith(".jpg") or file.endswith(".png")]
        print(file_list_jpg)
        self.img_list = file_list_jpg
        pixmap = QPixmap(self.img_list[0])
        print(self.img_list[0])
        self.lbl_img.setPixmap(pixmap)
        self.lbl_img.move(0, 0)
        self.repaint()

    def btnNext_clicked(self):
        self.img_index += 1
        pixmap = QPixmap(self.img_list[self.img_index])
        self.lbl_img.setPixmap(pixmap)
        self.repaint()

    def btnPrev_clicked(self):
        self.img_index -= 1
        pixmap = QPixmap(self.img_list[self.img_index])
        self.lbl_img.setPixmap(pixmap)
        self.repaint()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
