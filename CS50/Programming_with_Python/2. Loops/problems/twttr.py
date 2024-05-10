def main():

    output = ""

    string = input("Input: ")

    for letter in string:

        output += vowel_remover(letter)

    print(output)


def vowel_remover(letter):
    return "" if letter.lower() in ["a", "e", "i", "o", "u"] else letter


main()
