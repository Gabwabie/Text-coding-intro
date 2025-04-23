#Different types of sets in Python
# Set of integers
# my_set = {1, 2, 3}
# print(my_set)

#Set of mixed datatypes
# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

#Set cannot have duplicates
# my_set = {1, 2, 3, 4, 3, 2}
# print(my_set)

#We can make set from a list
# my_set = set([1, 2, 3, 2])
# print(my_set)

#Remove a number from a set
# num_set = set([0, 1, 2, 3, 4, 5])
# print("Original set:")
# print(num_set)
# num_set.pop()
# print("After removing the first element from the said set:")
# print(num_set,"\n")

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
print("\nUnion of two said sets:")
seta = setx.union(sety)
print(seta)
print("\nDifference of two said sets:")
setb = setx.difference(sety)
print(setb)

# import array as arr

# #create an array
# array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
# print("Original array: "+str(array_num))

# #count number of occurences
# print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

# #reverse the array
# array_num.reverse()
# print("Reverse the order of the items:")
# print(str(array_num))