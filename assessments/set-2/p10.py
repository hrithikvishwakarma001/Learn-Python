# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

tuple1 = (11, [22, 33], 44, 55)
# tuple1: (11, [222, 33], 44, 55)


list1 = list(tuple1)

list1[1][0] = 222

tuple1 = tuple(list1)

print(tuple1)
