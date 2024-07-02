from program_title import program_title, clear_screen

# Global Variable to Count Mark
right_answers = 0
    

# Global List Containing all questions
questions = [
    {
        "question": "What is the capital of bangladesh?",
        "option_1": "Dhaka",
        "option_2": "Chattagram",
        "option_3": "Rajshahi",
        "option_4": "Khulna",
        "answer": 1
    },
    {
        "question": "What is the Business Capital of Bangladesh?",
        "option_1": "Dhaka",
        "option_2": "Chattagram",
        "option_3": "Rajshahi",
        "option_4": "Khulna",
        "answer": 2
    },
    {
        "question": "What is HTML?",
        "option_1": "Programming Language",
        "option_2": "Style Sheet",
        "option_3": "Assembly Language",
        "option_4": "Markdown Language",
        "answer": 4
    },
]


# Program Title
def program_title_local():
    # Printing the program title
    program_title("Python Quiz App By Abrar")


# Printing the questions
def question_template(question_no, question):
    global right_answers  # Declare right_answers as global

    clear_screen()
    program_title_local()

    print(f"Question {question_no}/{len(questions)}: {question['question']}")
    print(f"  1) {question['option_1']}")
    print(f"  2) {question['option_2']}")
    print(f"  3) {question['option_3']}")
    print(f"  4) {question['option_4']}")

    while True:
        try:
            answer_submitted = int(input("\n Enter your choice: "))
            if answer_submitted in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


    if answer_submitted == question['answer']:
        right_answers += 1

def main():
    clear_screen()
    program_title_local() # Printing the Program title

    # Printing if the user wants to play or not
    while True:
        user_choice = input("Do you want to start the quiz now(yes/no): ").lower()
        if user_choice == "yes":
            break
        elif user_choice == "no":
            quit()

    # Start printing the questions
    question_no = 1
    for question in questions:
        question_template(question_no, question)
        question_no += 1
    
    # Printing the final result.
    clear_screen()
    result_text = f"You got total of {right_answers * 10} out of {len(questions) * 10} "
    print(" " * 8, "*" * 51)
    print(" " * 8, f"*{" " * round((50 - len(result_text))/2)}{result_text}{" " * (round((50 - len(result_text))/2) - 1)}*")
    print(" " * 8, "*" * 51)


if __name__ == "__main__":
    main()