# Problem 7: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# 10 400
# 20 300
# 30 200
# 40 100

for i in range(0,len(list1)):
  print(list1[i],list2[-(i+1)])