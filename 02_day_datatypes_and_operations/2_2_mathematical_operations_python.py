print(1 + 2)
print(2 - 1)
print(1 * 2)
print(6 / 3)    # -> Implicit Typecasting -> converts to float

print(6 // 3)   # does not do implicit typecasting but also rounds the number to the floor

print(4 ** 2)   #  4 raised to the power of 2


## Multiple operations --> PEMDASLR -> ( Parenthesis, Exponents, Multiplications/Division / Addition/Subtraction ) left to right


# PEMDASLR --> to the left = more priority

print(3 * 3 + 3 / 3 - 3)

# 3*3 = 9; 3/3 = 1.0; -1 ---> 9 + 1.0 - 3 = 7.0

print(3 * (3 + 3)/ 3 - 3)


# 3 * 6 / 3 -3  --> left hast more prio --> 18 / 3 - 3 --> 6.0 - 3 --> 3.0