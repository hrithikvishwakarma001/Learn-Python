'''
2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
    - *Input*: None
    - *Output*: "Type of variable1: <class 'int'>, value: 10..."
'''

# integer
one = int(1)
print("type of variable1:",type(one),"value:",one)

# float

# x = f"hero is hero {one}" #f is a sting where we can use variable with string
# print(x)

# print(float(one)) # convert any integer into float 1.0

two = 1.5
print("type of variable2:",type(two),"value:",two)
 
# string
three = "three"
print("type of variable3:",type(three),"value:",three)

# boolean

is_active = True
print("type of variable4:",type(is_active),"value:",is_active)

# List

arr = [1,"hrithik",False,5.1]
print("type of variable4:",type(arr),"value:",arr)

# tuple

unchangableArray = ("helo",25)

print("type of variable5:",type(unchangableArray),"value:",unchangableArray)

# dictionary

obj = {"name":"hrihtik","age":19}
print("type of variable6:",type(obj),"value:",obj)

# set

setting = {2,"hello",False,1.5,"hero"}
setting.add("foru")
setting.remove(False)
print("type of variable6:",type(setting),"value:",setting)