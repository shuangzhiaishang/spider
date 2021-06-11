from controller import Controller
from PyQt5.QtWidgets import QApplication, QWidget
from view import Ui_Form
import sys
from mydb import MyDB

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    form.setFixedSize(1068, 718)
    w = Ui_Form(form)
    db = MyDB('mydb.db')
    controller = Controller(w, db)
    form.show()
    sys.exit(app.exec_())