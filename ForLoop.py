# FOR LOOP
# for loop is used for iterating over a sequence (list, tuple, dict, set, string)
# using in oops
# with for loop, we can execute a statement once for each item in a list, tuple, set etc.
# Syntax:
    # for iterating_variable in list:
    #     code to execute
# Example:
# fruits = ['apple', 'guava', 'grape', 'mango']
# for i in fruits:
#     print(i)
# for i in range(len(fruits)):
#     print(fruits[i])
# Reverse = []
# for i in range(len(fruits)):
#     j = len(fruits) - i
#     print(fruits[j-1])
#     Reverse.append(fruits[j-1])
# print(Reverse)


# with continue statement, we can stop the current iteration of the loop and continue with the next one.
# Example:
# fruits = ['apple', 'guava', 'grape', 'mango']
# for i in fruits:
#     if i == "apple":
#         continue
#     print(i)


# else in for loop specifies a block of code to be executed when the loop is finished
# else block will not be executed if the loop is stopped by 'break' statement.
# Example:
# for x in range(6):
#     print(x)
# else:
#     print("range finished")

# for x in range(5):
#     if(x == 3): 
#         break
#     print(x)
# else:
#     print("sddsf")


# Nested for loop:
# loop inside a loop
# the inner loop will be executed one time for each iteration of the 'outer loop'
# Example:
# adj = ['big','red', 'tasty']
# fruits = ['apple', 'cherry', 'pomegranut']
# for x in fruits:
#     for y in adj:
#         print(f'{x} is {y}')


# pass statement:
# for loop can not be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
# Example:
# for x in [0,2,4]:
#     pass


# Questions:
# Simple
# 1. Print numbers from 1 to 10.
# for i in range(10):
#     print(i+1)


# 2. Print even numbers from 2 to 20.
# for i in range(21):
#     if(i != 0 and i % 2 == 0):
#         print(i)


# 3. Print the squares of numbers from 1 to 5.
# for i in range(5):
#     print((i+1) ** 2)


# 4. Print all elements of a list.
# x = [1,2,3,4,5,4,4]
# for i in x:
#     print(i)


# 5. Print characters of a given string one by one.
# txt = 'dharitri' 
# for i in txt:
#     print(i)


# Moderate
# 6: Print all odd numbers between 1 and 50.
# for i in range(50):
#     i += 1
#     if i % 2 != 0:
#         print(i)


# 7: Calculate the sum of numbers from 1 to 100.
# total = 0
# for i in range(1, 100):
#     total += i
# print(total)


# 8. Print the multiplication table of a given number.
# user_ip = int(input("Enter a number: "))
# print(user_ip)
# for i in range(10):
#     print(f'{user_ip} x {i+1} = {user_ip*(i+1)}')


# 9. Print numbers in reverse order from 10 to 1.
# for i in range(10):
#     print(10 - i)


# 10. Print elements of a list in reverse order without using reversed() or slicing.
# x = ['apple', 'banana', 'cherry', 'guava']
# y = []
# for i in range(len(x)):
#     # print(x[(len(x)-i)-1])
#     y.append(x[(len(x)-i)-1])
# print(y)


# 11. Print only prime numbers between 1 and 50.
# for i in range(2, 50):
#     is_prime = True
#     for j in range(2, int(i ** 0.5)+1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)


# 12. Print all numbers between 1 and 100 that are divisible by both 3 and 7.
# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i)


# 13. Count how many vowels are in a given string.
# vowel = ['a', 'e', 'i', 'o', 'u']
# user_ip = input("Enter a string: ")
# print(user_ip)
# count = 0
# for i in range(len(user_ip)):
#     if user_ip[i] in vowel:
#         print(user_ip[i])
#         count += 1
# print(f'{count} vowels present in given word')

# to count unique vowel
# vowel = ['a', 'e', 'i', 'o', 'u']
# user_ip = input("Enter a string: ")
# print(user_ip)
# txt = []
# count = 0
# for i in range(len(user_ip)):
#     if user_ip[i] in vowel and user_ip[i] not in txt:
#         print(user_ip[i])
#         txt.append(user_ip[i])
#         count += 1
# print(f'{count} unique vowels present in given word')

# to get vowels in dict with count of each vowel
# vowel = ['a', 'e', 'i', 'o', 'u']
# user_ip = input("Enter a string: ")
# txt = {}
# for i in range(len(user_ip)):
#     if user_ip[i] in vowel:
#         if user_ip[i] not in txt.keys():
#             txt.update({user_ip[i]: 1})
#         else:
#             txt[user_ip[i]] += 1  
# print(txt)