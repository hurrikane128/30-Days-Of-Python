# 30 days of python programming (Day 2)

import math

first_name = "Matt"
last_name = "Torres"
first_last = first_name + last_name
country = "NUSA"
city = "NC"
age = 27
year = 2000
is_married = False
is_true = True
is_light_on = True
var1, var2, var3 = "Var1", 1738, True


print(len(first_name))

if len(first_name) > len(last_name):
    print(f"Your first name is longer than your last by {len(first_name) - len(last_name)} characters.")
else:
    print(f"Your last name is longer than your first by {len(last_name) - len(first_name)} characters.")

num_one = 5
num_two = 3

print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
print(num_one / num_two)

print(num_one % num_two)
print(num_one ** num_two)

radius = 30
area = math.pi * (radius ** 2)
print("The area of the circle is:", area)


