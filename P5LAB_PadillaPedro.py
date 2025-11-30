# Pedro Padilla
# 11/30/2025
#P5LAB
# Simulates a self-checkout machine and calculates/displays the change due 
# in dollars, quarters, dimes, nickels, and pennies.

import random

DOLLAR_VALUE = 100
QUARTER_VALUE = 25
DIME_VALUE = 10
NICKEL_VALUE = 5
PENNY_VALUE = 1

def disperse_change(change_due_float):

    change_due_cents = round(change_due_float * 100)
    
    print(f"\nChange is: ${change_due_float:.2f}")

    dollars = change_due_cents // DOLLAR_VALUE
    change_due_cents %= DOLLAR_VALUE

    quarters = change_due_cents // QUARTER_VALUE
    change_due_cents %= QUARTER_VALUE

    dimes = change_due_cents // DIME_VALUE
    change_due_cents %= DIME_VALUE

    nickels = change_due_cents // NICKEL_VALUE
    
    pennies = change_due_cents % NICKEL_VALUE 

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")


def main():

    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${total_owed:.2f}")

    while True:
        try:
            cash_paid = float(input("How much cash will you put in the self-checkout? "))
            if cash_paid < total_owed:
                print("Error: Cash paid must be greater than or equal to the total owed.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the cash amount.")


    change_owed = round(cash_paid - total_owed, 2)
    
    if change_owed > 0:
        disperse_change(change_owed)
    else:
        print("No change owed.")


if __name__ == "__main__":
    main()