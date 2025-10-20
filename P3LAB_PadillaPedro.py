#Program: P3LAB_LastnameFirstname.py
#Author: Pedro Padilla
#Date: October 19, 2025
#Purpose: Calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed for a user-inputted amount of money.


def calculate_change():
    """
    Prompts the user for a money amount, calculates the change distribution,
    and prints the results according to the specified rules.
    """
    try:

        money_float = float(input("Enter the amount of money as a float: $"))
        
        total_cents = int(round(money_float * 100))
        
        remaining_cents = total_cents
        
        if total_cents == 0:
            print("No change")
            return
            
        def print_denomination_count(count, singular_name, plural_name):
            """Displays the coin count, using singular or plural name if count > 0."""
            if count > 0:
                name_to_use = singular_name if count == 1 else plural_name
                print(f"{count} {name_to_use}")

        
        dollars = remaining_cents // 100
        remaining_cents %= 100
        print_denomination_count(dollars, "Dollar", "Dollars")

        quarters = remaining_cents // 25
        remaining_cents %= 25
        print_denomination_count(quarters, "Quarter", "Quarters")

        dimes = remaining_cents // 10
        remaining_cents %= 10
        print_denomination_count(dimes, "Dime", "Dimes")

        nickels = remaining_cents // 5
        remaining_cents %= 5
        print_denomination_count(nickels, "Nickel", "Nickels")

        pennies = remaining_cents // 1
        print_denomination_count(pennies, "Penny", "Pennies")

    except ValueError:
        print("Invalid input. Please enter a numerical value (float).")

if __name__ == "__main__":

    calculate_change()
