
"""✅ MODULE 4: Inheritance

Slides – Key Concepts

Parent & Child classes

Using super()

Multiple Inheritance"""


#Code Demonstrations

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

Assignment

# Create Vehicle -> Car with inheritance
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Model: {self.model}")

car = Car("Toyota", 180, "Corolla")
car.display_info()
