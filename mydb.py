import sqlite3

from pandas.io import sql

# table course:
#   id  credit  attribute   property    obtain  start   finish
#
# table student:
#   id  name    password
#
# table grade
#   student_id    course_id   score
#
#
# Retrieve student grades
# Return (course_id, course_name, score, credit, attribute, property, obtain, start, finish)
# where student_id = id of student you want to find

class MyDB:
    def __init__(self, db):
        self._db = db
        
    def execute(self, sql):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            try:
                cur.execute(sql)
            except sqlite3.DatabaseError as error:
                print(error)
            con.commit()
                
    def insertIntoCourse(self, course):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.executemany('''insert or ignore into course values(?, ?, ?, ?, ?, ?, ?)''', course)
            con.commit()
            
    def insertIntoStudent(self, student):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.executemany('''insert or ignore into student values(?, ?, ?)''', student)
            con.commit()
            
    def insertIntoGrade(self, grade):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.executemany('''insert or ignore into grade values(?, ?, ?)''', grade)
            con.commit()
            
    def getGrades(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select course_id, score from grade where student_id=?", (student_id,))
            
            courses = cur.fetchall()
            for i, course in enumerate(courses):
                cur.execute('''select credit, attribute, property, obtain, start, finish from course where id=?''', (course[0],))
                courses[i] = course + cur.fetchone()
            #courses = list(map(lambda t:(t[0], t[2], t[1], t[3], t[4], t[5], t[6], t[7]), courses))
        return courses
    
    def exist(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select * from student where id=?", (student_id,))
            student = cur.fetchone()
        return student
    
    def checkPassword(self, student_id, password):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select password from student where id=?", (student_id,))
            return password == cur.fetchone()[0] 
        
    def deleteStudent(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("delete from student where id=?", (student_id,))
            cur.execute("delete from grade where student_id=?", (student_id,))
            con.commit()
            
    def getName(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select name from student where id=?", (student_id,))
            return cur.fetchone()[0]
            
if __name__ == "__main__":

    db = MyDB('mydb.db')
    '''
    student = [('8211190222', '袁宏远', None)]
    course = [('测量学', '2', None, None, None, None, None), ('地图学', '3', None, None, None, None, None)]
    grade = [('8211190222', '测量学', '90'), ('8211190222', '地图学', '92')]
    db.insertIntoCourse(course)
    db.insertIntoGrade(grade)
    db.insertIntoStudent(student)
    '''
    
    grades = db.getGrades('8211190222')
    #print(grades)
    #print(db.exist('8211190222'))
    #print(db.exist('8211190221'))
    #print(db.checkPassword('8211190207', 'sh15290222858'))
    db.deleteStudent('8211190207')