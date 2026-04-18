# Character data. 
player = {"name": "Naruto", "hp": 100, "chakra": 50, "dmg": 20}
enemy = {"name": "Sasuke", "hp": 100, "chakra": 50, "dmg": 18}

# Custom Exceptions
class TargetDeadError(Exception):
    '''Raised if a character tries to attack a target that has 0 HP.'''
    pass

class InvalidActionError(Exception):
    '''Raised when the user inputs an action that is not "1" or "2".'''
    pass

class StaminaExhaustedError(Exception):
    '''Raised when a player tries to use a Special Move without enough Chakra.'''
    pass


# Combat Function
def execute_attack(attacker, target, attack_type):
    target_name = target["name"]
    if target_name == player["name"]:
        target = player
    elif target_name == enemy["name"]:
        target = enemy

    attacker_name = attacker["name"]
    if attacker_name == player["name"]:
        attacker = player
    elif attacker_name == enemy["name"]:
        attacker = enemy

    '''Raises TargetDeadError if target["hp"] <= 0'''
    if target["hp"] <= 0:
        raise TargetDeadError(f"{target_name} has no more HP.")
    
    '''If attack_type == "1" (Standard): Deals attacker["dmg"] to the target.'''
    '''elif attack_type == "2" (Special): Deals attacker["dmg"] * 2 but costs 20 Chakra.'''
    if attack_type == "1":
        target["hp"] -= attacker["dmg"]
        print(f"-> {attacker['name']} uses Standard Attack! {target['name']} loses {attacker['dmg']} HP.")

    elif attack_type == "2":
        if attacker["chakra"] < 20:
            raise StaminaExhaustedError(f"{attacker_name} does not have enough Chakra for a Special Move.")
    
        damage = attacker["dmg"] * 2
        target["hp"] -= damage
        attacker["chakra"] -= 20
        print(f"-> {attacker['name']} UNLEASHES A SPECIAL MOVE! {target['name']} loses {damage} HP.")
    else:
        raise InvalidActionError("Action unknown. Choose 1 or 2.")

    if target["hp"] < 0:
        target["hp"] = 0

# User Interaction
print("=== Battle Start ===")
'''The battle continues as long as both characters have hp > 0.'''

# Display Status
'''Displaying at the start of each turn the current HP and Chakra of both fighters'''
while player["hp"] > 0 and enemy["hp"] > 0: 
    '''At the beginning of each turn, display the HP and Chakra for both characters.'''
    print(f"\n{player['name']} - HP: {player['hp']}, Chakra: {player['chakra']}")
    print(f"{enemy['name']} - HP: {enemy['hp']}, Chakra: {enemy['chakra']}")

    '''Player Turn: Prompt the user to choose an action. Handle all exceptions.'''
    try:
        action = input(f"\nYour turn {player['name']}: 1 for Standard Attack, 2 for Special Move: ")
        execute_attack(player, enemy, action)
    except (TargetDeadError, InvalidActionError, StaminaExhaustedError) as e:
        print(f"!!! {e}")
        continue

    '''Enemy Turn: If still alive, the enemy automatically performs a Standard Attack or Special Move based on its current Chakra.'''
    if enemy["hp"] > 0:
        print(f"\n{enemy['name']} is preparing an entry...")
        enemy_action = "2" if enemy["chakra"] >= 20 else "1"
        try:
            execute_attack(enemy, player, enemy_action)
            '''Handle exceptions if the enemy tries to attack a dead target.'''
        except TargetDeadError as e:
            break
    print("-" * 30)

'''Use an else block to announce the winner when the loop ends.'''
print("\n=== BATTLE OVER ===")
if player["hp"] > 0:
    print(f"VICTORY: {player['name']} wins with {player['hp']} HP remaining!")
else:
    print(f"DEFEAT: {enemy['name']} has defeated you...")

print("Combat sequence finished.")