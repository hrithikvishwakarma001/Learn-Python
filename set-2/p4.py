# Problem 4: Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"
# yaivePNT
lower = ""
upper = ""

for char in str1:
  if(char.islower()):
    lower = lower+char
  else:
    upper = upper+char

print(lower+upper)