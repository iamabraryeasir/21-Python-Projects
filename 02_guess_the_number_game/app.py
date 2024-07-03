from program_title import clear_screen, program_title
from random import randint

def main():
    clear_screen() # to clear the screen

    random_number = randint(1, 100) # generating and storing a random number 
    
    program_title("Guess the Number Game")

    attempts = 0        # variable to count the attempts
    
    range_start = 1     # variables for setting dynamic ranges
    range_end = 100
    
    while True:
        
        user_guess = int(input(f"Guess a number({range_start}-{range_end}): ")) # taking user guess

        if 1 <= user_guess <= 100:

            if user_guess < random_number:
                print("Try a Bigger number.\n")
                attempts += 1
                range_start = user_guess
            
            elif user_guess > random_number:
                print("Try a Smaller number.\n")
                attempts += 1
                range_end = user_guess

            elif user_guess == random_number:
                attempts += 1
                print("\n\tGreat you guessed it right!!!!!!")
                print(f"\tBut After total {attempts} attempts.", end="\n\n")
                break



if __name__ == "__main__":
    main()