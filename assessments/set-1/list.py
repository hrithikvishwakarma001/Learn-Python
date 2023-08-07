# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

numbers = [i for i in range(1, 11,1)] # index,range,steps

print(numbers)

# Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
# Input: [10, 20, 30, 40]
# - *Output*: "Sum: 100, Average: 25.0"

inp = input("enter your list of number : ")
array = [int(i) for i in inp.split()]

def sum(array):
  total = 0
  for x in array:
     total = total+x
  
  return total  

def average(sumCallback,numsArray):
  return sumCallback(numsArray) / len(numsArray)
  
print(int(average(sum,array)))