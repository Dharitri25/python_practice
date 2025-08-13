# SET
# {}
# buit-in datatype
# mutable
# unordered
# unindexed
# no duplicate members
# allow multiple datatypes
# set() is used to create a set
# set items are unchangeable but you can add or remove items
    # Example: my_set = {1, 2, 3, 'apple', 'banana'}
# can be empty  set()
    # Example: my_set = set()
# The values False and 0 are considered the same value in sets, and are treated as duplicates
# can be accessed using iteration, but not indexing

x = {1, 2, 3, 'apple', 'banana'}
# print(type(x))  # type of the set
# print(len(x))  # length of the set
# print(x)  # print the set
# print('apple' in x)  # check if 'apple' is in the set
# print('orange' not in x)  # check if 'orange' is not in

# for i in x:
#   print(i)  # iterate through the set

# set methods
# x.add('orange')
# x.add('grape')  # add 'orange' and 'grape' to the set
# x.update(['mango', 'peach'])  # add multiple elements to the set
# x.remove('apple')  # remove 'apple' from the set
# x.discard('banana')  # remove 'banana' from the set
# print(x)  # modified set
# If the item to remove does not exist, remove() will raise an error. 
# If the item to remove does not exist, discard() will not raise an error.

# x.pop()  # remove and return an arbitrary element from the set
# print(x)  # modified set after pop
# x.clear()  # remove all elements from the set
# print(x)  # empty set after clear
# del x  # delete the entire set
# print(x)  # this will raise an error since x is deleted

# join sets
# x1 = {1, 2, 3, 4}
# x2 = {4, 5, 6}
# union |
# joined = x1.copy()  # create a copy of the first set
# joined.update(x2)  # add elements from the second set to the copy
# joined = x1.union(x2)  # join two sets
# joined = x1 | x2  # join two sets using the union operator
# intersection &
# joined = x1.intersection(x2)  # get common elements in both sets
# joined = x1 & x2  # get common elements in both sets using the intersection
# intersection_update
# joined = x1.intersection_update(x2)  # update x1 with common elements
# difference -
# joined = x1.difference(x2)  # get elements in x1 that are not in x2
# joined = x1 - x2  # get elements in x1 that are not in
# joined = x2.difference(x1)  # get elements in x2 that are not in x1
# joined = x2 - x1  # get elements in x1 that are not in
# joined = x1.difference_update(x2)  # update x1 with elements that are not in x2
# symmetric_difference ^
# joined = x1.symmetric_difference(x2)  # get elements that are in either set but not in both
# joined = x1 ^ x2  # get elements that are in either set but not in
# joined = x1.symmetric_difference_update(x2)  # update x1 with elements that are in either set but not in both
# print(joined)  # print the joined set

# Set Methods
# Method	            Shortcut	    Description
# add()	 	                        Adds an element to the set
# clear()	 	                        Removes all the elements from the set
# copy()	 	                        Returns a copy of the set
# difference()	        -	        Returns a set containing the difference between two or more sets
# difference_update()	    -=	        Removes the items in this set that are also included in another, specified set
# discard()	 	                    Remove the specified item
# intersection()	        &	        Returns a set, that is the intersection of two other sets
# intersection_update()	&=	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                Returns whether two sets have a intersection or not
# issubset()	            <=	        Returns True if all items of this set is present in another set
#  	                    <	        Returns True if all items of this set is present in another, larger set
# issuperset()	        >=	        Returns True if all items of another set is present in this set
#  	                    >	        Returns True if all items of another, smaller set is present in this set
# pop()	 	                        Removes an element from the set
# remove()	 	                    Removes the specified element
# symmetric_difference()	^	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	                |	        Return a set containing the union of sets
# update()	            |=	        Update the set with the union of this set and others

