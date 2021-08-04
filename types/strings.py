# Strings:

# If you don’t want characters prefaced by \ to be interpreted
# as special characters, you can use raw strings by adding an r
# before the first quote:

print("C:\some\name")  # here \n means newline!
print(r"C:\some\name")

# String literals can span multiple lines.
# One way is using triple-quotes: """...""" or '''...'''

print(
    """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
)

# Strings can be concatenated (glued together)
# with the + operator, and repeated with *:

print("3*'un' +'ium'= ", 3 * "un" + "ium")

# Strings can be indexed (subscripted), with the first
# character having index 0.
# There is no separate character type;
# a character is simply a string of size one:

word = "Python"
print("word = ", word)
print("word[0] = ", word[0])
print("word[5] = ", word[5])
print("word[-1] = ", word[-1])
print("word[-6] = ", word[-6])

# While indexing is used to obtain individual characters,
# slicing allows you to obtain substring:

print("word[:2]+word[2:] = ", word[:2] + word[2:])
print(
    "word[0:2] = ", word[0:2]
)  # characters from position 0 (included) to 2 (excluded)
print(
    "word[2:5] = ", word[2:5]
)  # characters from position 2 (included) to 5 (excluded)

# s[:i] + s[i:] is always equal to s:
print("word[:4] + word[4:] = ", word[:4] + word[4:])

print(
    """
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1 """
)

# Python strings cannot be changed — they are immutable.
# Therefore, assigning to an indexed position in the string
# results in an error:

# If you need a different string, you should create a new one:

# word[0] = 'J' ==

word = "J" + word[1:]
print("word = ", word)

# String Methods

print("word length = ", len(word))
print("str(3.5 ) = ", str(3.5))
a = "         Hello, World! "
print(a.strip())  # returns "Hello, World!"
a = "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))  # returns ['Hello', ' World!']
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
x = "ain" not in txt
print(x)

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index types {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
