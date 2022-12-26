from help import *
import json


def main():
    valid_difficulty = False
    difficulty = -1

    print("Enter 1 for easy.")
    print("Enter 2 for medium.")
    print("Enter 3 for hard.")

    while valid_difficulty == False:
        #gets difficulty and validates it
        difficulty = input('Choose the difficulty you wish to play on.')
        if(difficulty.isdigit()):
            difficulty = int(difficulty)
            valid_difficulty = validate_difficulty(difficulty)
        else:
            print("Error. Please enter a digit between 1-3")
    
    #get set of numbers
    nums = get_set_of_numbers(difficulty)
    print("your set of numbers are:", nums)

    usage()

    #gets expression and validates it
    exp = input("Enter your first expression.")
    validate_expression(exp, nums)

if __name__ == "__main__":
    main()
