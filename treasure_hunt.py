
def program():
    print("Welcome to the treasure hunt game! Make choices and find the treasure.")
    print("You're at a cross road. Where do you want to go? Type ""left"" or ""right"" ")
    direction = input()

    if direction.lower() == "left":
        print("You come to a lake. There is an island in the middle of the lake. Type ""wait"" to wait for a boat. Type ""swim"" to swim across ")
        action = input()

        if action.lower() == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?")
            door = input()

            if door.lower() == "red":
                print("Burned by fire. Game Over")
            elif door.lower() == "blue":
                print("Eaten by beasts. Game Over")
            elif door.lower() == "yellow":
                print("You Win!")
            else:
                print("Game Over.")

        else:
            print("Attacked by trout. Game Over")

    else:
        print("Fall into a hole. Game Over.")

if __name__ == '__main__':
    program()
    

    