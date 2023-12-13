import math

# Literal String assignment
first = "Quinten"
last = "Krauth"

print(type(first))

# Constructor function
pizza = str("pepperoni")

print(type(pizza))

# Concatenatuib
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

# Multiline
multiline = """
Hello.
Hi, how are ya?
Deeecent wbu?
Aight.
"""

print(multiline)

# \n is a new line shortcut in a string

# String Methods
print(first)
print(first.lower())
print(first.upper())

print(multiline.title()) # capitalize the first letter of a word
print(multiline.replace("Hello", "Howdy")) # replace a word

print(len(multiline)) # counts characters in string

# String index values
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
print(first[5])
print(first[-1])

# Some methods return boolean data
print(first.startswith("Q"))

# Numeric data types

# Integer
price = 100
best_price = int(80)
print(type(price))
print(type(best_price))

# Float
GPA = 3.80

# Built in functions for numbers
print(abs(GPA)) # absolute value

print(round(GPA))

print(math.pi)
print(math.sqrt(81))