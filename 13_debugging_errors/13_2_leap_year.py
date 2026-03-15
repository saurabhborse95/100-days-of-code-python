def is_leap(year):
    if year % 4 == 0:
        print("divisible by 4")
        if year % 100 == 0:
            print(" divisible by 100")
            if year % 400 == 0:
                print("divisible by 400")
                return True
            else:
                print("NOT divisible by 400")
                return False
        else:
            print(" NOT divisible by 100")
            return True
    else:
        print("NOT divisible by 4")
        return False
print(is_leap(2020))