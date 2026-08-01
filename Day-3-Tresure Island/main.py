print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
first=input("Where you want to go ? Type 'left' or 'right'\n ").lower()
if first=="left":
    second=input('You have arrived to the lake.'
          'Now you have to go to island which locate middle of the lake.'
          'So now if you want to swim type "swim"'
          'if you wait for a boat type "wait"\n ').lower()
    if second=="wait":
        third=input('You have arrived to the island and '
                    'you have to choose correct door from colour'
                    'if you choose red door type "red" or if you '
                    'choose yellow door type "yellow" or if you choose '
                    'blue door type "blue"\n.').lower()
        if third=="blue":
            print("You were eaten by beasts.Game Over")
        elif third=="red":
            print("you were burned by fire.Game Over")
        elif third=="yellow":
            print("you win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print('Game Over')
