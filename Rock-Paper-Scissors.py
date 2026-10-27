import random

SCORE = 0
COMPUTERSCORE = 0
RESTART = True

WinningCombos = {
    "rock" : "scissors",
    "scissors" : "paper",
    "paper" : "rock"
}

SELECTION = {
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}

print("\nWelcome to my rock paper scissors game!\n")
while RESTART:
    while SCORE < 3 and COMPUTERSCORE < 3:
        try:
            selection = int(input("Choose your move (Rock(1),Paper(2),Scissors(3)): ").strip())
            selection = SELECTION[selection]
        except (ValueError, KeyError):
            print("Incorrect value please try again.")
            continue
        computer_selection = random.randint(1,3)
        computer_selection = SELECTION[computer_selection]

        print(f"\nYou chose {selection} and the computer chose {computer_selection}\n")
        if selection == computer_selection:
            print("This round is a tie.\n")
        elif WinningCombos[selection] == computer_selection:
            print("You get a point!\n")
            SCORE += 1
        else:
            print("The computer won this round :(\n")
            COMPUTERSCORE += 1
        
        print(f"Current Score:\nYou: {SCORE}\nComputer: {COMPUTERSCORE}.\n")

        if SCORE < 3 and COMPUTERSCORE < 3:
            print("Next Round\n")
    print("Game Over!\n")
    if SCORE == 3:
        print("You won good job!\n")
    else:
        print("The computer wins this time:(\n")
    
    while True:
        answer = input("Would you like to play again (Yes/No)?: ").strip().lower()

        if answer == "yes":
            SCORE = 0
            COMPUTERSCORE = 0
            print("\nStarting a new game!\n")
            break
        elif answer == "no":
            RESTART = False
            print("\nThanks for playing.")
            break
        else:
            print("\nInvalid answer try again please.\n")