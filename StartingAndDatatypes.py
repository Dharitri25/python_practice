# import sys
# print(sys.version)
# print(sys.argv)
# print("Dharitri")

# syntax 
# if 2>1:
#     print("2 is greater than 1")
# else:
#     print("2 is not greater than 1")

## Variables
# type
# x = 2
# x='dd'
# print(x, type(x))

#multiple variables
# x,y,z=1,'d2',3.0
# print(x,y,z)

# x=y=z= '1'
# print(x,y,z)

'''print('sdsdsdsd')
sdsds'''

# print('j','k')

# DATA TYPES
# Text:	str
# Numeric :	int, float, complex
# Sequence : list, tuple, range
# Mapping: dict
# Set :	set, frozenset
# Boolean: bool
# Binary : bytes, bytearray, memoryview
# None:	NoneType

# number
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# x=1.0
# print(type(x))
# y=int(x)
# print(x,y)
# complex numbers can not be converted into any other type

# random
# import random
# print(random.randrange(1,10))

# string
# a = "Hello, World!"
# # print(a[5])
# print(len(a))

# for x in "banana":
#   print(x)

# x= 'dharitri m'
# print('i' in x)
# print('i' not in x)
# print(x[1:4])
# print(x[:4])
# print(x[2:])
# print(x[-5:-2])
# print(x[::-1])
# print(x.upper())
# print(x.lower())
# print(x.strip())
# print(x.replace('d','s'))
# print(x.split(" "))

# y= 'dharitri'
# print(y.rjust(20,'.'))
# print(y.center(21))
# print(y.ljust(20,'.'))
# print(y.ljust('.', 20)) # wrong, exp: first argument must be integer and a complex or float one.
# ............dharitri
#       dharitri      
# dharitri............
# ............dharitri
#        dharitri      // center for dharitri with odd number.But somehoe 
# dharitri............
# print(x + " " + y)

# x='dharitri'
# y='dharitri'
# print(x == y)
# print(x != y)

# x='dharitri'
# y='dharitri'
# print(x is y)
# print(x is not y)

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)

# 'f' string
# x=15
# print(f'The value of x is {x}')

# escape string
# print('dharitri\nmaharana') # new line
# print('dharitri\tmaharana') #tab add
# print('dharitri\\maharana') #back slash between words
# print('dharitri\'maharana') #single quote also wrten ass " ' "
# print('dharitri\"maharana') #double quote
# print('dharitri\rmaharana') #
# print('dharitri\bmaharana') # backspace last char of the left side word got vanished
# print('dharitri\vmaharana') # vertical tab #almost kie a \n for nes word
# print('dharitri\fmaharana') # form feed
# \ooo -> ovtal
# \xhh -> hex
# \Uxxxxxxxx -> unicode

# STRING MEthODS
# x='dharitri'
# print(x.capitalize()) #first letter capital
# print(x.upper()) # all capital
# print(x.isupper())
# print(x.lower()) # all small (local use only on A-Z)
# print(x.casefold()) # all small (international use on any language)
# print(x.islower()) # true or false on all small
# print(x.strip()) # remove white space
# print(x.replace('d','s')) # replace
# print(x.split(' ')) # split
# print(x.count('d')) # count
# print(x.count('r')) 
# print(x.find('e')) # find and return the position (if not found then returns -1)
# print(x.endswith('i')) # true or false
# print(x.startswith('d')) # true or false
# print(x.index('i')) # find and return the position (if not found then returns error
# print(x.rindex('i'))
# print(x.join('s y')) #sdharitri dharitriy
# print(x.join('aa')) #adhritria
# print(x.partition('i')) # return tuple
# print(x.rpartition('i'))
# print(x.ljust(20,'.'))
# print(x.rjust(20,'.'))
# print(x.isnumeric()) # true or false
# print(x.isalpha()) # true or false
# print(x.isalnum()) # true or false
# print(x.isdecimal()) # true or false
# print(x.maketrans('d','s'))

# BOOLEAN
# x = "Hello"
# y = 0

# print(bool(x))
# print(bool(y))
# 0 # False
# None # False
# '' # False
# print(bool(0.0)) # False
# False # False
# 1 # True
# 'dharitri' # True
# True # True
# print(bool(' ')) # True

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))
# print(bool(set()))
# print(bool(frozenset()))
# print(bool(0j))