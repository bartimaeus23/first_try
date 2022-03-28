class Course():
    student_count = 0

    def __init__(self, name, amp_diligence):
        self.name = name
        self.amp_diligence = amp_diligence

    def grade_student(self, name, diligence):
        grade = self.amp_diligence * diligence
        print(name + ' has ' + str(grade) + ' on ' + self.name)

    def __str__(self):
        return str(self.name)


class User():
    __last_id = 1

    def __init__(self, name, age):
        User.__last_id += 1
        self.name = name
        self.__id = User.__last_id
        self.age = age
        self.course = ''
        Course.student_count += 1

    def enroll_course(self, course):
        if type(course) == Course:
            self.course = course
            print('Student applied for course of ' + str(self.course))
            return self.course


# creating course
# creating  user
# user's method - giving him his course
user1 = User('Ivan', 34)
course1 = Course('Phylosophy', 666)
user1.enroll_course(course1)
course1.grade_student('Ivan', 1000)