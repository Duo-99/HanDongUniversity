print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choose_lane = input(
    "You are at a cross road. Where do you want to go? Type 'left' or 'right'.\n"
)
if choose_lane == "left":
    print(
        f"You have chosen {choose_lane}. You have come to a lake. There is an island in the lake.\n"
    )
    choose_swim = input(
        "You came to Lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or Type 'swim' to swin across.\n"
    )
    if choose_swim == "wait":
        print(
            f"You have chosen {choose_swim}. You have arrived at the island unharmed. There.\n"
        )
        choose_door = input(
            "You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\n"
        )
        if choose_door == "red":
            print(
                f"You have chosen {choose_door}. You have entered a room of beasts. Game Over!"
            )
        elif choose_door == "yellow":
            print(
                f"You have chosen {choose_door}. You have found the treasure. You Win!"
            )
        else:
            print(
                "You have chosen blue. You have entered a room of beasts. Game Over!"
            )
    else:
        print(
            f"You have chosen {choose_swim}. You have been attacked by a trout. Game Over!"
        )

else:
    print(
        f"You have chosen {choose_lane}. You have fallen into a hole. Game over!"
    )