def show_menu():
    print("\n--- Fantasy Item Shop ---")
    print("1. Sword - 50 gold")
    print("2. Shield - 30 gold")
    print("3. Potion - 20 gold")
    print("4. Armor - 75 gold")
    print("5. Inventory bekijken")
    print("6. Winkel verlaten")
    print("7. Item verkopen")
    print("8. Werken")


def show_inventory(inventory):
    if len(inventory) == 0:
        print("Je inventory is leeg.")
    else:
        print("\n--- Inventory ---")
        for item in inventory:
            print(item)


def can_buy(gold, price):
    return gold >= price


def buy_item(gold, inventory, item_name, price):
    if can_buy(gold, price):
        gold -= price
        inventory.append(item_name)
        print(f"Je hebt {item_name} gekocht!")
    else:
        print("Je hebt niet genoeg gold!")

    return gold


def sell_item(gold, inventory):
    show_inventory(inventory)
    item = input("Welk item wil je verkopen? ")

    if item in inventory:
        inventory.remove(item)
        gold += 10
        print(f"Je hebt {item} verkocht voor 10 gold!")
    else:
        print("Je hebt dit item niet.")

    return gold


def work(gold):
    gold += 20
    print("Je hebt 20 gold verdiend!")
    return gold


def choose_difficulty():
    while True:
        print("1. Easy - 150 gold")
        print("2. Normal - 100 gold")
        print("3. Hard - 50 gold")

        choice = input("Kies een moeilijkheid: ")

        match choice:
            case "1":
                return 150
            case "2":
                return 100
            case "3":
                return 50
            case _:
                print("Ongeldige keuze!")


player_gold = choose_difficulty()
inventory = []

while True:
    print(f"\nJe hebt {player_gold} gold.")

    show_menu()
    choice = input("Maak een keuze: ")

    match choice:
        case "1":
            player_gold = buy_item(player_gold, inventory, "Sword", 50)

        case "2":
            player_gold = buy_item(player_gold, inventory, "Shield", 30)

        case "3":
            player_gold = buy_item(player_gold, inventory, "Potion", 20)

        case "4":
            player_gold = buy_item(player_gold, inventory, "Armor", 75)

        case "5":
            show_inventory(inventory)

        case "6":
            print("Bedankt voor je bezoek!")
            break

        case "7":
            player_gold = sell_item(player_gold, inventory)

        case "8":
            player_gold = work(player_gold)

        case _:
            print("Ongeldige keuze!")