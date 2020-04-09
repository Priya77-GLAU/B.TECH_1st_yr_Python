#=======================================PYTHON SETS METHODS===================================================
#=============================================================================================================

#1.> add() =>  Add an element to the set.    
fruit_set = {"apple", "banana", "orange"}
fruit_set.add("cherry")
print(fruit_set)


#1.> clear() =>  Remove all elements from the set.
fruit_set = {"apple", "banana", "orange"}
fruit_set.clear()
print(fruit_set)


#1.> copy()    =>  Copy the fruits set.
fruit_set = {"apple", "banana", "orange"}
fruit_set_new = fruit_set.copy()
print(fruit_set_new)


#2.> difference()   =>  Return a set that contains the items that only
#                       exist in set1, and not in set2.
fruit_set = {"apple", "banana", "orange"}
fruit_set2 = {"apple", "banana", "papaya"}
fruit_set_new = fruit_set.difference(fruit_set2)
print(fruit_set_new)


#3.> difference_update()   =>  Remove the items that exist in both sets.
fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set_new = fruit_set.difference_update(fruit_set2)
print(fruit_set_new)


#4.> discard()  =>  Remove "banana" from the set.
fruit_set = {"apple", "banana", "orange"}
fruit_set.discard("banana")
print(fruit_set)


#5.> intersection() =>  Return a set that contains the items that
#                       exist in both set1, and set2.
fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set_new = fruit_set.intersection(fruit_set2)
print(fruit_set_new)

# Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)


#6.> intersection_update()  =>  Remove the items that is not present in both set1, and set2.
fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set_new = fruit_set.intersection_update(fruit_set2)
print(fruit_set_new)

#Compare 3 sets, and return a set with items that is present in all 3 sets.
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)


#7.> isdisjoint()   =>  Return True if no items in set1 is present in set2.
fruit_set = {"apple", "banana", "orange"}
dairy_set2 = { "milk", "butter", "bread"}
fruit_set_new = fruit_set.isdisjoint(fruit_set2)
print(fruit_set_new)


#8.> issubset() =>  Return True if all items set1 are present in set2.
fruit_set = {"apple", "banana"}
fruit_set2 = { "apple", "cherry", "banana", "orange"}
fruit_set_new = fruit_set.issubset(fruit_set2)
print(fruit_set_new)


#9.> issuperset()   =>  Return True if all items set2 are present in set1.
fruit_set = { "apple", "cherry", "banana", "orange"}
fruit_set2 = {"apple", "banana"}
fruit_set_new = fruit_set.issubset(fruit_set2)
print(fruit_set_new)



#10.> pop() =>  Remove a random item from the set.
fruit_set = {"apple", "banana", "orange"}
fruit_set.pop()
print(fruit_set)


#11.> remove()  =>  Remove "banana" from the set.
fruit_set = {"apple", "banana", "orange"}
fruit_set.remove("apple")
print(fruit_set)


#12.> symmetric_difference()    =>  Return a set that contains all items from both sets,
#                                   except items that are present in both sets.

fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set_new = fruit_set.symmetric_difference(fruit_set2)
print(fruit_set_new)


#13.> symmetric_differece_update()  =>  Remove the items that are present in both sets,
#                                   AND insert the items that is not present in both sets.

fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set_new = fruit_set.symmetric_difference_update(fruit_set2)
print(fruit_set_new)


#14.> union()  =>  Return a set that contains all items from both sets, duplicates are excluded.
fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set_new = fruit_set.union(fruit_set2)
print(fruit_set_new)

# Unify more than 2 sets.
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)


#15.> update()  =>  Insert the items from set2 into set1.-
fruit_set = {"apple", "banana", "orange"}
fruit_set2 = { "cherry", "banana", "orange"}
fruit_set.update(fruit_set2)
print(fruit_set)


#=================================================END=========================================================


#______________________PTR's (Points to remember)______________________________________________________________

'''
1.)
This method is different from the remove() method, because the remove() method
will raise an error if the specified item does not exist, and the discard()
method will not. (SET)

2.)
Note: The pop() method returns removed value. (SET)
'''














