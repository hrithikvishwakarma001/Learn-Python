def add_name_age(name, age, my_dict):
    my_dict[name] = age
    return my_dict

def update_age(name, age, my_dict):
    if name in my_dict:
        my_dict[name] = age
    return my_dict

def delete_name(name, my_dict):
    if name in my_dict:
        del my_dict[name]
    return my_dict


my_dict = {}
my_dict = add_name_age("John", 25, my_dict)
print(my_dict)

my_dict = update_age("John", 26, my_dict)
print(my_dict)

my_dict = delete_name("John", my_dict)
print(my_dict)
