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
ch=input("You're at a crossroad,where do you want to go? Type \"left\" or \"right\".\n")
ch=ch.lower()
if(ch=="left"):
    ch2=input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat. Type\"swim\" to swim across.\n").lower()
    if(ch2=="wait"):
       ch3=input("You arrived at the island unharmed. There is a house with three doors. One red, onr yellow and one blue. Which color do you choose?\n").lower()
       if(ch3=="yellow"):
           print("You found the treasure. You win!!")
       elif(ch3=="red"):
           print("You went into a room with fire . Game over.")
       elif(ch3=="blue"):
           print("You went into a room with water . Game over.")
       else:
           print("You chose a door that does not exist. Game over. ")
    else:
        print("You got attacked by an angry trout. Game over. ")
else:
    print("You fell into a hole. Game over.")