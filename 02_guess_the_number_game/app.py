from random import randint

def main():
    random_number = randint(1, 100) # generating and storing a random number 
    
    while True:
        user_guess = int(input("Guess a number(1-100): ")) # taking user guess

        if 1 <= user_guess <= 100:
            if user_guess < random_number:
                print("Guess a big number.\n")
            
            elif user_guess > random_number:
                print("Guess a small number.\n")
            
            elif user_guess == random_number:
                print("Great you guessed it right!!!!!!")
                break



if __name__ == "__main__":
    main()