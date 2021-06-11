# This file shows the grades or syllabus that you get from website or database
# Core function:
# def showGrades(grades):
#     grades:
#         columns = 初修学期    获得学期    课程    成绩    学分    课程属性    课程性质    获得方式
#         index = 1 2 ...... 
# def showSyllabus(syllabus):
#    syllabus:
#        columns = 星期日    星期一    星期二    星期三    星期四    星期五    星期六
#        index = 1-2    3-4    5-6    7-8    9-10    11-12
#
# Both grades and syllabus should be a pandas.DataFrame object!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import time

class Ui_Form(object):
    def __init__(self, form):
        self.form = form
        self.setupUi(form)
        self.file = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        self.tableViewOutput = QtWidgets.QTableView(Form)
        self.tableViewOutput.setGeometry(QtCore.QRect(10, 10, 671, 691))
        self.tableViewOutput.setObjectName("tableViewOutput")
        self.labelCurfunction = QtWidgets.QLabel(Form)
        self.labelCurfunction.setGeometry(QtCore.QRect(710, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelCurfunction.setFont(font)
        self.labelCurfunction.setObjectName("labelCurfunction")
        self.comboBoxCurfunction = QtWidgets.QComboBox(Form)
        self.comboBoxCurfunction.setGeometry(QtCore.QRect(830, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.comboBoxCurfunction.setFont(font)
        self.comboBoxCurfunction.setObjectName("comboBoxCurfunction")
        self.comboBoxCurfunction.addItem("")
        self.comboBoxCurfunction.addItem("")
        self.labelUsername = QtWidgets.QLabel(Form)
        self.labelUsername.setGeometry(QtCore.QRect(710, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.lineEditUsername = QtWidgets.QLineEdit(Form)
        self.lineEditUsername.setGeometry(QtCore.QRect(790, 100, 261, 31))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.labelPassword = QtWidgets.QLabel(Form)
        self.labelPassword.setGeometry(QtCore.QRect(710, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditPassword = QtWidgets.QLineEdit(Form)
        self.lineEditPassword.setGeometry(QtCore.QRect(790, 160, 261, 31))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.labelUpdateTime = QtWidgets.QLabel(Form)
        self.labelUpdateTime.setGeometry(QtCore.QRect(710, 220, 261, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelUpdateTime.setFont(font)
        self.labelUpdateTime.setObjectName("labelUpdateTime")
        self.lineEditUpdateTime = QtWidgets.QLabel(Form)
        self.lineEditUpdateTime.setGeometry(QtCore.QRect(790, 220, 261, 31))
        self.lineEditUpdateTime.setObjectName("lineEditUpdateTime")
        self.progressBarTotal = QtWidgets.QProgressBar(Form)
        self.progressBarTotal.setGeometry(QtCore.QRect(730, 380, 321, 21))
        self.progressBarTotal.setProperty("value", 0)
        self.progressBarTotal.setObjectName("progressBarTotal")
        self.labelSchedule = QtWidgets.QLabel(Form)
        self.labelSchedule.setGeometry(QtCore.QRect(710, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelSchedule.setFont(font)
        self.labelSchedule.setObjectName("labelSchedule")
        self.labelStatus = QtWidgets.QLabel(Form)
        self.labelStatus.setGeometry(QtCore.QRect(781, 330, 200, 31))
        self.labelStatus.setFont(font)
        self.labelStatus.setObjectName("labelStatus")
        self.pushButtonBegin = QtWidgets.QPushButton(Form)
        self.pushButtonBegin.setGeometry(QtCore.QRect(720, 440, 131, 41))
        self.pushButtonBegin.setObjectName("pushButtonBegin")
        self.pushButtonClear = QtWidgets.QPushButton(Form)
        self.pushButtonClear.setGeometry(QtCore.QRect(890, 440, 131, 41))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.labelName = QtWidgets.QLabel(Form)
        self.labelName.setGeometry(QtCore.QRect(710, 280, 211, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.lineEditName = QtWidgets.QLineEdit(Form)
        self.lineEditName.setGeometry(QtCore.QRect(920, 280, 131, 31))
        self.lineEditName.setReadOnly(True)
        self.lineEditName.setObjectName("lineEditName")
        self.pushButtonSave = QtWidgets.QPushButton(Form)
        self.pushButtonSave.setGeometry(QtCore.QRect(720, 510, 131, 41))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonUpdate = QtWidgets.QPushButton(Form)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(890, 510, 131, 41))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.pushButtonQuit = QtWidgets.QPushButton(Form)
        self.pushButtonQuit.setGeometry(QtCore.QRect(890, 650, 131, 41))
        self.pushButtonQuit.setObjectName("pushButtonQuit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sr的小工具"))
        self.labelCurfunction.setText(_translate("Form", "当前功能："))
        self.comboBoxCurfunction.setItemText(0, _translate("Form", "查看本学期课程"))
        self.comboBoxCurfunction.setItemText(1, _translate("Form", "查看成绩"))
        self.labelUsername.setText(_translate("Form", "账号:"))
        self.labelPassword.setText(_translate("Form", "密码:"))
        self.labelUpdateTime.setText(_translate("Form", "最近更新:"))
        self.labelSchedule.setText(_translate("Form", "进度:"))
        self.pushButtonBegin.setText(_translate("Form", "开始"))
        self.pushButtonClear.setText(_translate("Form", "清空"))
        self.labelName.setText(_translate("Form", "当前被查询人姓名:"))
        self.pushButtonSave.setText(_translate("Form", "保存"))
        self.pushButtonUpdate.setText(_translate("Form", "更新"))
        self.pushButtonQuit.setText(_translate("Form", "退出"))
        
    def showGrades(self, grades):
        model = QtGui.QStandardItemModel()
        self.tableViewOutput.setModel(model)
        self.tableViewOutput.verticalHeader().setDefaultSectionSize(30)
        self.tableViewOutput.horizontalHeader().setDefaultSectionSize(120)
        for index, col in enumerate(grades.columns.values):
            model.setHorizontalHeaderItem(index, QtGui.QStandardItem(col))
        self.tableViewOutput.setColumnWidth(2, 200)
        self.progressBarTotal.setProperty("value", 20)
        for index, col in enumerate(grades.columns.values):
            for row in range(grades.shape[0]):
                model.setItem(row, index, QtGui.QStandardItem(str(grades[col][row])))
                self.progressBarTotal.setProperty("value", 
                    80/(grades.shape[0]*grades.shape[1])*(index*grades.shape[1]+row))
        
        self.progressBarTotal.setProperty("value", 100)
        self.showStatus("完成")
        self.setTime()
        self.file = grades
    
    def showSyllabus(self, syllabus):
        model = QtGui.QStandardItemModel()
        self.tableViewOutput.setModel(model)
        self.tableViewOutput.verticalHeader().setDefaultSectionSize(120)
        self.tableViewOutput.horizontalHeader().setDefaultSectionSize(90)
        for index, col in enumerate(syllabus.columns.values):
            model.setHorizontalHeaderItem(index, QtGui.QStandardItem(col))
        self.progressBarTotal.setProperty("value", 20)
        for index, col in enumerate(syllabus.columns.values):
            for row in range(syllabus.shape[0]):
                model.setItem(row, index, QtGui.QStandardItem(str(syllabus[col][row])))
                self.progressBarTotal.setProperty("value", 
                    80/(syllabus.shape[0]*syllabus.shape[1])*(index*syllabus.shape[1]+row))
        
        self.progressBarTotal.setProperty("value", 100)
        self.showStatus("完成")
        self.setTime()
        self.file = syllabus
        
    def showStatus(self, status):
        _translate = QtCore.QCoreApplication.translate
        self.labelStatus.setText(_translate("Form", status))
        
    def setTime(self):
        _translate = QtCore.QCoreApplication.translate
        day = date.today().strftime("%B %d, %Y")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        self.labelUpdateTime.setText(_translate("Form", "最近更新: "+day+"   "+current_time))
        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget
    import sys
    import pandas as pd
    app = QApplication(sys.argv)
    form = QWidget()
    form.setFixedSize(1068, 718)
    w = Ui_Form(form)
    form.show()
    
    #syllabus = pd.DataFrame([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]], columns = list('1234567'))
    #w.showSyllabus(syllabus)
    
    #grades = pd.DataFrame([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]], columns=list('abcdefgh'))
    #w.showGrades(grades)
    
    sys.exit(app.exec_())