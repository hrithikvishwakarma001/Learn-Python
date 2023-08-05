# The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
  if(num>500):
    break
  if(num % 5 == 0 and num<=150):
    print(num)