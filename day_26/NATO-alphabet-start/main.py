"""
Little tool for spelling out names using NATO Alphabet
"""
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows() }

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a name. No white spaces for now :-) :').upper()
phon_words_list = [nato_phonetic_dict[letter] for letter in user_input]
print(phon_words_list)

