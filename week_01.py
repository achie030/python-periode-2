
print("Welcome to the Fantasy Item Shop!")

# Ask the player for their name
player_name = input("What is your name? ")

player_gold = 100
inventory = []

print("Hello", player_name, "! You have", player_gold, "gold.")

# Items in the shop
items = ["Sword", "Shield", "Potion", "Bow"]

print("Items in the shop:")

for item in items:
    print(item)

# Shop menu
while True:
    print()
    print("=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("What would you like to do? ")

    match choice:
        case "1":
            if player_gold >= 50:
                player_gold = player_gold - 50
                inventory.append("Sword")
                print("You bought a Sword!")
                print("Remaining gold:", player_gold)
            else:
                print("You don't have enough gold!")

        case "2":
            if player_gold >= 40:
                player_gold = player_gold - 40
                inventory.append("Shield")
                print("You bought a Shield!")
                print("Remaining gold:", player_gold)
            else:
                print("You don't have enough gold!")

        case "3":
            if player_gold >= 20:
                player_gold = player_gold - 20
                inventory.append("Potion")
                print("You bought a Potion!")
                print("Remaining gold:", player_gold)
            else:
                print("You don't have enough gold!")

        case "4":
            if player_gold >= 60:
                player_gold = player_gold - 60
                inventory.append("Bow")
                print("You bought a Bow!")
                print("Remaining gold:", player_gold)
            else:
                print("You don't have enough gold!")

        case "5":
            print("Your inventory:")

            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                for item in inventory:
                    print("-", item)

        case "6":
            print("Thanks for visiting,", player_name, "!")
            print("You have", player_gold, "gold left.")
            break

        case _:
            print("Invalid choice!")
