import enum
from mydb import MyDB
from PyQt5 import QtCore, QtGui, QtWidgets
from network import NetWork
import pandas as pd
from copy import deepcopy

class Ui_Form(object):
    def __init__(self, form):
        self.form = form
        self.network = NetWork()
        self.setupUi(form)
        self.initUi()
        self.connectUi()

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
        self.labelPasskey = QtWidgets.QLabel(Form)
        self.labelPasskey.setGeometry(QtCore.QRect(710, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.labelPasskey.setFont(font)
        self.labelPasskey.setObjectName("labelPasskey")
        self.lineEditPasskey = QtWidgets.QLineEdit(Form)
        self.lineEditPasskey.setGeometry(QtCore.QRect(790, 220, 261, 31))
        self.lineEditPasskey.setObjectName("lineEditPasskey")
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
        self.pushButtonHistory = QtWidgets.QPushButton(Form)
        self.pushButtonHistory.setGeometry(QtCore.QRect(890, 510, 131, 41))
        self.pushButtonHistory.setObjectName("pushButtonHistory")
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
        self.labelPasskey.setText(_translate("Form", "密匙:"))
        self.labelSchedule.setText(_translate("Form", "进度:"))
        self.pushButtonBegin.setText(_translate("Form", "开始"))
        self.pushButtonClear.setText(_translate("Form", "清空"))
        self.labelName.setText(_translate("Form", "当前被查询人姓名:"))
        self.pushButtonSave.setText(_translate("Form", "保存"))
        self.pushButtonHistory.setText(_translate("Form", "查看历史"))
        self.pushButtonQuit.setText(_translate("Form", "退出"))
    
    def initUi(self):
        self.curFunc = 0
        self.username = ''
        self.password = ''
        self.passkey = ''
        self.name = ''

    def connectUi(self):
        self.pushButtonBegin.clicked.connect(self.update)
        self.pushButtonBegin.clicked.connect(self.begin)
        self.pushButtonClear.clicked.connect(self.clear)
        self.pushButtonClear.clicked.connect(self.update)
        self.pushButtonQuit.clicked.connect(quit)

    def update(self):
        self.curFunc = self.comboBoxCurfunction.currentIndex()
        self.username = self.lineEditUsername.text()
        self.password = self.lineEditPassword.text()
        self.passkey = self.lineEditPasskey.text()
        self.name = self.lineEditName.text()

    def begin(self):
        if self.curFunc == 0:
            self.funcCourseSchedule()
        elif self.curFunc == 1:
            self.funcResult()
        
    def funcCourseSchedule(self):
        if self.network.loginEAS(self.username, self.password) == False:
            self.showStatus("登陆教务系统失败")
            return
        self.showStatus("登录教务系统成功")

        studentName = self.network.getStudentInfoFromEAS()
        self.lineEditName.setText(studentName)
        self.progressBarTotal.setProperty("value", 5)

        courseSchedule = self.network.getCourseScheduleFromEAS()
        self.progressBarTotal.setProperty("value", 15)
        self.showStatus("成功获取课程表信息")

        model = QtGui.QStandardItemModel()
        self.tableViewOutput.setModel(model)
        self.tableViewOutput.verticalHeader().setDefaultSectionSize(120)
        self.tableViewOutput.horizontalHeader().setDefaultSectionSize(90)
        for index, col in enumerate(courseSchedule.columns.values):
            model.setHorizontalHeaderItem(index, QtGui.QStandardItem(col))
        self.progressBarTotal.setProperty("value", 20)
        for index, col in enumerate(courseSchedule.columns.values):
            for row in range(courseSchedule.shape[0]):
                model.setItem(row, index, QtGui.QStandardItem(str(courseSchedule[col][row])))
                self.progressBarTotal.setProperty("value", 
                    80/(courseSchedule.shape[0]*courseSchedule.shape[1])*(index*courseSchedule.shape[1]+row))
        
        self.progressBarTotal.setProperty("value", 100)
        self.showStatus("完成")
        
    def login(self):
        self.showStatus("尝试登录教务系统")
        if self.network.loginEAS(self.username, self.password) == False:
            self.showStatus("登陆教务系统失败")
            return
        self.showStatus("登录教务系统成功")

        self.name = self.network.getStudentInfoFromEAS()
        self.lineEditName.setText(self.name)
        self.progressBarTotal.setProperty("value", 5)

        results = self.network.getResultsFromEAS()
        self.progressBarTotal.setProperty("value", 15)
        self.showStatus("成功获取成绩信息")
        return results
    
    def getResult(self, db):
        login = db.checkPassword(self.username, self.password)
        if not login:
            print('wrong password')
            return None
        self.name = db.getName(self.username)
        self.lineEditName.setText(self.name)
        results = db.getGrades(self.username)
        columns = ['课程', '成绩', '学分', '课程属性', '课程性质', '获得方式', '初修学期', '获得学期']
        results = pd.DataFrame(results, columns=columns)
        columns = columns[-2:] + columns[:-2]
        return results[columns]
    
    def saveToDB(self, results, db):
        print('save info to db')
        student = [(self.username, self.name, self.password)]
        grade = pd.DataFrame(deepcopy(results.loc[:, ['课程', '成绩']]))

        results.drop('成绩', axis='columns', inplace=True)
        columns = list(results.columns)
        columns = columns[2:] + columns[:2]
        results = results[columns]

        grade = list(map(lambda x:(self.username,)+tuple(x), grade.values))
        course = list(map(lambda x:tuple(x), results.values))
        
        db.insertIntoStudent(student)
        db.insertIntoCourse(course)
        db.insertIntoGrade(grade)
        print('saved info')

    def funcResult(self):
        db = MyDB('mydb.db')
        results = None
        if db.exist(self.username):
            print('student exist in db')
            results = self.getResult(db)
        else:
            print('login...')
            results = self.login()
            if not results:
                return
            self.saveToDB(results, db)
        
        if results is None:
            return

        model = QtGui.QStandardItemModel()
        self.tableViewOutput.setModel(model)
        self.tableViewOutput.verticalHeader().setDefaultSectionSize(30)
        self.tableViewOutput.horizontalHeader().setDefaultSectionSize(120)
        for index, col in enumerate(results.columns.values):
            model.setHorizontalHeaderItem(index, QtGui.QStandardItem(col))
        self.tableViewOutput.setColumnWidth(2, 200)
        self.progressBarTotal.setProperty("value", 20)
        for index, col in enumerate(results.columns.values):
            for row in range(results.shape[0]):
                model.setItem(row, index, QtGui.QStandardItem(str(results[col][row])))
                self.progressBarTotal.setProperty("value", 
                    80/(results.shape[0]*results.shape[1])*(index*results.shape[1]+row))
        
        self.progressBarTotal.setProperty("value", 100)
        self.showStatus("完成")
            
    def showStatus(self, status):
        _translate = QtCore.QCoreApplication.translate
        self.labelStatus.setText(_translate("Form", status))

    def clear(self):
        model = QtGui.QStandardItemModel(0, 0)
        self.tableViewOutput.setModel(model)
        self.lineEditUsername.setText('')
        self.lineEditPassword.setText('')
        self.lineEditPasskey.setText('')
        self.lineEditName.setText('')
        self.progressBarTotal.setProperty("value", 0)
        self.showStatus('')

    
