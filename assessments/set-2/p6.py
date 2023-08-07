# Problem 5: Concatenate two lists index-wise

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

res = []

for x in list1:
  for y in list2:
    res.append(x+y)


print(res)