def years_to_weeks_converter(number_of_years):
    number_of_weeks = number_of_years * 52
    return number_of_weeks

def weeks_to_days_converter(number_of_weeks):
    number_of_days = number_of_weeks * 7
    return number_of_days

def life_in_weeks(current_age):
    assumed_life_expectancy = 90
    remaining_life_in_years = assumed_life_expectancy - current_age
    remaining_life_in_weeks = years_to_weeks_converter(remaining_life_in_years)
    remaining_life_in_days = weeks_to_days_converter(remaining_life_in_weeks)
    print(f"You have {remaining_life_in_weeks} and {remaining_life_in_days} weeks left.")


current_age = int(input("What is your current age? "))#
life_in_weeks(current_age)