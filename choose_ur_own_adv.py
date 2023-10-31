print(""" 
88                                                       88  
88                                                       ""  
88                                                           
88,dPPYba,   ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYYba, 88  
88P'    "8a a8"     "8a 88P'   `"8a I8[    "" ""     `Y8 88  
88       d8 8b       d8 88       88  `"Y8ba,  ,adPPPPP88 88  
88b,   ,a8" "8a,   ,a8" 88       88 aa    ]8I 88,    ,88 88  
8Y"Ybbd8"'   `"YbbdP"'  88       88 `"YbbdP"' `"8bbdP"Y8 88 
""")

print("Welcome to Treasure Island! \nYour mission is to find the treasure!")

volcano = input("You are at a crossroads at the volcano path. \nChoose where to go! Left or Right? ")

#After Volcano
if volcano == "Left" or "left" or "L":
    water_works = input("Nice! You chose the correct way! \nYou stumble upon a river. You have the option to swim or wait for a boat. \nDo you choose to Swim or Wait? ")
else:
    print("You fell into a hole! GAME OVER")

#After Swim
if water_works != "Swim" or "swim" or "S":
    choose_door = input("Good thinking! \nNow you stumble upon 3 doors at this house, which color door are you going through? \nRed, Yellow, or Blue??? ")
else:
    print("AHHHH NOO! You were eaten by trout! GAME OVER")

#After Door
if choose_door == "Yellow" or "yellow" or "Y":
    print("Congrats! You are the winner!")
elif choose_door == "Red" or "red" or "R":
    print("You were burned by a flames! YOU LOST")
elif choose_door == "Blue" or "blue" or "B":
    print("You were eaten by Bella the VAMP! GAME OVERRRR")
else:
    print("BLEHHH YOU LOSE")
