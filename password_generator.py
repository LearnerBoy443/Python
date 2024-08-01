# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
if nr_letters< 0:
    print("Number of elements cannot be negative.")
elif nr_letters > len(letters):
    print("Number of elements cannot be greater than the length of the list.")
else:
    random_elements = random.sample(letters, nr_letters)
if nr_symbols < 0:
    print("Number of elements cannot be negative.")
elif nr_symbols > len(symbols):
    print("Number of elements cannot be greater than the length of the list.")
else:
    random_elements2 = random.sample(symbols, nr_symbols)
if nr_numbers < 0:
    print("Number of elements cannot be negative.")
elif nr_numbers > len(numbers):
    print("Number of elements cannot be greater than the length of the list.")
else:
    random_elements3 = random.sample(numbers, nr_numbers)
random_pass=random_elements+random_elements2+random_elements3
random.shuffle(random_pass)
print(''.join(random_pass))


