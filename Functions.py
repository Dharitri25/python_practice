# FUNCTION
# function is a block of code which only runs when it is called
# we can pass parameters into a function
# 'def' keyword is used
# syntax:
# def function_name():
#     code block

# Example:
# def func():
#     print("me")
# func()

# Arguments: information passed in parameter () to be used inside a function. (order of args)
# Arbitrary Arguments: (*arg): when don't know how many argumnets are needed then *arg is used
    # This way the function will receive a tuple of arguments, and can access the items accordingly
    # Example:
    # def func(*kids):
    #     print("The youngest child is: "+ kids[2])
    # func("ma", "na", "la")

# Keyword Arguments (kwargs): we can send arguments with the key = value.
# here order of the arguments are not mandatory.
    # def func(a,b):
    #     print(a+b)
    # func(b="b", a="a")
# Arbitrary Keyword Arguments (**kwargs): same as *args
# synatx **args
    # def func(**arg):
    #     print(f'first name: {arg['fname']}')
    # func(fname = 'd', lname = 'm')

# default parameter: If we call the function without argument, it uses the default value
# def func (c = 'c'):
#     print(c)
# func()

# pass statemenet: function can not be empty.
# if no code inside the function, then use pass to avoid error
# def func():
#     pass

# Recursion
# Recursion is when a function calls itself — either directly or indirectly — to solve a problem.
# when a problem can be broken into smaller subproblems of the same type
# used in math problem, tree traversal, searching, sorting
# example:
# def countdown(n):
#     if n == 0:
#         print("Blast 🔥!")
#         return
#     else: 
#         print(n)
#         countdown(n - 1)

# countdown(5)

# Factorial:
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

# sum
# def sum_natural(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_natural(n-1)
# print(sum_natural(5))

