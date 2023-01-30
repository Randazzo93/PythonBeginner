import random

def program():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    game_images = [rock,paper,scissors]
    game_choice = ["rock","paper","scissors"]

    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
    choice = int(input())
    print("you chose: " + game_choice[choice])
    print(game_images[choice])
    
    computer = random.randint(0,2) 
    print("computer chose: " + game_choice[computer])
    print(game_images[computer])

    if choice >= 3 or choice < 0: 
        print("You typed an invalid number, you lose!") 
    elif choice == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and choice == 2:
        print("You lose")
    elif computer > choice:
        print("You lose")
    elif choice > computer:
        print("You win!")
    elif computer == choice:
        print("It's a draw")


        



if __name__ == '__main__':
    program()
    

