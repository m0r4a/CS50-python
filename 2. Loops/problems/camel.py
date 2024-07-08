def main():
    var_name = input("What's your variable name: ")

    for letter in var_name:

        if letter.isupper():
            print("_", letter.lower(), end="", sep="")

        else:
            print(letter, end="")

    print()


main()
