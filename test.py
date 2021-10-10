class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return None

    def get_name(self):
        print(self.name)

    def get_age(self):
        return self.age

s1 = Student("Cephas", 18)
s2 = Student("Adi", 18)
s2.get_name()