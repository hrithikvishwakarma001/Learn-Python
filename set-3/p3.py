# Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

# - *Input*: [2, 7, 11, 15], target = 9
# - *Output*: "[0, 1]"

def twoSome(arr,target):
  dec={}
  for index,x in enumerate(arr):
    dif = target - x
    if(dif in dec):
      return [dec[dif],index]
    dec[x] = index
  return "no integer"

print(twoSome([2, 7, 11, 15],9))