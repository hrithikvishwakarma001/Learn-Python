# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
  temp=""
  for j in range(i):
    temp = temp+str(j+1)+" "
  print(temp)  