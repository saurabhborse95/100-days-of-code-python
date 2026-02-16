def format_name(f_name, l_name):
    """Take a first and last name and formats it to return the full name
    Now i can write everything like this docstring
    write tests and descriptions for each functions in this way

    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    full_name = formatted_f_name + " " + formatted_l_name
    print(f"Your full name is {full_name}")
    return full_name

