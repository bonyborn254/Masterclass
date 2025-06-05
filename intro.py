"""✅ MODULE 1: Introduction to OOP

Slides – Key Concepts

What is OOP?

OOP vs Procedural Programming

4 Pillars of OOP: Encapsulation, Inheritance, Polymorphism, Abstraction

Benefits: Modularity, Reusability, Scalability

Visual: Diagram comparing Procedural vs OOP styles"""


#Code Demonstration

#Procedural Style

students = []

def add_student(name, age):
    students.append({'name': name, 'age': age})

def show_students():
    for student in students:
        print(f"{student['name']} is {student['age']} years old.")

add_student("Alice", 20)
add_student("Bob", 22)
show_students()

OOP Style

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old.")

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.show()
student2.show()

Assignment

# a) Create a Car class with attributes: make, model, year
# b) Instantiate 3 Car objects and print their details
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} ({self.year})")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mustang", 2022)
car3 = Car("Tesla", "Model 3", 2023)

car1.display_info()
car2.display_info()
car3.display_info()
