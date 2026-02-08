import random

print("Welcome to the Python Password Generator!\n")
pass_len = int(input("How many letters would you like in your password? \n"))
num_symbols = int(input("How many symbols would you like in your password? \n"))
total_numbers = int(input("How many total numbers would you like in your password? \n"))

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!', '#', '$', '%', '&', '*', '@', '?', '+', '-']


# Easier Level
# password = ""
# num_alphabets = pass_len - num_symbols - total_numbers
#
# for alphabet in range(0, num_alphabets):
#     password += random.choice(alphabets)
# for symbol in range(0, num_symbols):
#     password += random.choice(symbols)
# for number in range(0, total_numbers):
#     password += random.choice(numbers)
#
# print(f"\nYour generated password is ---->    {password}")
#

### Harder Level
password = ""
password_choices = ["alphabets", "numbers", "symbols"]
total_alphabets = pass_len - num_symbols - total_numbers
count_alphabets = 0
count_numbers = 0
count_symbols = 0
for p in range(0, pass_len):
    choice = random.choice(password_choices)
    if choice == "alphabets":
        if count_alphabets < total_alphabets:
            password += random.choice(alphabets)
            count_alphabets += 1
    elif choice == "numbers":
        if count_numbers < total_numbers:
            password += random.choice(numbers)
            count_numbers += 1
    elif choice == "symbols":
        if count_symbols <= num_symbols:
            password += random.choice(symbols)
            count_symbols += 1


# password = ''.join(random.sample(password, len(password)))      # randomize the characters internally to avoid clustering
print(f"Your generated password is: {password}")