def main():
    greet = input("Greet: ")
    print(f"${value(greet)}")


def value(greeting):
    clean_greet = greeting.strip().lower()

    if clean_greet.startswith("hello"):
        amount = 0

    elif clean_greet.startswith("h"):
        amount = 20

    else:
        amount = 100

    return amount


if __name__ == "__main__":
    main()
