# CLASSES / OBJECTS
# python is an object oriented language
# almost evrything in python is an object with its properties and methods
# Class in pytohn is like an object constructor, or a "blueprint" for creating objects

#examples of class:
# class MyClass:
#     c = 5

# o = MyClass()
# print(o.c)

# __init__() method
# built-in method
# all classes have a method called __init__(), which is always executed when calss is being initiated
# example:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Dharitri", 24)
# print(p1.name)
# print(p1.age)

# The __init__() method is called automatically everytime the class is being used to create a new object.

# __str__() method
# controls what should be returned when the class object is represented as a string
# if __str__() is not set, the string representation of the object is returned
# example:
# class Person:
#     def __init__(self, name, age): #sets value inside the method
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})" # returns the variable in a required form
# p1 = Person("Dharitri", 24)
# print(p1)

# create Methods:
# we can create own method
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myFunction(self):
#         print(f'Hello my name is {self.name}')
# p1 = Person("Dharitri", 24)
# p1.myFunction()

# The self parameter is a reference to the current instant if the class.
# self we can write anything
# self is the first parameter of any function in the class
# example:
# class Person:
#     def __init__(me, name, age):
#         me.name = name
#         me.age = age

#     def func(abc):
#         print("Hello my name is " + abc.name)
# p1 = Person("Dharti", 24)
# p1.func()

# Modify object property
# p1.age = 41

# Delete object properties
# del p1.age
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36) #object of class Person
# del p1.age
# print(p1.age) # throws error as no declaration of age as it just deleted.

# Delete Object
# del p1

# pass statement: class can not be empty, so when nothing is there, then use pass inside it
