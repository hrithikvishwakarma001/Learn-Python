# : Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.

# Input: [("John", 25), ("Jane", 30)]
# Output: "John is 25 years old. Jane is 30 years old."

data = [("John", 25), ("Jane", 30)]

output = ""
for name, age in data:
    output += f"{name} is {age} years old. "

print(output)
