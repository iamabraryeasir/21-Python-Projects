import random
from program_title import clear_screen, program_title

# Rock Paper Scissors ASCII Art

# Rock
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


# printing art based on choice
def choice_print(choice):
    if choice == 'rock':
        print(rock_art)
    elif choice == 'paper':
        print(paper_art)
    else:
        print(scissors_art)


# Main game logic
def check_winner(your_choice, computers_choice):
    if your_choice == 'rock' and computers_choice == 'paper':
        return 'computer'
    
    elif your_choice == 'paper' and computers_choice == 'scissor':
        return 'computer'
    
    elif your_choice == 'scissor' and computers_choice == 'rock':
        return 'computer'
    
    if computers_choice == 'rock' and your_choice == 'paper':
        return 'you'
    
    elif computers_choice == 'paper' and your_choice == 'scissor':
        return 'you'
    
    elif computers_choice == 'scissor' and your_choice == 'rock':
        return 'you'
    
    elif computers_choice == your_choice:
        return 'draw'


# Main function
def main():
    rps = ['rock', 'paper', 'scissor'] 

    computer_won = 0
    you_won = 0
    draw = 0

    while True:
        # Clearing the screen
        clear_screen()

        # printing program title
        program_title("Rock, Paper, Scissor Game")

        # generating choice of the computer
        computers_choice = random.choice(rps)       
        

        # taking human choice
        print("1) Rock \n2) Paper \n3) Scissor")
        while True:                                 
            your_choice = int(input("What is your choice(1/2/3): "))
            if your_choice in [1, 2, 3]:
                break
        

        # converting the int choice to a text formate
        match your_choice:
            case 1:
                your_choice = 'rock'
            case 2: 
                your_choice = 'paper'
            case 3:
                your_choice = 'scissor'


        # Printing art's based on choices
        print("Computer Chose:")
        choice_print(computers_choice)

        print("You Chose:")
        choice_print(your_choice)

        # Check for the winner
        winner = check_winner(your_choice, computers_choice)

        # Printing eho is the winner
        if winner == 'you':
            you_won += 1
            print("Great You Won the Game.")

        elif winner == 'computer':
            computer_won += 1
            print("Aah, Computer Won the Game.")    

        else:
            draw += 1
            print("The match is draw.")

        # asking if they want to play more:
        while True:
            your_choice = input("\nDo you want to play more(y/n): ").lower()
            if your_choice in ['y', 'n']:
                break

        if your_choice == 'n':
            clear_screen()
            break
    
    # Printing the Final Result
    computer_won_text = f"*   1. Computer Won  -> {computer_won}"
    you_won_text = f"*   2. You Won       -> {you_won}"
    draw_text = f"*   3. Draw Match    -> {draw}"

    print("\t", f"*" * 50)
    print("\t", f"*{" " * 15}   Final Result   {" " *15}*")
    print("\t", f"*{" " * 48}*")
    print("\t", f"{computer_won_text}{" " * (50 - (len(computer_won_text) + 1))}*")
    print("\t", f"{you_won_text}{" " * (50 - (len(you_won_text) + 1))}*")
    print("\t", f"{draw_text}{" " * (50 - (len(draw_text) + 1))}*")
    print("\t", f"*" * 50)

if __name__ == "__main__":
    main()