def main():

    amount_due = 50

    while amount_due > 0:

        print("Amount Due:", amount_due)

        coin = int(input("Insert Coin: "))

        amount_due = coin_checker(amount_due, coin)

    print("Change Owed:", -amount_due)


def coin_checker(amount_due, coin):
    return amount_due - coin if coin in [25, 10, 5] else amount_due


main()
