#### Logical Operators are used to check or veryify the conditional operators

# there are three different operators: and ; or ; not

height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the roller coaster")
    age = int(input("Please mention your age: "))
    if age <= 12:
        print("Please pay 5€")
    elif age <= 18:
        print("Please pay 7€")
    elif age >=45 and age <=55:
        print("everything is going to be ok. Have a free ride on us!")
    else:
        print("Please pay 10€")
else:
    print("Sorry you cannot ride the roller coaster")
