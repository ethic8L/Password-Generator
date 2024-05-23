# Password Generator Project

ascii_art = r"""

 ____    __    ___  ___  _    _  _____  ____  ____      ___  ____  _  _  ____  ____    __    ____  _____  ____ 
(  _ \  /__\  / __)/ __)( \/\/ )(  _  )(  _ \(  _ \    / __)( ___)( \( )( ___)(  _ \  /__\  (_  _)(  _  )(  _ \
 )___/ /(__)\ \__ \\__ \ )    (  )(_)(  )   / )(_) )  ( (_-. )__)  )  (  )__)  )   / /(__)\   )(   )(_)(  )   /
(__)  (__)(__)(___/(___/(__/\__)(_____)(_)\_)(____/    \___/(____)(_)\_)(____)(_)\_)(__)(__) (__) (_____)(_)\_)


"""

print(ascii_art)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j ', 'k', 'l ', 'm', 'n', 'o', 'p', 'q ', 'r', ' s ', 't', 'u',
           'v', 'w ', 'x', 'y ', 'z ', 'A', 'B', ' C', ' D ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []


for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)


random.shuffle(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")