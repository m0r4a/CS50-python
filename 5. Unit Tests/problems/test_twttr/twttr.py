def main():
    string = input("Phrase: ")
    shorten(string)


def shorten(word):
    output = ""
    for letter in word:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
            output += letter
        else:
            pass

    return output


if __name__ == "__main__":
    main()
