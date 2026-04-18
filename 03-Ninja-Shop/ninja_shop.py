#Shop Data - Dictionary
shop_items = {
    "Kunai": {"price": 50, "stock": 10},
    "Scroll": {"price": 150, "stock": 0},
    "Katana": {"price": 500, "stock": 2}
}

# Display Shop Menu - Start of the program, display all available items
print("Available items: ", shop_items)

# Custom Exceptions.
class ItemNotFoundError(Exception):
    '''Should raise when the user enters an item name that doesn't exist in the shop.'''
    pass

class OutOfStockError(Exception):
    '''Should raise when the user tries to buy an item with 0 stock.'''
    pass

class InsufficientFundsError(Exception):
    '''Should raise when the user's balance is lower than the item price.'''
    pass

# Purchase Function.
def buy_item(item_name, wallet_balance):
    '''Raises ItemNotFoundError if the item is not in 'shop_items'.'''
    if item_name not in shop_items:
        raise ItemNotFoundError(f"The item '{item_name}' you're looking for is not in the shop menu.")
    item_data = shop_items[item_name]

    '''Raises OutOfStockError if the item's stock is 0.'''
    if item_data["stock"] <= 0:
        raise OutOfStockError(f"The item '{item_name}' is currently out of stock.")

    '''Raises InsufficientFundsError if wallet_balance < price, else decreases the stock by 1 and returns the remaining balance.'''
    if wallet_balance < item_data["price"]:
       raise InsufficientFundsError(f"Insufficient funds for {item_name} ({item_data['price']} Ryo needed).")
    
    item_data["stock"] -= 1
    new_balance = wallet_balance - item_data["price"]
    return new_balance
    
#User Interaction.
print("--- Welcome to the Ninja Shop ---")
for item, info in shop_items.items():
    print(f"{item}: Price = {info['price']} Ryo, Stock = {info['stock']}")

try:
    current_balance = float(input("\nEnter your current wallet balance in Ryo: "))
except ValueError:
    print("Invalid balance format. Exiting the shop.")
    exit()

while True:
    print(f"\nCurrent Balance: {current_balance} Ryo")
    choice = input("Enter the name of the item you wish to buy (or type 'exit' to leave): ")
    if choice.lower() == 'exit':
        print("Thank you for visiting the Ninja Shop!")
        break

    try:
        current_balance = buy_item(choice, current_balance)
        print(f"Successfully purchased {choice}! Remaining balance: {current_balance} Ryo")
    except (ItemNotFoundError, OutOfStockError, InsufficientFundsError) as e:
        print(f"Purchase failed: {e}")
    finally:
        print("--- Transaction attempt finished ---")




    

    
