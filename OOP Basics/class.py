class Student:
    species = 'Homo sapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'


student1 = Student('John', 20)
student2 = Student('Jane', 21)

print(student1)
print(student2)