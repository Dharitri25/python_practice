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


# QUESTION:
# 1. Write a function greet_user(name) that takes a name and prints "Hello, <name>!".
# def greet_user(name):
#     print(f'Hello, {name}!')
# greet_user('Dharitri')


# 2. Write a function square(num) that returns the square of a given number.
# def square(num):
#     return num ** 2
# print(square(2))


# 3. Write a function is_even(num) that returns True if the number is even, otherwise False.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(6))


# 4. Write a function sum_two_numbers(a, b) that returns the sum of two numbers.
# def sum_two_numbers(a, b):
#     return a + b
# print(sum_two_numbers(3,5))


# 5. Write a function factorial_iterative(n) that returns the factorial of n using a for loop.
# def factorial_iterative(n):
#     j = 1
#     if n == 0:
#         return 1
#     for i in range(1,n+1):
#         j *= i
#         i += 1
#     return j
# print(factorial_iterative(6))


# 6. Write a function find_max(a, b, c) that returns the largest of three numbers.
# def find_max(a, b, c):
#     if a > b and a > c:
#         print("largest: ", a)
#     elif b > a and b > c:
#         print("largest: ", b)
#     else:
#         print("largest: ", c)
# find_max(12, 3, 6)


# 7. Write a function count_vowels(string) that returns the number of vowels in a given string.
# def count_vowels(string):
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for i in range(len(string)):
#         if string[i].lower() in vowels:
#             count += 1
#     return count
# print(count_vowels('dhAritri')) 


# 8. Write a function reverse_string(s) that returns the reversed version of a string.
# def reverse_string(s):
#     txt = ""
#     for i in range(1,len(s)+1):
#         txt += s[len(s) - i]
#     return txt
# print(reverse_string('dharitri'))


# 9. Write a function is_palindrome(s) that checks if the string is a palindrome.
# def is_palindrome(s):
#     is_True = False
#     if len(s) == 1:
#         is_True = True
#     if len(s) == 2 and s[0] == s[-1]:
#         is_True = True
#     for i in range(1, len(s) + 1):
#         if s[i-1] == s[len(s) - i]:
#             is_True = True
#         else:
#             is_True = False
#     print(is_True)
# is_palindrome('dhar')


# 10. Write a function multiplication_table(n) that prints the multiplication table of a number n.
# def multiplication_table(n):
#     for i in range(10):
#         print(f'{n} x {i + 1} = {n * (i+1)}')
# multiplication_table(7)


# 11. Write a function sum_list(numbers) that returns the sum of all elements in a list.
# numbers = [1,5,6,2]
# def sum_list(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         total += numbers[i]
#     print(total)
# sum_list(numbers)


# 12. Write a function find_min_max(numbers) that returns both the smallest and largest number in a list.
# def find_min_max(numbers):
#     smallest = largest = numbers[0]
#     for i in numbers[1:]:
#         if i < smallest:
#             smallest = i
#         elif i > largest:
#             largest = i
#     print(f'smallest number: {smallest}')
#     print(f'largest number: {largest}')
# find_min_max([21,3,14])

# def find_min_max(numbers):
#     print(f'smallest: {min(numbers)}')
#     print(f'largest: {max(numbers)}')
# find_min_max([33,23,43])

# def find_min_max(numbers):
#     sortedNum = sorted(numbers)
#     print(f'smallest: {sortedNum[0]}')
#     print(f'largest: {sortedNum[-1]}')
# find_min_max([4,3,5])


# 13. Write a function remove_duplicates(lst) that removes duplicate items from a list.
# def remove_duplicates(lst):
#     temp = []
#     for i in lst:
#         if i not in temp:
#             temp.append(i)
#     print(temp)
# remove_duplicates([2,3,2,4])


# 14. Write a function count_occurrences(lst, value) that counts how many times value appears in lst.
# def count_occurrences(lst, value):
#     count = 0
#     for i in lst:
#         if i == value:
#             count += 1
#     print(f'{value} occurs {count} times in {lst}')
# count_occurrences([2,3,3,3,5], 3)


# 15. Write a function second_largest(numbers) that returns the second largest number in a list.
# def second_largest(numbers):
#     sortedNum = sorted(numbers)
#     print(f'second largest number {sortedNum[-2]}')
# second_largest([3,5,2,65,33])


# 16. Write a recursive function factorial_recursive(n) to calculate factorial.
# def factorial_recursive(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# print(factorial_recursive(6))


# 17. Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
# def fibonacci(n):






# LAMBDA Function:
# variable = lambda arg : expression
# lambda function is shown powerful when being used inside a function as an anonymous function.
# example:
# x = lambda a: a +10
# print(x(5))

# x = lambda a,b, c:a+b+c
# print(x(9,10,11))

# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2) #n = 2
# print(mydoubler(11)) # a = 11

# def myFunc(n):
#     return lambda a : a * n
# getDouble = myFunc(2)
# getTripple = myFunc(3)

# print(getDouble(2))
# print(getTripple(3))
