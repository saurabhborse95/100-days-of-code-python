## Lets say whoever gets the ticket gets an option to buy a ticket
bill = 0
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the roller coaster")
    age = int(input("Please mention your age: "))
    if age <= 12:
        bill = 5
        print("Children tickets are 5€")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7€")
    else:
        bill = 10
        print("Adult tickets are 10€")
    wants_photo = input("Do you want a photo. Ticket is 3€. Type Y for yes or N for no? ")
    if wants_photo == "Y":
        # Add 3€ to the bill
        bill += 3
    print(f"--> Your bill is: {bill} €")


else:
    print("Sorry you cannot ride the roller coaster")
