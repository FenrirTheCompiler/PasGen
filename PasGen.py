#Prompt user for how many letters, numbers, and symbols they want.  
#Output is a password with all elements jumbled in random order.

import random

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols_list = [ "~", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?", ">", "<"]

password = ""
new_password = ""
password_list = []

letters = int(input("How many letters? "))
numbers = int(input("How many numbers? "))
symbols = int(input("How many symbols? "))

#module_name.list_name


while letters > 0:
    random.shuffle(letters_list)
    password = password + letters_list[1]
    letters = letters - 1

while numbers > 0:
    random.shuffle(numbers_list)
    password = password + numbers_list[2]
    numbers = numbers - 1

while symbols > 0:
    random.shuffle(symbols_list)
    password = password + symbols_list[3]
    symbols = symbols - 1

for char in password:
    password_list.append(char)

random.shuffle(password_list)

for char in password_list:
    new_password = new_password + char


print(new_password)
