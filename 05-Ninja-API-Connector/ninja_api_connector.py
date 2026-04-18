import requests

# Custom Exceptions

'''Raised if the server returns a status code other than 200.'''
class APIDownError(Exception): pass 
'''Raised if the data received is empty or missing expected fields.'''
class DataCorruptedError(Exception): pass

# Sync function 

def sync_rankings():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code != 200:
        raise APIDownError(f"Server returned error code: {response.status_code}")

    data = response.json()
    if not data:
        raise DataCorruptedError("The server returned an empty list.")
    
    ninja_list = [] # Empty list
    for user in data:
        name = user.get("name")
        city = user.get("address", {}).get("city")

        if name and city:
            ninja_list.append(f"Ninja: {name} from {city}")
        else:
            raise DataCorruptedError("Missing mandatory fields in server data.")
    
    return ninja_list

# User Interaction
print("--- NINJA API CONNECTOR ---")
synchronisation = input("Do you want to synchronize? (yes/no): ").strip().lower()

if synchronisation == "yes":
    print("Connecting to the hidden leaf cloud server...")
    try:
        # IMPORTANT : On stocke le résultat de la fonction dans 'rankings'
        rankings = sync_rankings() 
        
    except requests.exceptions.RequestException as e: 
        print(f"Network Error: Could not connect to the server. ({e})")
    except (APIDownError, DataCorruptedError) as e:
        print(f"Server Error: {e}")
        
    else:
        # Ce bloc s'exécute uniquement si aucune exception n'a été levée
        print("\n--- Global Ninja Rankings ---")
        for ninja in rankings:
            print(ninja)
        
        # Sauvegarde dans le fichier
        with open("rankings.txt", "w") as f:
            for ninja in rankings:
                f.write(ninja + "\n")
        print("\nRankings successfully saved to rankings.txt")
        
    finally:
        # S'exécute quoi qu'il arrive
        print("Closing connection to server.")
        print("-" * 30)
else:
    print("Synchronization cancelled.")