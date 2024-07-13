import inflect

name_list = []
p = inflect.engine()

while True:
    try:
        name_list.append(input("Name: "))

    except EOFError:
        inflect_list = p.join(name_list)
        print("Adieu, adieu, to", inflect_list)
        break
