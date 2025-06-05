"""Encapsulation

Slides – Key Concepts

Access Modifiers: Public, Protected, Private

Getters and Setters"""


#Code Demonstrations

class Person:
    def __init__(self, name, age):
        self.name = name              # Public
        self._email = "hidden@email" # Protected
        self.__password = "1234"     # Private

    def show_info(self):
        print(f"Name: {self.name}, Email: {self._email}")

    def get_password(self):
        return self.__password

p = Person("Alice", 30)
print(p.name)
print(p._email)  # Discouraged, but works
# print(p.__password)  # Raises AttributeError
print(p.get_password())

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

acc = Account("Bob", 1000)
print(acc.get_balance())
acc.set_balance(1500)
print(acc.get_balance())
acc.set_balance(-500)  # Should trigger error

