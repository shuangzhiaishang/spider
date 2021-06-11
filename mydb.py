import sqlite3

# table course:
#   id  name  credit  attribute   property
#
# table student:
#   id  name  password
#
# table grade
#   student_id    course_id   score  obtain  start finish
# 
# table syllabus
#   student_id    course_name   day_of_week     time_of_day
#
#
# Retrieve student grades
# Return (course_id, course_name, score, credit, attribute, property, obtain, start, finish)
# where student_id = id of student you want to find
#
# Retrieve syllabus
# Return (course_name, day_of_week, time_of_day)

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
            cur.executemany('''insert or ignore into course values(?, ?, ?, ?, ?)''', course)
            con.commit()
            
    def insertIntoStudent(self, student):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.executemany('''insert or ignore into student (id, name, password) values(?, ?, ?)''', student)
            con.commit()
            
    def insertIntoGrade(self, grade):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.executemany('''insert or ignore into grade values(?, ?, ?, ?, ?, ?)''', grade)
            con.commit()
            
    def insertIntoSyllabus(self, syllabus):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.executemany("insert into syllabus values(?, ?, ?, ?)", syllabus)
            con.commit()
            student_id = syllabus[0][0]
            cur.execute("update student set syllabus='exist' where id=?", (student_id,)) 
        
            
    def getGrades(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select course_id, score, obtain, start, finish from grade where student_id=?", (student_id,))
            
            grades = cur.fetchall()
            print(grades)
            for i, course in enumerate(grades):
                cur.execute('''select name, credit, attribute, property from course where id=?''', (course[0],))
                grades[i] = course + cur.fetchone()
            #courses = list(map(lambda t:(t[0], t[2], t[1], t[3], t[4], t[5], t[6], t[7]), courses))
        return grades
    
    def login(self, student_id, password):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select password from student where id=?", (student_id,))
            return password == cur.fetchone()[0] 
        
    def deleteStudent(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("delete from student where id=?", (student_id,))
            cur.execute("delete from grade where student_id=?", (student_id,))
            cur.execute("delete from syllabus where id=?", (student_id,))
            con.commit()
            
    def getName(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select name from student where id=?", (student_id,))
            return cur.fetchone()[0]
        
    def getSyllabus(self, student_id):
        with sqlite3.connect(self._db) as con:
            cur = con.cursor()
            cur.execute("select course_name, day_of_week, time_of_day from syllabus where student_id=?", (student_id,))
            syllabus = cur.fetchall()
        return syllabus
            
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
    
    grades = db.getGrades('8211190207')
    print(grades)
    #print(grades)
    #print(db.exist('8211190222'))
    #print(db.exist('8211190221'))
    #print(db.checkPassword('8211190207', 'sh15290222858'))
    #db.deleteStudent('8211190207')
    #student = [('8211190220', '袁宏远', None)]
    #db.insertIntoStudent(student)
    #syllabus = [('8211190207', '地图学', '四', '3-4')]
    #db.insertIntoSyllabus(syllabus)
    #print(db.existSyllabus('3'))
    #print(db.existSyllabus('8211190207'))
    #syllabus = db.getCourseSchedule('2')
    #print(syllabus)