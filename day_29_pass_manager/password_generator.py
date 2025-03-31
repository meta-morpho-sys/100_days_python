import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# --------------------- Mechanism to Pick Letters, Numbers and Symbols ------------------
#  1st layer of randomness: We decide how many letters/numbers/symbols the code will pick for the password
letters_to_pick = random.randint(8,10)
numbers_to_pick = random.randint(2,4)
symbols_to_pick = random.randint(2,4)

# --------------------- Mechanism to randomly append them to a characters list ----------
# 2nd layer of randomness: We use the random integers from above as a range for the random choice from relative array
password_chars_list = []

[password_chars_list.append(random.choice(letters)) for char in range(letters_to_pick)]
[password_chars_list.append(random.choice(numbers)) for num in range(numbers_to_pick)]
[password_chars_list.append(random.choice(symbols)) for sym in range(symbols_to_pick)]

# --------------------- Mechanism to shuffle the chars and output a password ------------
# 3rd layer of randomness - shuffling the characters before transforming them into a password string

password = ''
for char in password_chars_list:
    password += char

print(password)

