# initialisation - create a dictionary to store characters where each of the character have : chakra(int) and lvl(int)
ninja_stats = {
    "Naruto": {"chakra": 100, "lvl": 1},
    "Sasuke": {"chakra": 80, "lvl": 1}
}

#  At the start of the program, display all characters along with their chakra and lvl

print("Display characters: ", ninja_stats)

# custom exceptions - define the following custom exception classe : InsufficientChakraError

class InsufficientChakraError(Exception):
    pass

# function - write a function "use_jutsu(character_name, cost)" that checks if the character exist (raise a keyerror or use .get()), checks if the current chakra is > or = to the cost (if yes then substract the cost and show the chakra value, else raise an exception "InsufficientChakraError" with a message.)

def use_jutsu(character_name, cost):
    #check if character exist
    if character_name not in ninja_stats:
        raise KeyError(f"Character name : {character_name} not found.")
    #get ninja stats
    stats = ninja_stats[character_name]

    #check the stats
    if stats["chakra"] >= cost:
        stats["chakra"] -= cost
        print(f"{character_name} used a jutsu! Remaining chakra: {stats['chakra']}")
        return stats["chakra"]
    else:
        raise InsufficientChakraError(f"Chakra of {character_name} not sufficient.")
    
while True:
    try:
        name = input("Enter the name of the character: ")
        if name.lower() == "exit":
            break
            
        cost = int(input("Enter the chakra cost of the jutsu: "))
        new_chakra = use_jutsu(name, cost)
        print(f"Success! {name} has now {new_chakra} chakra")

    except ValueError:
        print("Invalid input. Please enter a valid number for chakra cost.")
    except KeyError as e:
        print(f"Error: {e}")
    except InsufficientChakraError as e:
        print(f"Error: {e}")
    finally:
        print("Microproject attempt finished.\n")