import random


def gameplay():
    print("#######Enter your letter as either lower-case or upper-case#######")
    player = input("Enter a choice ('R' for rock, 'P' for paper, 'S' for scissors): \n").upper()
    action = ['R', 'P', 'S']
    cpu = random.choice(action)
    print("*******************************")
    


    if player == cpu:
        if player == 'R':
            print(f"Both players selected 'Rock'. It's a tie!\n")
            print("**********Please play again!!!**********")
            gameplay()
        elif player == 'P':
            print(f"Both players selected 'Paper'. It's a tie!\n")
            print("**********Please play again!!!**********")
            gameplay()
        elif player == 'S':
            print(f"Both players selected 'Scissors'. It's a tie!\n")
            print("**********Please play again!!!**********")
            gameplay()


    elif player == "R":
        if cpu == "S":
            print("*******************************")
            print('Player (Rock) : CPU (Scissors)\n')
            print("Rock beats Scissors! You win!")
            print("*******************************")
        elif cpu == "P":
            print("*******************************")
            print('Player (Rock) : CPU (Paper)\n')
            print("Paper beats Rock! You lose.")
            print("*******************************")



    elif player == "P":
        if cpu == "R":
            print("*******************************")
            print('Player (Paper) : CPU (Rock)\n')
            print("Paper beats Rock! You win!")
            print("*******************************")
        elif cpu == "S":
            print("*******************************")
            print('Player (Paper) : CPU (Scissors)\n')
            print("Scissors beats Paper! You lose.")
            print("*******************************")



    elif player == "S":
        if cpu == "P":
            print("*******************************")
            print('Player (Scissors) : CPU (Paper)\n')
            print("Scissors beats Paper! You win!")
            print("*******************************")
        elif cpu == "R":
            print("*******************************")
            print('Player (Scissors) : CPU (Rock)\n')
            print("Rock beats Scissors! You lose.")
            print("*******************************")
    else:
        print("Invalid input!!!")
        print("**********Please try again!!!**********")
        gameplay()
gameplay()