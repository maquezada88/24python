from help import *


def main():
    valid_difficulty = False
    difficulty = -1

    print("Enter 1 for easy.")
    print("Enter 2 for medium.")
    print("Enter 3 for hard.")

    while valid_difficulty == False:

        difficulty = input('Choose the difficulty you wish to play on.')
        if(difficulty.isdigit()):
            difficulty = int(difficulty)
            valid_difficulty = validate_difficulty(difficulty)
        print(difficulty)


if __name__ == "__main__":
    main()