"""Design Patterns in OOP

Slides – Key Concepts

What are Design Patterns?

Types: Creational, Structural, Behavioral

Creational Pattern: Singleton

Structural Pattern: Adapter

Behavioral Pattern: Observer"""


#Code Demonstrations

#Singleton Pattern

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True

#Adapter Pattern

class OldPrinter:
    def print_text(self):
        print("Printing from Old Printer")

class NewPrinter:
    def modern_print(self):
        print("Printing from New Printer")

class PrinterAdapter:
    def __init__(self, printer):
        self.printer = printer

    def print_text(self):
        self.printer.modern_print()

old = OldPrinter()
new = PrinterAdapter(NewPrinter())

old.print_text()
new.print_text()  # Works like old

#Observer Pattern

class Subscriber:
    def update(self, message):
        print("Received:", message)

class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, message):
        for sub in self.subscribers:
            sub.update(message)

sub1 = Subscriber()
sub2 = Subscriber()

pub = Publisher()
pub.subscribe(sub1)
pub.subscribe(sub2)

pub.notify("New Article Available")

#Assignment

# Implement your own Singleton for Logger
class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)

logger1 = Logger()
logger2 = Logger()

logger1.log("System started.")
logger2.log("User logged in.")

print(logger1.logs)
print(logger1 is logger2)  # True
