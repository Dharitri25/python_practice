# TUPLE
# ()
# built-in data type
# immutable
# allowed multiple data types
# can be nested (1,2,3, (4,5,6), 'a', 'b', 'c')
# can be empty  ()
#  tuple() is used to create a tuple
# duplicate values are allowed (1, 2, 2, 3, 4)
# can be accessed using indexing, where the first element is at index 0
# Example: my_tuple = (1, 2, 3, 'apple', 'banana')

# x= (1, 2, 3, 'apple', 'banana')
# print(type(x))  # type of the tuple
# print(len(x))  # length of the tuple
# print(x[0])  # first element
# print(x[-1])  # last element
# print(x[:])  # all elements
# print(x[1:4])  # slicing the tuple
# print(x[::-1])  # reverse the tuple
# y = list(x) # convert tuple to list
# print(x)
# print(y)

# since tuples are immutable, we cannot change the elements of a tuple
# if we want to append or modify a tuple, we need to convert it to a list first
# y = list(x)  # convert tuple to list
# y[1] = 'orange'  # change the second element
# print(y)
# y.append('grape')  # add 'grape' to the end of the list
# y.extend(['mango', 'peach'])  # add multiple elements to the end
# x = tuple(y)  # convert list back to tuple
# print(x)  # modified tuple

# cannot remove items in a tuple.
# y = list(x)
# y.remove("apple")
# x = tuple(y)

# can delete the entire tuple
# del x  # delete the entire tuple
# print(x)  # this will raise an error since x is deleted

# tuple methods
# x = ('apple', 'banana')
# print(x.count('apple'))  # count the number of occurrences of 'apple'
# print(x.index('banana'))  # find the index of 'banana'   
# # print(x.index('orange'))  # this will raise an error since 'orange' is not in the tuple
# print(x.index('apple', 0, 2))  # find the index of 'apple' in the first two elements
# print(x.index('banana', 0, 2))  # this will raise an error since 'banana' is not in the first two elements
# (a,b) = x  # unpacking the tuple
# print(a, b)  # print the unpacked values

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (*green, tropic, red) = fruits
# print(green) #picks all elements except the last two
# print(tropic)
# print(red)

# Loop through a tuple
x = (1, 2, 3, 'apple', 'banana')
y = (4, 5, 6, 'orange', 'grape')
# for i in x:
#     print(i)  # iterate through the tuple

# for i in range(len(x)):
#     print(f'{i}: {x[i]}')  # iterate through the tuple using index

# while x:
#     print(x[0])  # print the first element
#     x = x[1:]  # remove the first element
# print(x)  # this will raise an error since x is now empty

# joined = x + y  # join two tuples
# joined = x.__add__(y)  # join two tuples using the add method
# joined = x * 2 # repeat the tuple twice
# print(joined)


# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
