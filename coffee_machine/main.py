import menu 

main_menu = menu.menu
resources = menu.resources

espresso = menu.menu["espresso"]
latte = menu.menu["latte"]
cappuccino = menu.menu["cappuccino"]


def report(resources):

    print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${resources["money"]:.2f}\n")

    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

def money_input(drink):
    print("Insert some coins.")
    try:
        quarters = float(input("Enter the no of quaters: "))
        dimes = float(input("Enter the no of dimes: "))
        nickles = float(input("Enter the no of nickles: "))
        pennies = float(input("Enter the no of pennies: "))
    except ValueError:
        print("Invalid coin inserted. Transaction cancelled.")
        return None

    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

    if total >= drink["cost"]:
            change = total - drink["cost"]
            if change >= 0:
                print(f"Here is {change:.2f} in change.")
                return change
    else:
        print("Sorry that's not enough money. Money refunded..")
        return None

def making_drink(drink):
    print(f"The drink is ${drink["cost"]:.2f}.")
    if resources["water"] >= drink["ingredients"]["water"]:
        if resources["milk"] >= drink["ingredients"]["milk"]:
            if resources["coffee"] >= drink["ingredients"]["coffee"]:
                change = money_input(drink)
                if change is not None and change >= 0:
                        print(f"Here is your {choice}🧋  Enjoy!\n")
                        resources["water"] -= drink["ingredients"]["water"]
                        resources["milk"] -= drink["ingredients"]["milk"]
                        resources["coffee"] -= drink["ingredients"]["coffee"]
                        resources["money"] += drink["cost"]
            else:
                print(f"Sorry there is not enough coffee..")
        else:
            print(f"Sorry there is not enough milk..")
    else:
        print(f"Sorry there is not enough water..")
                  

while True:
 
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        print("Few seconds! The machine is shutting down....")
        break 

    if choice == 'report':
        report(resources)
        continue

    if choice == 'espresso':
        making_drink(espresso)
    elif choice == 'latte':
        making_drink(latte)
    elif choice == 'cappuccino':
        making_drink(cappuccino)
    else:
        print(f"Sorry {choice} not the menu... Try Again!")
        continue
    
    
        






