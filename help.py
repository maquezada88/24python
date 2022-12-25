import random
import json

def usage():
    print("Use addition, multiplication, subtraction, or division in order to get 24!")
    print("Can only use each number once!")

def get_set_of_numbers(difficulty):
    

    if difficulty == 1:
        nums = get_easy_numbers()
        return nums
    elif difficulty == 2:
        nums = get_medium_numbers()
        return nums
    elif difficulty ==3:
        nums = get_hard_numbers()
        return nums
    else:
        print("ERROR IN GET SET OF NUMBERS")

def get_easy_numbers():
    x = random.randint(1, 5) - 1
    f = open('easy_numbers.json')
    data = json.load(f)
    easy_nums = data['easy'][x]
    return easy_nums

def get_medium_numbers(x):
    x = random.randint(1, 5) - 1
    f = open('medium_numbers.json')
    data = json.load(f)
    medium_nums = data['easy'][x]
    return medium_nums

def get_hard_numbers(x):
    x = random.randint(1, 5) - 1
    f = open('hard_numbers.json')
    data = json.load(f)
    hard_nums = data['easy'][x]
    return hard_nums

def validate_difficulty(difficulty):
    if int(difficulty) < 1 or int(difficulty) > 3:
        print("Error. Enter a digit between 1 and 3.")
        return False
    
    return True
