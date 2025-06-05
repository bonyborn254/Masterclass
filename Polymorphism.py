"""Polymorphism

Slides – Key Concepts

Method Overriding

Duck Typing

Abstract Base Classes (ABC)"""


#Code Demonstrations

class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

def animal_sound(animal):
    animal.make_sound()

animal_sound(Dog())
animal_sound(Cat())

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

ft_emp = FullTimeEmployee("Alice", 5000)
pt_emp = PartTimeEmployee("Bob", 20, 80)

print(f"{ft_emp.name}'s Salary: {ft_emp.calculate_salary()}")
print(f"{pt_emp.name}'s Salary: {pt_emp.calculate_salary()}")
