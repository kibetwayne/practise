
import random
letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(4, 10)
print(f'you will have {nr_letters} letters in your password')
nr_symbols = random.randint(2, 10)
print(f'you will have {nr_symbols} symbols in your password')
nr_numbers = random.randint(2, 10)
print(f'you will have {nr_numbers} numbers in your password')

pass_word = []
for i in range(nr_numbers):
    pass_word += random.choice(numbers)

for i in range(nr_letters):
    pass_word += random.choice(letters)

for i in range(nr_symbols):
    pass_word += random.choice(symbols)

random.shuffle(pass_word)

print(f"here is your password: {''.join(pass_word)}")

