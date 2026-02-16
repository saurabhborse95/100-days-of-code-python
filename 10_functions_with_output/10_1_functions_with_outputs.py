def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    full_name = formatted_f_name + " " + formatted_l_name
    print(f"Your full name is {full_name}")
    return full_name


f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
full_name = format_name(f_name, l_name)