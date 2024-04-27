def main():

    expression = input("Expression: ")

    values = expression.split(" ")

    match values[1]:

        case "+":
            print(float(values[0]) + float(values[2]))

        case "-":
            print(float(values[0]) - float(values[2]))

        case "*":
            print(float(values[0]) * float(values[2]))

        case "/":
            if values[2] != 0:
                print(float(values[0]) / float(values[2]))

            else:
                print("The divisor can't be 0")


main()
