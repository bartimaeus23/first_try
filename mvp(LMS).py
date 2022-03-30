class User():
    __id = 0

    def __init__(self, name):
        User.__id += 1
        self.name = name


class Student(User):

    def __init__(self, name, admission_time):
        super().__init__(name)
        self.admission_time = admission_time
        self.courses = []
        self._marks = {
            1 : None,
            2 : None,
            3 : None
        }

        self.available_courses = CourseDatabase()

class Course():

    def __init__(self, name, id, teacher):
        self.name = name
        self.id = id
        self.teacher = teacher

class CourseDatabase():

    def __init__(self):
        self._courses = [
            {
                'id' : 1,
                'name' : 'Physics',
                'teacher' : 'Birulkin'
            },
            {
                'id': 2,
                'name': 'Math',
                'teacher': 'Alma'
            },
            {
                'id': 3,
                'name': 'Informatics',
                'teacher': 'Igory'
            }
        ]

    def create_course(self, name, id, teacher):
        new_course = {
            'id': id,
            'name': name,
            'teacher': teacher
        }
        self._courses.insert(id - 1, new_course)
        return Course(name, id, teacher)

class CourseEnrollment():
    __admissions_number = 0

    def __init__(self, student, course):
        CourseEnrollment.__admissions_number += 1
        self.student = student
        self.course = course

    def enrol_student(self):
        if type(self.student) == Student and type(self.course) == Course:
            self.student.courses.append(self.course)

class Exam():
    __studentpassed = 0

    def __init__(self, course_id):
        self.course_id = course_id

    def grade_student(self, student, mark):
        if type(student) == Student:
            student._marks[self.course_id] = mark

student1 = Student('Barti', 1894)
course_database1 = CourseDatabase()
course1 = course_database1.create_course('jym', 4, 'Raphi')
enrol1 = CourseEnrollment(student1, course1)
enrol1.enrol_student()
exam1 =Exam(2)
exam1.grade_student(student1, 5)
print(student1._marks)
print(course_database1._courses)


