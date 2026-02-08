print('''
                                                                           
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
 ***************************************************************************************************+                                                              
 ''')

print("\n\nWelcome to the Treasure Island!! \n You\'re mission is to find the diamonds in the treasure island.")
print("you are on Island X and want to navigate out of the sea to the Island Zeta. ")
choice_cross_sea = input("Would you cross the sea with a boat or plane? \n").lower() # helps in normalizing the input string
if choice_cross_sea == "boat" :
    print("Ouch, there are deadly sharks and pirahnas in the water. GAME OVER!")
elif choice_cross_sea == "plane":
    print("Good choice, clearing the runway on Island Zeta Airport......................\n")
    print("You just got to know the diamonds may be hidden in some cave in this island.")
    travel_choice = input("Would you like to travel through the jungle on bike or  car:  ").lower() # helps in normalizing the input string
    if travel_choice == "bike" :
        print("Bad Choice, roads are bad and slippery to the cave. "
              "You are captured by a sworm of honeybees and you don't reach the cave--> Game Over!")
    elif travel_choice == "car" :
        print("Good choice, reaching Cave Borita in 10 mins")
        print("You have now reached the cave. There are three major Gates from this cave. "
              "Gate Albe, Gate Bravo and Gate Carlo\n")
        gate = input(" Which gate do you want to use? Albe, Bravo or Carlo :  ").lower() # helps in normalizing the input string
        print(gate)
        if gate == "albe" or gate == "carlo":
            print("You fell into a 1000m deep trench -> Game Over!")
        elif gate == "bravo" :
            print("Bravo!! You have reached the treasury Box full of Diamonds!!!!  -> YOU WON!!!")



