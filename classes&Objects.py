"""Basic Class Definitions

Slides – Key Concepts

__init__ method

Instance vs Class Attributes

Calling methods from objects"""


#Code Demonstrations

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.bark()
dog2.bark()

class Circle:
    pi = 3.1427  # Class attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

circle1 = Circle(5)
circle2 = Circle(10)

print("Area of Circle 1:", circle1.area())
print("Area of Circle 2:", circle2.area())

#Assignment

# Create a Book class and show book summary
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

book1.summary()
book2.summary()
