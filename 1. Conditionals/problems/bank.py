def main():
    greet = input("Greet: ")

    clean_greet = greet.strip().lower()

    if clean_greet.startswith("hello"):
        print("$0")

    elif clean_greet.startswith("h"):
        print("$20")

    else:
        print("$100")


main()
