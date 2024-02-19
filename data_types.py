import math

# Naming Convention for Files
# all lowercase and _ if spaces needed


# String Data Type

# literal assignment
first = "Dave"
last = "Gray"

# Check Type
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#  constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# MISC: Ctrl + D shortcut to select multiple occurences one at a time

# Concatenation
fullname = first + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.

                ALl good?
                
'''
print(multiline)

#Escaping special characters (backwards slash \)
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

# MISC: Shift + Alt + down arrow => shortcut to copy line

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "            "
multiline = "      " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String Index Values
print(first[1])
print(first[-1]) #last value
print(first[1:-1]) #range exclusive of vals
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True #capital T or F
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type (often used in electrical engineering)
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# BUilt-in functions for numbers
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


# Imported Math Module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")