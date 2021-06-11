# This file stores the logic for controlling the gui,
# it gets grades and syllabus using Network module
# and update view
#
#                     0          ------------
#    -------      |---------->  | getSyllabus|--------\             #########     save
#   | begin | ----               ------------            update     #  view # ----------->   .csv file
#    -------      |______        ------------          ---------->  #########
#                     1  \---> |  getGrades  |--------/
#                                ------------
#
#
#

from network import NetWork
from PyQt5 import QtGui, QtWidgets
import pandas as pd

class Model:
    def __init__(self, view, db):
        self._view = view
        self._db = db
        
    def begin(self):
        student_id = self._view.lineEditUsername.text()
        password = self._view.lineEditPassword.text()
        option = self._view.comboBoxCurfunction.currentIndex()
        if option == 0:
            self.getSyllabus(student_id, password)
        elif option == 1:
            self.getGrades(student_id, password)
            
    def getGrades(self, student_id, password):
        grades = self.getGradesFromDB(student_id, password)
        if grades is None:
            self.getGradesFromWeb(student_id, password)
            return
        self._view.name = self._db.getName(student_id)
        self._view.lineEditName.setText(self._view.name)
        self._view.showGrades(grades)
        
    def getGradesFromDB(self, student_id, password):
        if self._db.login(student_id, password):
            grades = self._db.getGrades(student_id)
            columns = ['初修学期',    '获得学期',    '课程',    '成绩',    '学分',    '课程属性',    '课程性质',    '获得方式', '名字']
            return pd.DataFrame(grades, columns=columns)
        return None
    
    def getGradesFromWeb(self, student_id, password):
        network = NetWork()
        if network.loginEAS(student_id, password) == False:
            return
        self._view.name = network.getStudentInfoFromEAS()
        self._view.lineEditName.setText(self._view.name)
        grades = network.getGradesFromEAS()
        self._view.showGrades(grades)
        
    def getSyllabus(self, student_id, password):
        pass
        
    def getSyllabusFromWeb(self, student_id, password):
        network = NetWork()
        if network.loginEAS(student_id, password) == False:
            return
        self._view.name = network.getStudentInfoFromEAS()
        self._view.lineEditName.setText(self._view.name)
        syllabus = network.getSyllabusFromEAS()
        self._view.showGrades(syllabus)
        
    def clear(self):
        model = QtGui.QStandardItemModel(0, 0)
        self._view.tableViewOutput.setModel(model)
        self._view.lineEditUsername.setText('')
        self._view.lineEditPassword.setText('')
        self._view.lineEditPasskey.setText('')
        self._view.lineEditName.setText('')
        self._view.progressBarTotal.setProperty("value", 0)
        self._view.showStatus('')
        
    def save(self):
        if self._view.file is None:
            return
        path = QtWidgets.QFileDialog.getSaveFileName(self._view.form, 'Save File')[0]
        try:
            self._view.file.to_csv(path, header = False, index=False)
        except FileNotFoundError:
            print('file not found')