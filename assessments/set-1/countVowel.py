# Count Vowels: Write a Python program that counts the number of vowels in a given string.
# Input: "Hello
# Ouput: "2


def countVowels(str):
  vowels = "AEIOUaeiuo"
  count = 0
  for x in str:
    if(x in vowels):
      count = count+1
  return count

print("your vowels",countVowels("hrithik"))