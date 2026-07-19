Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 3.0
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 5.0
    }
}

resources = {
    "water": 500,
    "coffee": 100,
    "milk": 400,
}

def is_resource_sufficient(order_ingredients):
    """Returns True if order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def coins_counter():
    """Counts inserted coins and returns the total value."""
    print("Please insert coins:")
    quarters = int(input("Enter the number of quarters ($0.25)--- "))
    dimes = int(input("Enter the number of dimes ($0.10)--- "))
    nickels = int(input("Enter the number of nickels ($0.05)--- "))
    penny = int(input("Enter the number of pennies ($0.01)--- "))
    
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (penny * 0.01)
    return total

def transaction(money_received, drink_cost):
    """Returns True if payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

# --- Main Program Loop ---
money = 0
machine_offline = False

while not machine_offline:
    user_choice = input("\nWhich drink would you like to have? (espresso, latte, cappucino)--- ").lower()
    
    if user_choice == "off":
        machine_offline = True
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${money}")
    elif user_choice in Menu: 
        drink = Menu[user_choice]
        # Fixed capitalization to lowercase "ingredients"
        if is_resource_sufficient(drink["ingredients"]):
            payment = coins_counter()
            if transaction(payment, drink["cost"]):
                money += drink["cost"] # Successfully update profit
                make_coffee(user_choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select a valid drink.")