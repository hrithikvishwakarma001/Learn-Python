# Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.

word = "fdfd"

rev=""

for x in word:
  rev = x + rev

# print(word,rev)
if(word==rev):
  print("is this is palindrom")
else :
  print("not palindrome")
