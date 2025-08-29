# replace() method
a = "Hello world"
print(a.replace("H", "J"))

# split string
a = "Hello, World"
print(a.split(","))

# concatenation of strings
a = "Hello world"
b = ", This is Armash"
print(a+b)
 
# Format string (implemented in version 3.6)
age = 19
txt = f"My name is Armash, I am {age}" 
print(txt)

# Escape characters
#To put a "" in a string we use \""

#Python booleans
print(10 > 5)
#bool() function
print(bool("abc")) #Most of the values are True
print(bool("")) #Similarly it is true for all Lists and tuples except for the empty ones

# Sequence datatypes
#List datatype, Tuple, Range
list = ['abcd', 'efgh', 723, 1, 2, 4, 5, 'a']
list2 = ['b', 'c', 'd']
print(list + list2)
print(list[1 : 3])
print(list[1][2])

#Range datatype in python
#range(start, stop, step)
for i in range(0, 6, 2):
    print(i)