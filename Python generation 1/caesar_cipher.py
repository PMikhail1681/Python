# Alphabets for Russian and English languages
# Алфавиты для русского и английского языков
ru = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
    'ы', 'ь', 'э', 'ю', 'я'
]

en = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

while True:
    # Welcome message and user's choice of action
    # Приветственное сообщение и выбор действия пользователя
    print('Welcome to the Caesar Cipher program!')

    # Prompt to choose an action: encryption or decryption
    # Запрос на выбор действия: шифрование или дешифрование
    direction = input('Choose what you need. (encryption/decryption): ')

    # Prompt to choose the alphabet language: Russian or English
    # Запрос на выбор языка алфавита: русский или английский
    language = input('Choose the alphabet language. (Russian/English): ')
    
    # Prompt for entering the shift value (key)
    # Запрос на ввод значения сдвига (ключа)
    step = int(input('Enter the shift value: '))

    # Prompt for entering the text to process
    # Запрос на ввод текста для обработки
    text = input('Enter the text to process: ')
    
    # Function for encrypting text
    # Функция для шифрования текста
    def encrypt(text, step, alphabet):
        encrypted_text = ""
        for char in text:
            if char.lower() in alphabet:
                char_index = alphabet.index(char.lower())
                encrypted_index = (char_index + step) % len(alphabet)
                encrypted_char = alphabet[encrypted_index]
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    # Function for decrypting text
    # Функция для дешифрования текста
    def decrypt(text, step, alphabet):
        decrypted_text = ""
        for char in text:
            if char.lower() in alphabet:
                char_index = alphabet.index(char.lower())
                decrypted_index = (char_index - step) % len(alphabet)
                decrypted_char = alphabet[decrypted_index]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

    # Depending on the user's choice, perform encryption or decryption in the selected language
    # В зависимости от выбора пользователя выполняем шифрование или дешифрование на выбранном языке
    if direction == 'encryption' and language == 'Russian':
        encryption = encrypt(text, step, ru)
        print("Encrypted text:", encryption)
    elif direction == 'encryption' and language == 'English':
        encryption = encrypt(text, step, en)
        print("Encrypted text:", encryption)
    elif direction == 'decryption' and language == 'Russian':
        decryption = decrypt(text, step, ru)
        print("Decrypted text:", decryption)
    elif direction == 'decryption' and language == 'English':
        decryption = decrypt(text, step, en)
        print("Decrypted text:", decryption)
    else:
        print('Please enter valid data.')

    # Prompt to continue the program
    # Запрос на продолжение работы программы
    answer = input('Continue? (yes/no)')

    if answer.lower() == 'no':
        print('Goodbye! See you again!')
        break   # Exit from the loop, program termination
                # Выход из цикла, завершение программы