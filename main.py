# use hashtag to make comments in python

# use _ to separate variable words
first_name = "Valerio"
last_name = "Failah"
full_name = first_name + " " + last_name

print("Welcome in Python " + first_name + "!")
print("The type of the var name is:",
      type(first_name))  # this stamp the type of that variable in console (int in this case)
print()
print("Your full name is: " + full_name)
print()

age = 31
age += 1
print("Your age is:", age)
print("The type of the var age is:", type(age))  # string

# casting int age into string to concatenate using + instead of ,
print("Your age is: " + str(age) + " (casted age into string)")
print()

height = 175.56
print("Your height is:", height, "cm")
print("The type of the var height is:", type(height))  # float (decimals)
print("Your height is: " + str(height) + " cm (casted height into string)")
print()

is_human = True  # for booleans var, False and True must be Capitalized
print("Are you a human?:", is_human)
print("Are you a human?: " + str(is_human) + " (casted boolean into string")
