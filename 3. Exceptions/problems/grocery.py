def main():
    inventory = {}

    while True:
        try:
            item = input("").upper()
            if item in inventory:
                inventory[item]['amount'] += 1
            else:
                inventory[item] = {'name': item, 'amount': 1}

        except EOFError:
            for item in sorted(inventory.keys()):
                value = inventory[item]
                print(f"{value['amount']} {value['name']}")

            exit()


main()
