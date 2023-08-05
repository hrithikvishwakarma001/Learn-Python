
def fib(n):
  arrList = [0,1]
  while len(arrList) < n:
    prevSum = arrList[-1]+arrList[-2]
    arrList.append(prevSum)
  return arrList  

print(fib(10))