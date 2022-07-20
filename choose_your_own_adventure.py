name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer = input("you are on a dirt road, it has come to an end you can go left or right, which way would you like to go? ").lower()
if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? type (walk) to walk around and (swim) to swim accross: ").lower()
    if answer == "swim":
        print("you swam accross and were eaten by a crocodile")
    elif answer == "walk":
        print("you walked for miles, ran out of water and you lost the game")
    else:
        print("not a valid option. you lose.")
elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("you go back and get lost")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. do you talk to him (yes/no)? ").lower()
        if answer == "yes":
            print("you talk to him and you win")
        elif answer == "no":
            print("he get angry and killed you")
        else:
            print("not a valid option. you lose.")
    else:
        print("not a valid option. you lose.")
else:
    print("not a valid option. you lose.")
print("thank you for playing")
