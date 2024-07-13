from emoji import emojize

string = input("Input: ")

emojized_string = emojize(string, language='alias')

print("Output:", emojized_string)
