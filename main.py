from PyQt5.QtWidgets import QApplication, QWidget
from widget import Ui_Form
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    form.setFixedSize(1068, 718)
    w = Ui_Form(form)
    form.show()
    sys.exit(app.exec_())
