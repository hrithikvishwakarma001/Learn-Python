# String Reversal: Write a Python function that takes a string and returns the string in reverse order.
# Input: "Python"
# Output: "nohtyP"

inputStr = input("Enter your string : ")

def reverseStr(str):
  reversed_str = ""
  for char in str:
      reversed_str = char + reversed_str
  return reversed_str

print(reverseStr(inputStr))
  
   