import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_alphabet_source = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet_source.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
valid_input = False

while not valid_input:
    user_input = input("Enter a word to convert to NATO alphabet:")
    try:
        print([nato_dict[char] for char in user_input.upper()])
    except KeyError:
        print("A-Z characters only")
    else:
        valid_input = True
