class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def avg_grade(self):
        value = 0
        
        for student in self.students:
            value += student.get_grade()
        return value/3

s1 = Student("Cep", 18, 96)
s2 = Student("Ray", 18, 86)
s3 = Student("Hope", 23, 76)

Course1 = Course("CS", 3)

Course1.add_student(s1)
Course1.add_student(s2)
Course1.add_student(s3)


print(Course1.avg_grade())


       
        
