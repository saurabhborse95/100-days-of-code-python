def is_leap_year(year):
    divisible_4 = False
    divisible_100 = False
    divisible_400 = False

    if year % 4 == 0:
        divisible_4 = True
        if year % 100 == 0:
            divisible_100 = True
            if year % 400 == 0:
                divisible_400 = True
    if divisible_4:
        if divisible_100 == True and divisible_400 == True:
            return True
        elif divisible_100 == True and divisible_400 == False:
            return False
        elif divisible_100 == False and divisible_400 == True:
            return True
        elif divisible_100 == False and divisible_400 == False:
            return True

    else:
        return False


# is_leap_year(2026)
print(is_leap_year(2024))