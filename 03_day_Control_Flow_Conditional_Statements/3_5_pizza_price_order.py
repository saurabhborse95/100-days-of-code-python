print("Welcome to the Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")

pepperoni = input("Do you want pepperoni on your pizza (2€ for S, 3€ for M and L) ? Y or N :")

extra_cheese = input("Do you want extra chese on your pizza (plus 1€) ? Y or N :")
print("----------")
pizza_price = 0

if size == "S":
    print("Pizza size S is 15€")
    pizza_price += 15
    if pepperoni == "Y":
        print("Peperoni +2€")
        pizza_price += 2
    if size == "M":
        print("Pizza Size M = 20€")
        pizza_price = 20
    elif size == "L":
        print("Pizza Size L costs 25€")
        pizza_price = 25

    if pepperoni == "Y":
        print("Peperoni +3€")
        pizza_price += 3
if extra_cheese == "Y":
    print("Extra Cheese +1€")
    pizza_price += 1

print(f"Your pizza price is {pizza_price} €")