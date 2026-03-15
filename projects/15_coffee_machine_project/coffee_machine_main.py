MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO 1: Print Report on "report"
#TODO 2: Check Resources sufficient?
#Todo 3: Process Coinds
# TODO 4: check transaction successful?
# TODO 5: make coffee

coffee_machine_ON = True
profit = 0
def print_resources():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${profit}")
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} for your order.")
            return False
        else:
            return True
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters? :  ")) * 0.25
    total += int(input("how many dimes? :  ")) * 0.10
    total += int(input("how many nickles? :  ")) * 0.05
    total += int(input("how many pennies? :  ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted or False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that is not enough money.  ---> Money refunded")
        return False



def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources
    """

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} !:  ☕️")


while coffee_machine_ON:
    choice = input("What would you like? (espresso / latte / cappuccino)  : ")
    if choice == "off":
        print("\n\nTurning the coffee machine off ....")
        coffee_machine_ON = False
        break
    elif choice == "report":
        print_resources()

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

