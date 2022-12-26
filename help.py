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

def validate_expression(expression, nums):
    exp = expression.strip() #remove leading and trail spaces 

    op = validate_operator(expression) #get and validate operator
    if(op == 'E'):
        return False
    
    split_exp = exp.split(op) #split up by operator
    
    if validate_expression_helper(split_exp, nums):
        print("nums in validate_expression: ", nums)

    return True

def validate_operator(expression):

    if('+' in expression ):
        return '+'
    elif('-' in expression):
        return '-'
    elif('*' in expression):
        return '*'
    elif('/' in expression):
        return '/'
    else:
        print("ERROR. NO VALID OPERATORS FOUND IN STRING.")
        return 'E'

def validate_expression_helper(split_exp, nums):
    #make sure both operands are integers
    if(int(split_exp[0])==False or int(split_exp[1]) == False):
        print("ERROR. OPERANDS NEED TO BE INTEGERS.")
        return False

    #make sure the operands are in the list. need to truncate list after checking first operand.
    flag = False
    if int(split_exp[0]) in nums:
        flag = True
    else:
        print("ERROR FIRST VALUE NOT IN LIST:", split_exp[0])
        print("NUMS IN LIST:", nums)
        print("split list:", split_exp)
        return False
    
    nums.remove(int(split_exp[0]))

    if int(split_exp[1]) in nums:
        flag = True
        nums.remove(int(split_exp[1]))
    else:
        print("ERROR. SECOND VALUE NOT IN LIST:", split_exp[1])
        print("NUMS IN LIST:", nums)
        return False
    
    return flag
