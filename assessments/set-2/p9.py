# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# {'name': 'Kelly', 'salary': 8000}

res = {}
for x in keys:
  res[x] = sample_dict[x]

print(res)