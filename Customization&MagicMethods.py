"""Customization & Magic Methods

Slides – Key Concepts

__str__, __repr__

Operator Overloading (+, ==)

__len__, __getitem__, __contains__

Context Managers (__enter__, __exit__)"""


#Code Demonstrations

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has ${self.balance}"

    def __add__(self, other):
        return BankAccount(self.owner, self.balance + other.balance)

    def __eq__(self, other):
        return self.balance == other.balance

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)
merged = acc1 + acc2

print(merged)
print("Equal?", acc1 == acc2)
