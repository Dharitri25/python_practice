
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# LIST
# used to store multiple items in a single variable
# buit-in datdtype
# Lists are mutable, can be changed, and can be modified, can be used to store any type of content
# List allows duplicate members
# Lists are ordered, meaning the items have a defined order, and that order will not change
# Lists are created using square brackets []
    # Example: my_list = [1, 2, 3, 'apple', 'banana']
# Lists can contain different data types, including other lists
    # Example: my_list = [1, 'apple', 3.14, [4, 5, 6]]
# Lists can be nested, meaning a list can contain other lists as elements
    # Example: my_list = [1, 2, [3, 4], 5]
# Lists can be empty, meaning they can have no elements
    # Example: my_list = []
# Lists can be accessed using indexing, where the first element is at index 0
    # Example: my_list[0] returns the first element of the list


# x = [1, 2, 3, 'apple', 'banana']
# print(type(x))  # type of the list
# print(len(x))  # length of the list
# print(x[0])  # first element
# print(x[:])  # all elements
# print(x[1:4])  # slicing the list
# print(x[:3])  # first three elements
# print(x[3:])  # last elements after index 3
# print(x[-2])  # second last element
# print(x[::1]) # print the list as it is
# print(x[::-1])  # reverse the list (sequence[start:end:step])
# print(x[1:4:2])  # slicing with step
# print(x[-1:-4:-1])  # reverse slicing

# LIST METHODS
# x[1] = 'orange'  # change the second element
# x.insert(2, 'kiwi')  # insert 'kiwi' at index 2
# x.append('grape')  # add 'grape' to the end of the list
# x.extend(['mango', 'peach'])  # add multiple elements to the end of the list
# x.remove('apple')  # remove 'apple' from the list
# x.pop(1)  # remove the element at index 1
# del x[0]  # delete the first element
# x.clear()  # remove all elements from the list
# print(x)  # modified list

# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(x[i]) # iterate through the list using index
#     print(f'{i}: {x[i]}')  # print the index and element (i, x[i])  # iterate through the list using index

# list comprehension
# newlist = [expression for item in iterable if condition == True]
# [print(i) for i in x] # list comprehension to print each element in the list
# new_list = [i for i in x if "a" in str(i)]  # create a new list with elements containing 'a'
# print(new_list)  # print the new list
# print([i for i in range(10)])
# print([str(i).upper() for i in x])
# print([i for i in x if isinstance(i, str)])  # create a new list with only string elements
# print([i for i in x if isinstance(i, int)])  # create a new list with only integer elements
# new_LIST = [i for i in x if isinstance(i, str)]  # create a new list with only string elements
# new_LIST.sort()
# print(new_LIST) 
# new_LIST.sort(reverse=True)  # sort the list in reverse order
# print(x[:])

# copy:
# copied = x  # shallow copy of the list (just creates a new name for the same list)
# copied = x.copy() # creates a new copy of the list

# join:
l1 = ['apple', 'banana', 'cherry']
l2 = ['orange', 'kiwi', 'melon']
# joined = l1 + l2
# print(joined)
# l1.extend(l2)
# print(l1)
# + creates a new list but does not modify the original list
# extend modifies the original list by adding elements from another iterable

# Methods     Description
# append()	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list
