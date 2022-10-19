from curses.ascii import isdigit

import string
import secrets
import random


def get_number_letters():
    print("Welcome to the PyPassword Generator!\n")
    while True:
        letters = input("How many letters would you like in your password?")
        if letters.isdigit():
            num_letters = int(letters)
            return num_letters
        print("Please introduce only numbers.")


# get_number_letters()

def get_number_symbols():
    while True:
        symbols = input("How many symbols would you like in your password?")
        if symbols.isdigit():
            num_symbols = int(symbols)
            return num_symbols
        print("Please introduce only numbers.")


# get_number_symbols()


def get_numbers():
    while True:
        numbers = input("How many numbers would you like in your password?")
        if numbers.isdigit():
            num_numbers = int(numbers)
            return num_numbers
        print("Please introduce only numbers.")


def get_password():
    num_letters = get_number_letters()
    num_symbols = get_number_symbols()
    num_numbers = get_numbers()

    password_list = ([random.choice(string.ascii_letters) for i in range(num_letters)] +
                     [random.choice(string.punctuation) for i in range(num_symbols)] + 
                     [random.choice(string.digits) for i in range(num_numbers)])
    
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"La contraseña es la siguiente: {password}")



get_password()
