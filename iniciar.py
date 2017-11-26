import sys
from PyQt5 import QtWidgets, uic, QtGui

# Cargar archivo .ui
form_class = uic.loadUiType("conversor.ui")[0]


class MyForm(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_clean.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)
        self.btn_calc.clicked.connect(self.calc)

        # hacer conversion de metros x segundo a kilometros x hora.

    def calc(self):
        conversion = float(self.valor1.text()) * 3.6
        self.valor2.setText(str(conversion))

    def clear(self):
        self.valor1.clear()
        self.valor2.clear()

    def exit(self):
        self.btn_exit.exit()


app = QtWidgets.QApplication(sys.argv)
window = MyForm(None)
window.show()
app.exec_()
