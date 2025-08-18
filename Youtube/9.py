# DELETE object
# del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name
    
# x = Student('DM')
# print(x)
# del x # x object of class Student is deleted
# print(x)


# Private(like) attributes & methods
# when you want to make an attribute or method private inside a class which can not be used outside of the class.
# add '__' before the name of the attribute or method
# example:
# class Person:
#     __name = 'Anonymous'
#     def __hello(self):
#         print("hello!")
    
#     def welcome(self):
#         return self.__hello()
# x = Person()
# # print(x.__name) # error cause name is private attribute
# # x.__hello() # error as hello() as private method can be accessed inside the class only
# x.welcome()


