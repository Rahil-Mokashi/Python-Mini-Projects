import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


image = r'''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

print(image)

primary_condition = True
main_condition = True

def add(a, b):
    """So this function takes two inputs and return addtion of the inputs"""
    return a + b

def sub(a, b):
    """So this function takes two inputs and return subtraction of the inputs"""
    return a - b

def multiply(a, b):
    """So this function takes two inputs and return multiplication of the inputs"""
    return a * b

def divide(a, b):
    """So this function takes two inputs and return division of the inputs and also check if the second input is 0"""
    if b == 0:
        return "Infinite!"
    else:
        return a / b



while main_condition == True:
    num1 = float(input("What's your first no?: "))
    primary_condition = True
    while primary_condition == True:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        
        num2 = float(input("What's your next number?: "))

        if operator == '+':
            solution = add(a = num1, b = num2)
            print(f"{num1} {operator} {num2} = {solution:.2f}")
        elif operator == '-':
            solution = sub(a = num1, b = num2)
            print(f"{num1} {operator} {num2} = {solution:.2f}")
        elif operator == '*':
            solution = multiply(a = num1, b = num2)
            print(f"{num1} {operator} {num2} = {solution:.2f}")
        elif operator == '/':
            solution = divide(a = num1, b = num2)
            if solution == 'Infinite!':
                print(f"The solution is {solution}. Try different no")
                break
            print(f"{num1} {operator} {num2} = {solution:.2f}")
        else:
            print("Invalid Operator....")
            break

        choice = input(f"Type 'y' to continue calculating with {solution:.2f}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = solution
            primary_condition = True 
        elif choice == 'n':
            clear_screen()
            primary_condition = False
        else:
            print("Unidentified choice...\nExiting program...")
            primary_condition = False
            main_condition = False
            break
    