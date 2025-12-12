# Pedro Padilla
# 12/12/2025
# Assignment Name: CTI110 Final Project - Text-Based Game
# Brief description of program: A simple text-based character interaction and combat game.

import random
import time

# --- FUNCTION DEFINITIONS ---

def create_character():
    """
    Creates the main character dictionary based on user input.
    (Meets 'Character Creation' requirement) [cite: 4]
    :return: A dictionary representing the player character.
    """
    print("🌟 Character Creation 🌟")
    time.sleep(1) # Use time library for a pause 

    # Get character name
    name = input("Enter your character's name: ").strip()

    # Get attributes (using simple input validation)
    # Ensure health starts high and strength is reasonable
    while True:
        try:
            strength = int(input("Enter your character's strength (5-15): "))
            if 5 <= strength <= 15:
                break
            else:
                print("Strength must be between 5 and 15.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    character = {
        "name": name,
        "health": 100,
        "max_health": 100,
        "strength": strength,
        "inventory": {},  # Optional inventory dictionary
    }
    print(f"\nWelcome, {character['name']}! Your adventure begins.\n")
    return character # This is a value-returning function

# Non-value returning function 
def display_character(character):
    """
    Displays the character's attributes.
    (Meets 'Displaying Characters' requirement) 
    """
    print("-" * 30)
    print(f"👤 Character Stats: {character['name']}")
    print(f"   Health: {character['health']} / {character['max_health']}")
    print(f"   Strength: {character['strength']}")
    if character.get("inventory"):
        print(f"   Inventory: {', '.join(character['inventory'].keys())}")
    else:
        print("   Inventory: Empty")
    print("-" * 30)

# Value-returning function (Can represent "Attacking/Game Logic") 
def calculate_damage(attacker_strength):
    """
    Calculates a random amount of damage the attacker deals.
    (Meets 'Attack functionality' requirement part 1: logic) 
    :param attacker_strength: The strength attribute of the attacker.
    :return: The total damage dealt.
    """
    # Use random library to add variance to the attack 
    damage = attacker_strength + random.randint(-2, 3)
    # Ensure damage is never negative
    return max(1, damage)

# Non-value returning function for the game loop action
def combat_round(player_char, enemy_char):
    """
    Simulates a single combat round, reducing defender health.
    (Meets 'Attack functionality' requirement part 2: health reduction) 
    :param player_char: The player's character dictionary.
    :param enemy_char: The enemy's character dictionary.
    """
    print("\n⚔️ Combat Round! ⚔️")
    time.sleep(1)

    # Player attacks enemy
    player_damage = calculate_damage(player_char['strength'])
    enemy_char['health'] -= player_damage 
    print(f"{player_char['name']} attacks! They deal {player_damage} damage to the {enemy_char['name']}!")
    
    if enemy_char['health'] > 0:
        # Enemy attacks player (simple logic)
        enemy_damage = calculate_damage(enemy_char['strength'])
        player_char['health'] -= enemy_damage 
        print(f"The {enemy_char['name']} retaliates! You take {enemy_damage} damage.")
    
    time.sleep(1)

# Main Function 
def main():
    """
    The main function that runs the game loop.
    (Meets 'Main Function and Game Flow' requirement) 
    """
    # Initialize the game 
    player = create_character()
    
    # Create a simple enemy
    enemy = {
        "name": "Goblin",
        "health": 50,
        "max_health": 50,
        "strength": 7,
    }
    
    game_running = True
    
    # The Game Loop 
    while game_running:
        display_character(player)
        print(f"🚨 Enemy Spotted: {enemy['name']} (Health: {enemy['health']})")
        
        print("\nWhat do you do?")
        # Allows for displaying and attacking characters 
        print("1. 👊 Attack")
        print("2. 🏃 Run Away (Exit)") # Provides a way to exit the game loop 
        
        choice = input("Enter choice (1 or 2): ").strip()
        print("\n")
        
        if choice == '1':
            combat_round(player, enemy)
            
            # Check win/loss conditions
            if player['health'] <= 0:
                print("💀 You have been defeated! Game Over.")
                game_running = False
            elif enemy['health'] <= 0:
                print(f"🎉 You defeated the {enemy['name']}! You win the game!")
                game_running = False
                
        elif choice == '2':
            print("You wisely run away. The game ends.")
            game_running = False # Way to exit the game loop 
            
        else:
            print("Invalid choice. Try again.")
            
        time.sleep(1)
 
if __name__ == "__main__":
    main()