import random

# Define character sets
# Определение наборов символов
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symbol = 'il1Lo0O'

chars = ''

# Ask the user for password generation criteria
# Запрос у пользователя критериев генерации пароля
quantity = int(input('How many passwords do you want to generate? '))
length = int(input('What should be the length of each password? '))
dig1 = input(f'Should the password contain digits {digits}? (yes/no) ')
let1 = input(f'Should the password contain lowercase letters {lowercase_letters}? (yes/no) ')
let2 = input(f'Should the password contain uppercase letters {uppercase_letters}? (yes/no) ')
pun1 = input(f'Should the password contain punctuation symbols {punctuation}? (yes/no) ')
sym = input(f'Should ambiguous characters {symbol} be excluded? (yes/no) ')

# Build the character set based on user choices
# Создание набора символов на основе выбора пользователя
if dig1.lower() == 'yes':
    chars += digits
if let1.lower() == 'yes':
    chars += lowercase_letters
if let2.lower() == 'yes':
    chars += uppercase_letters
if pun1.lower() == 'yes':
    chars += punctuation
if sym.lower() == 'yes':
    for i in range(len(symbol)):
        chars = chars.replace(symbol[i], '')

# Generate and print passwords
# Генерация и вывод паролей
for j in range(quantity):
    password = ''.join(random.sample(chars, length))
    print(password, sep='\n')
    password = ''.join(random.sample(chars, length))
    print(password, sep = '\n')      