def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        #return                             # returns NOTHING
        return "You did not provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    full_name = formatted_f_name + " " + formatted_l_name
    # print(f"Your full name is {full_name}")
    return full_name
    print("Hello")                  # this command doesn't get executed, after return everything is ignored

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
full_name = format_name(f_name, l_name)
print(f"{full_name}")