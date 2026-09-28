# Personal Mini-Toolkit

## Project Overview

The **Personal Mini-Toolkit** is a menu-driven Python program created for the PLP Python Week 8 Final Project. It provides four simple tools that can be used from one main menu. The tools are a simple calculator, a to-do list, a number guessing game, and a name formatter. The project demonstrates important Python concepts learned during the course, including variables, input and output, conditionals, loops, lists, functions, and f-strings. The program also handles invalid input with friendly messages instead of crashing.

## Tools Included

### 1. Simple Calculator

Performs basic mathematical operations:

* Addition
* Subtraction
* Multiplication
* Division

### 2. To-Do List

Allows the user to:

* Add tasks
* View tasks
* Remove tasks

The tasks are stored in a Python list that changes while the program is running.

### 3. Number Guessing Game

The user tries to guess a secret number between 1 and 10. The program tells the user whether the guess is too high or too low until the correct number is entered.

### 4. Name Formatter

The user enters their name, and the program formats it into a clean and readable form.

## How to Run

Make sure Python is installed on your computer.

Open a terminal in the project folder and run:


python toolkit.py


The program will display the main menu:

1. Simple Calculator
2. To-Do List
3. Number Guessing Game
4. Name Formatter
5. Quit

Enter the number of the tool you want to use.

## Project Files

```text
plp-python-week8/
│
├── toolkit.py
├── toolkit_plan.txt
├── README.md
└── screenshots/
```

## Python Concepts Demonstrated

The project demonstrates:

* Variables
* `input()`
* `print()`
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* Lists
* Functions
* f-strings
* Input validation
* Basic error handling

## Screenshots

The `screenshots` folder contains evidence of the program being tested, including:

* Main menu
* Invalid menu choice
* Simple calculator
* To-do list
* Number guessing game
* Name formatter

## Reflection

The hardest part of this project was connecting the different tools to one menu while making sure the program returned to the menu after each tool finished. The bug that took the longest to fix was handling invalid user input, especially when the user entered text instead of a number. I learned that input validation is important because users do not always enter the information a program expects. The to-do list also helped me understand how a list can change while a program is running by adding and removing items. I became more comfortable using loops and conditionals to control how the program behaves. I also learned how functions can make a larger program easier to organize and understand. With one more week, I would add permanent file storage so that tasks and other information would not disappear when the program closes.
