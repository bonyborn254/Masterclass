"""Composition

Slides – Key Concepts

Has-a relationship

Building objects from smaller components

When to use Composition vs Inheritance"""


#Code Demonstrations

class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def specs(self):
        print(f"CPU: {self.cpu.model}")
        print(f"RAM: {self.ram.size} GB")
        print(f"Storage: {self.storage.capacity} GB")

cpu = CPU("Intel i7")
ram = RAM(16)
storage = Storage(512)

comp = Computer(cpu, ram, storage)
comp.specs()
