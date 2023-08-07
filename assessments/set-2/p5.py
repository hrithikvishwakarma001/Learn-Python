# Problem 5: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# ['My', 'name', 'is', 'Kelly']

res=[]

for i in range(0,len(list1)):
  res.append(list1[i]+list2[i])

print(res)