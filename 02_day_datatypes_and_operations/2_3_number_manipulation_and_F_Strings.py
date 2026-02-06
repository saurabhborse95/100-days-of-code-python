bmi = 84 / 1.65 **2

print(bmi)   # 30.85399449035813


print(int(bmi))  # this floors the float number  --> 30


# Round function

print(round(bmi))   # traditional round up function --> 31

print(round(bmi, 2))  # rounds to the float number to 2 decimals


## Assignment operator

score = 20
# User scores a point
score += 1
print(score)
score *= 2
print(score)

score /= 2
print(score)




### F-Strings

# until now print(string + string)

score = 15
height = 1.8
is_winning = True

print(f"Your score is = {score}, and your height is = {height}, and you are winning is {is_winning}")
