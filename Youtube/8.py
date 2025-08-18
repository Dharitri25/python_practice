# OOP in Python:
# to map with real world scenario, we started using objects in code
# this is object oriented language

# procedural language < functioanl language < oop
# lists, string are object

# Class and Object in python
# blueprint for an object
# name starts with capital letter

# Object is an instance of the class

# __init__():
# all classes have a function called __init__(), which is alway executed when the class is being executed

# class Student:
#     name = 'dharitri'
#     def __init__(self):
#         print("hi hello")

# c = Student()
# paranthesis are added to call the class and __init__() will be called automatically

# class Student:
#     college_name = "ABC College"

#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         print("New student is getting added!!")
    
# x = Student('Dharitri', 24, 8.9)
# print(f'{x.name}({x.age}) having {x.marks}marks')

# Methods
# class stores two type of things:
#     attributes: data about the object
#     methods: functions that belong to objects

# Questions
# create a class which takes name and marks of three subjects of the student and also define a method to print average mark
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def printAvg(self):
#         totalmarks = sum(self.marks.values())
#         totalSub = len(self.marks.keys())
#         print({totalmarks, totalSub})
#         avg = int(totalmarks / totalSub)
#         print(f'Average marks of {self.name} is {avg}')
    
# marks = {'eng': 89, 'mth': 97, 'phy': 90}
# x = Student('Dharitri', marks)
# x.printAvg()


# Static Methods
# methods those don't use the self parameter
# these work at class level and not in object level
# Example:
# class Student:
#     @staticmethod
#     def college():
#         print("ABC College")
# x = Student()
# x.college()


# DECORATOR:
# A decorator in python is simply a function that takes another function as input, adds some extra functionality and returns a new function.


# Questions:
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
# class Account:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
    
#     def debit(self, cash):
#         self.balance -= cash
#         print(f"{cash} amount is debited from account no. {self.acc_no}. balance is {self.balance}")
    
#     def credit(self, cash):
#         self.balance += cash
#         print(f"{cash} is credited to account no. {self.acc_no}. Balance is {self.balance}")
#     def checkBalance(self):
#         print("Your available balance is: ", {self.balance})

# x = Account(1200, 1234567890)
# x.debit(200)
# x.credit(100)
# x.checkBalance()

