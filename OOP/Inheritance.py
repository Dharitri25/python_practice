# Inheritance
# allows to define a class thats inherits all the methods and properties from another class
# Parent class is the class from which the methods and properties are being inherited.
# Child class is the class in whihc the methods and properties from parent class are being utilised.
# example:
# # parent class
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
    
#     def printname(self):
#         print(self.fname + " " + self.lname)
# x = Person('D', 'M')
# x.printname()

# # child class
# class Student(Person):
#     pass

# y = Student('Dharitri', 'Maharana')
# y.printname()


#  __init__() method: same as in classes
# when __init__() is being added to the child class, the chile will no longer inherit the parent's __init__()
# to make it inherited:
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname):
#         ...


# Super() function 
# this will make the child inherit all the methods and properties from it's parents
# example
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname) #this will inherit all the properties and functions from parent

# Add properties
