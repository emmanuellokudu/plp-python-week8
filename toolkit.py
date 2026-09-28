# Personal Mini-Toolkit
# PLP Python Week 8 Final Project

# This list stores the tasks added by the user.
tasks = []


# Simple Calculator
# This tool performs basic mathematical calculations.
def calculator():
    print("\n========== SIMPLE CALCULATOR ==========")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = first_number + second_number
            print(f"\nResult: {first_number} + {second_number} = {result}")

        elif operation == "2":
            result = first_number - second_number
            print(f"\nResult: {first_number} - {second_number} = {result}")

        elif operation == "3":
            result = first_number * second_number
            print(f"\nResult: {first_number} x {second_number} = {result}")

        elif operation == "4":
            if second_number == 0:
                print("\nYou cannot divide by zero.")
            else:
                result = first_number / second_number
                print(
                    f"\nResult: {first_number} / "
                    f"{second_number} = {result}"
                )

        else:
            print("\nInvalid operation. Please choose 1-4.")

    except ValueError:
        print("\nInvalid number. Please enter numbers only.")


# To-Do List
# This tool allows the user to add, view, and remove tasks.
def todo_list():
    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task == "":
                print("Task cannot be empty.")
            else:
                tasks.append(task)
                print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task removed: {removed_task}")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select 1-4.")


# Number Guessing Game
# This tool lets the user guess a secret number until they get it right.
def guessing_game():
    secret_number = 7
    attempts = 0

    print("\n========== NUMBER GUESSING GAME ==========")
    print("I am thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")

            elif guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(
                    f"Correct! You guessed the number in "
                    f"{attempts} attempts."
                )
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Name Formatter
# This tool formats the user's name in a clean and readable way.
def name_formatter():
    print("\n========== NAME FORMATTER ==========")

    name = input("Enter your full name: ").strip()

    if name == "":
        print("You did not enter a name.")
    else:
        formatted_name = name.title()

        print(f"\nOriginal name: {name}")
        print(f"Formatted name: {formatted_name}")
        print(f"Welcome, {formatted_name}!")


# Main menu
# This loop keeps the toolkit running until the user chooses Quit.
def main():
    print("========================================")
    print("       WELCOME TO THE MINI-TOOLKIT")
    print("========================================")
    print("Choose a tool from the menu to get started.")

    while True:
        print("\n========================================")
        print("          PERSONAL MINI-TOOLKIT")
        print("========================================")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Name Formatter")
        print("5. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            name_formatter()

        elif choice == "5":
            print("\nThank you for using the Personal Mini-Toolkit.")
            print("Goodbye!")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select an option from 1 to 5."
            )


# Start the program
main()