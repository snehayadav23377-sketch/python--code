class animal:
  def sound(self):
    print("The animal makes a sound")
class dog(animal):
    def sound(self):
        print("The dog barks")

class Student:
    def display(self):
        print("Hello, Student!")

s = Student()
s.display()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s = Student("Sneha", 20)
s.show()

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Sneha")

print(s1.school)
print(s2.school)


class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()

class Student:
    def __init__(self):
        self.__marks = 90

    def show(self):
        print(self.__marks)

s = Student()
s.show()









        
