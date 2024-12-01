import random

com_num=random.randint(1,100)

def welcome() -> int:
    print(" Welcome to the Number Guessing Game!\n  I'm thinking of a number between 1 and 100. \n  You have 5 chances to guess the correct number.")
    print(''' Please select the difficulty level:\n
                \t1. Easy (10 chances)\n
                \t2. Medium (5 chances)\n
                \t3. Hard (3 chances)''')
    choice = int(input(' Enter your choice: '))
    if choice < 1 or choice > 3:
        print('\nYou enter something out of my range.')
        raise ValueError('You should enter value between 1 to 3.')
    dificult={1: 'Easy', 2: 'Medium', 3: 'Hard'}
    chance=[10, 5, 3]
    print(f" \nGreat! You have selected the {dificult[choice]} difficulty level. \n\tLet's start the game!")
    return chance[choice-1]

def procced_next(user_num: int, attempt:int):
    if user_num < com_num:
        print("\033[91m"+f' Incorrect! The number is grater than {user_num}'+"\033[0m")
        return False
    elif user_num > com_num:
        print("\033[91m"+f' Incorrect! The number is less than {user_num}'+"\033[0m")
        return False
    else:
        print(f' Congratulation! You choose the right number in {attempt} attempts.')
    return True

def fail():
    print(f' You lose! You are unable to select right number was {com_num}.')