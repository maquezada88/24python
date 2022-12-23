import random

def usage():
    print("Use addition, multiplication, subtraction, or division in order to get 24!")

def rand_num():
    return random(0,3)

def validate_difficulty(difficulty):
    if int(difficulty) < 1 or int(difficulty) > 3:
        print("Error. Enter a digit between 1 and 3.")
        return False
    
    return True
