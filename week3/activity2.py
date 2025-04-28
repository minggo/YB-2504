# Create students, record their grades, and show results.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show(self):
        print(f"Student: {self.name}, Grades: {self.grades}")

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print("Students in the school:")
        for student in self.students:
            student.show()

student1 = Student('Tom')
student1.add_grade(85)
student1.add_grade(80)


student2 = Student('Jerry')
student2.add_grade(78)
student2.add_grade(90)

school = School()
school.add_student(student1)
school.add_student(student2)
school.show_students()