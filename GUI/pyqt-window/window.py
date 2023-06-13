import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_ui = uic.loadUiType('window.ui')[0] # Qt Designer로 만든 UI파일 로딩
class MyWindowApp(QMainWindow, form_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.on_click_btn)
    
    def on_click_btn(self, e):
        QMessageBox.information(self, 'title', 'Hello', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyWindowApp()
    main_window.show()
    app.exec_()
