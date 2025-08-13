# python has 2 loops
    # while loop
    # For loop

# WHILELOOP
# while loop is used to execute a block of code repeatedly as long as a given condition is true.
# Syntax:
# while condition:
#     code to be executed

# Example:
# i = 1
# while i <= 5:
#     print(i)
#     i += 1    # i = i + 1

# i = 1
# while i<=10:
#     print(i)
#     i+=1

# with break we can exit the loop prematurely
# Example
# i = 1
# while i <= 10:
#     if i == 5:
#         break  # Exit the loop when i is 5
#     print(i)
#     i += 1

# with continue we can skip the current iteration and continue with the next one
# Example
# i = 1
# while i <= 10:
#     i += 1
#     if i == 5:
#         continue  # Skip the current iteration when i is 5
#     print(i)

# with else we can execute a block of code after the loop completes normally (not interrupted by break)
# Example
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("Loop completed without interruption.")

# i = 1
# while i <= 10:
#     if i == 5:
#         break  # Exit the loop when i is 5
#     print(i)
#     i += 1
# else:
#     print("Loop completed without interruption.")

# Example of a while loop that counts down from 10 to 1
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1  # Decrement i by 1 each iteration

# Guess correct name:
# while True:
#     user_name = input("Enter your username: ")
#     if(user_name == "dharitri"):
#         print("Correct username")
#         break
#     else: 
#         print("Incorrect username!")
#         continue

# Questions:
# 1. Print numbers from 10 down to 1 using a while loop.
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# 2. Keep asking the user to enter a number until they enter a negative number, then stop.
# while True:
#     user_ip = int(input("Enter a number: "))
#     if(user_ip < 0):
#         print("You entered a negative number")
#         break
#     else:
#         continue

# 3. Write a program to calculate the sum of the first 50 positive integers using a while loop.
# i = 1
# total = 0
# while i <=50:
#     total += i
#     i += 1
# print(total)

# 4. Guess the number game:
#     Computer picks a number between 1-20.
#     User keeps guessing until correct.
# import random
# i = random.randint(1, 20)
# while True:
#     user_ip = int(input("Enter a number : "))
#     if(user_ip == i):
#         print(f"correct guess {user_ip}")
#         break

# 5: Multiplication table (e.g., for 7) using while.
# i = 1
# while i<=10:
#     print(f'7 x {i} = {7 * i}')
#     i += 1

# 6. Reverse a number
# user_ip = input("Enter a number: ")
# i = -1
# output = ""
# while -i <= len(user_ip):
#     output += user_ip[i]
#     i -= 1
# print(f'your input: {user_ip}')
# print(f'reserse of input: {output}')

# 7. Sum Until Total Exceeds Limit
# num = 100
# total = 0
# while True:
#     user_ip = int(input("Enter a number: "))
#     total += user_ip
#     if(total >= num):
#         print(total)
#         print(f"The sum of input numbers {total} exceeds the given number {num}")
#         break

# 8. Find First Number Divisible by 7 and 5
# user_ip = int(input("Enter a number: "))
# i = user_ip
# while i >= user_ip:
#     if i % 5 == 0 and i % 7 == 0:
#         print(f"{i} is divisible by both 5 and 7")
#         break
#     i += 1
