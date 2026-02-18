from cal_art import logo
def calulator(l_operand):

    print("+\n-\n*\n/\n")
    operator = input("Pick an operation :   ")
    r_operand = float(input("What's the next number? :  "))


    if operator == "+":
        res = l_operand + r_operand
    elif operator == "-":
        res = l_operand - r_operand
    elif operator == "*":
        res = l_operand * r_operand
    elif operator == "/":
        res = l_operand / r_operand

    print(f"{l_operand} {operator} {r_operand} = {res}")
    continueCalc = input("Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation :  ")
    return res, continueCalc


print(logo)
print("\n\n")
continueCalc = 'y'
l_operand = float(input("What's the first number? :   "))
while continueCalc == 'y':

    res, continueCalc = calulator(l_operand)
    if continueCalc == "y":
        res, continueCalc = calulator(res)
    elif continueCalc == "n":
        break
