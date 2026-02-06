### Strings

# Subscripting -> pulling out a character from a string

print("Hello"[1])   # prints "e"

# extract the last character from a string

print("Hello"[-1])   # prints 1 character from last  --> o
print("Hello"[-2])   # prints 2 characters from last --> l

# String Concatenation

print("123" + "345" )   # this prints as a concatenation

### Integers

print(123 + 465)   # this prints as addition = 588

# Large Integers  --> Commas can be converted to _ for example 1,00,000 = 1_00_000
print(15_00_000)



### Float

print(3.14)


### Booolean

print(True)
print(False)


# len() function can  only take a string and not an int

# len(12345) will give a Type Error

len("12345")

# type() gives you the datatype of the variable
print(type("Hello"))
print(type(12345))
print(type(True))
print(type(1.20))

## Typecasting ->   Converting Data Types   --> int() ; float() ; bool() ; str()

print(int("1234") + int("10"))


print(int("abc") + int("10"))   # --> Value Error ->

