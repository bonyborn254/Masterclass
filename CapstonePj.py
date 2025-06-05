"""Capstone Project – Student Management System

Slides – Key Concepts

Integrate: Classes, Inheritance, Encapsulation, Polymorphism

Design a scalable architecture

Optional Add-ons: File I/O, Exception Handling"""


#Code Demonstration

class Person:
    def __init__(self, name, email):
        self.name = name
        self._email = email  # Protected

    def display(self):
        print(f"Name: {self.name}, Email: {self._email}")

class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display(self):
        super().display()
        print(f"ID: {self.student_id}, Enrolled in: {', '.join(self.courses)}")

class Teacher(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

# Polymorphism in action
def show_profile(person):
    person.display()

s = Student("Alice", "alice@email.com", "S001")
s.enroll("Math")
s.enroll("Physics")

t = Teacher("Mr. John", "john@email.com", "Science")

show_profile(s)
show_profile(t)

#Assignment

# Extend the system:
# 1. Add Admin class who can add/remove students or teachers
# 2. Store all users in a list
# 3. Display all user details using polymorphic function

class Admin(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_id):
        self.users = [u for u in self.users if getattr(u, 'student_id', None) != user_id]

    def display_users(self):
        for user in self.users:
            user.display()
            print("------")

admin = Admin("Mrs. Smith", "admin@school.com")
student1 = Student("Bob", "bob@email.com", "S002")
teacher1 = Teacher("Ms. Jane", "jane@email.com", "Math")

admin.add_user(student1)
admin.add_user(teacher1)
admin.display_users()
