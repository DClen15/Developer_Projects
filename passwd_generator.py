# Making a basic password generator
import random

print('This program will generate a secure password for you.')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Collect user input for desired number of letters, numbers and symbols
nr_letters = int(input('Enter the number of letters you would like in the password: \n'))
nr_numbers = int(input('Enter the number of numbers you would like in the password: \n'))
nr_symbols = int(input('Enter the number of symbols you would like in the password: \n'))
# Create an empty list as a place holder
tracker = []
# iterates through the total number of letters user inputs and grabs a random element from the letters list
# same thing for numbers and symbols below
for i in range(1, nr_letters + 1):
  rand_letter = random.choice(letters)
  tracker.append(rand_letter)

for i in range(1, nr_numbers + 1):
  rand_num = random.choice(numbers)
  tracker.append(rand_num)

for i in range(1, nr_symbols + 1):
  rand_sym = random.choice(symbols)
  tracker.append(rand_sym)
# Takes the random list of letters, numbers, and symbols and randomizes their order
random.shuffle(tracker)
# Joins each item of the tracker list into a string called password
password = ''.join(tracker)

print(f'Your new password is: {password}')


