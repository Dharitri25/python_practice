
# four pillars of oop in python
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism



# Abstraction:
# hiding unnecessary data and show only required data
# example:
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clt = False
#     def startCar(self):
#         self.acc = True
#         self.brk = True
#         print("Car started")
# x = Car()
# x.startCar()



# Encapsulation:
# wrap attributes and functions or methods with in a class.
# normally used in creating class
# example:
# class Student:
#     clg = "ABC College" #variable or attribute
#     def __init__(self, name):
#         self.name = name
    
#     def getName(self): #function or method
#         print(f'Student name is {self.name} from {self.clg}')

# x = Student('DM')
# x.getName()



# Inheritance
# when one class(child/derived) derives the attributes(properties/methods) of another class(parent/base)
# syntax -> class ChildClass(ParentClass)
# types of Inheritance:
    # Single Inheritance 
    # Multi-level Inheritance
    # Multiple Inheritance

# example:
# Single inheritance
# class Car:
#     color = "red"
#     @staticmethod
#     def start():
#         print("Car started")
    
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
# x = ToyotaCar('fortuner')
# print(x.name) #child attribute
# print(x.color) #parent attribute taken by child
# x.start() #parent method taken by child


# Multi-level inheritance
# class Car:
#     color = 'red'
#     @staticmethod
#     def start():
#         print('car started')
#     @staticmethod
#     def stop():
#         print('car stopped')

# class ToyotaCar(Car):
#     brand = 'Toyota'
#     def __init__(self):
#         self.brand = brand
# class Fortuner(ToyotaCar):
#     def __init__(self, model):
#         self.model = model
# x = Fortuner('f1')
# print(x.model) #child attr
# print(x.brand) #parent attr
# x.start() #grandparent method


# Multiple Inheritance
# class A:
#     varA = 'A'
# class B:
#     varB = 'B'
# class C(A,B):
#     varC = 'C'
# x = C()
# print(x.varC)
# print(x.varB)
# print(x.varA)



# Super()
# class Car():
