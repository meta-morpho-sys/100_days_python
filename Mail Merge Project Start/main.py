# Simple code for Mail Merging
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    text = starting_letter.read()


with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    print(names)
    for name in names:
        with open(f"./Output/ReadyToSend/LetterTo{name}.txt", "w") as ready:
            new_text = text.replace("[Name]", name.strip())
            print(new_text)
            ready.write(new_text)

