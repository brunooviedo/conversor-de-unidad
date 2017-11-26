import sys
from PyQt5 import QtWidgets, uic, QtCore

# Cargar archivo .ui
form_class = uic.loadUiType("conversor.ui")[0]


class MyForm(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_clean.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    def clear(self):
        self.valor_1.clear()
        self.valor_2.clear()

    def exit(self):
        self.btn_exit.exit()


app = QtWidgets.QApplication(sys.argv)
window = MyForm(None)
window.show()
app.exec_()
