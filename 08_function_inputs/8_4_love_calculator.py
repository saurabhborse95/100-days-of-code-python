def calculate_love_score(name_a , name_b):
    combined_name = (name_a + name_b).upper()
    score = 0
    for letter in "TRUELOVE":
        if letter in combined_name:
            score += combined_name.count(letter)

    print(score)

#
#
partner_A_name = input("Write the name of Partner A: ")
partner_B_name = input("Write the name of Partner B: ")
calculate_love_score(partner_A_name, partner_A_name)

# calculate_love_score("Saurabh Borse", "Urvi Bhandarkar")








