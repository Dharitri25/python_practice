# DICTIONARY
# {key: value}
# collection of key-value pairs
# keys must be unique and immutable
# values can be of any type and can be duplicated
# dictionaries are unordered, changeable, and indexed
# dictionaries are created using curly brackets {}
    # Example: my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# can be empty  {}
    # Example: my_dict = {}
# can be accessed using indexing, where the key is used to access the value
    # Example: my_dict['name'] returns the value of 'name' in the dictionary
# can be modified using indexing, where the key is used to modify the value
    # Example: my_dict['name'] = 'Jane' changes the value of 'name' in the dictionary to 'Jane'
# can be deleted using the del keyword, where the key is used to delete the key-value pair
    # Example: del my_dict['name'] deletes the key-value pair with key 'name' from the dictionary   
# can be iterated through using a for loop, where the key is used to access the value   
# Example: for key in my_dict: print(key, my_dict[key]) prints all key-value pairs in the dictionary
# can be nested, meaning a dictionary can contain other dictionaries as values
    # Example: my_dict = {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'state': 'NY'}}

x = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(type(x))  # type of the dictionary
# print(len(x))  # length of the dictionary
# print(x['name'])  # access value by key
# print(x)  # print the dictionary
# print('name' in x)  # check if 'name' is in the dictionary
# print('apple' not in x)  # check if 'apple' is not in the dictionary
# i = x.get('name')  # get value by key, returns None if key does not exist
# print(i)  # print the value of 'name'
# print(x.keys())
# print(x.values())  # print all values in the dictionary
# print(x.items())  # print all key-value pairs in the dictionary
# x['name'] = "dharitri"
# print(x)

# loop
# for key in x:
#     print(key, x[key])  # iterate through the dictionary and print key-value pairs

# x.update({'name': 'Jane', 'country': 'USA'})  # add or update key-value pairs
# print(x)  # modified dictionary
# x['dsa'] = 'USA'
# print(x)
# x.pop('age')
# print(x)
# x.popitem()  # remove and return the last inserted key-value pair
# print(x)
# del x['city']  # delete a specific key-value pair
# print(x)  # modified dictionary after deletion
# x.clear()  # remove all key-value pairs from the dictionary
# print(x)  # empty dictionary after clearing
# del x  # delete the entire dictionary
# print(x)  # this will raise an error since x is deleted
# myDi = x.copy()
# v = x
# print(myDi)
# print(x is v) #true
# print(myDi is x) #false

# nested = {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'state': 'NY'}}
# print(nested['address']['city'])  # access nested value
# print(nested['address']['country'])  # this will raise an error since 'country
# print(nested , x)
# print(nested.get('address', {}).get('country', 'Not Found'))  # safely access nested value with default
# print(nested['address']['city'])

# Methods
# Method	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()    Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary
