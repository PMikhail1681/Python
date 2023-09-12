from random import randint

# Welcome message to the Guess the Number game, bro!
# Приветствие пользователя в игре "Угадай число, бро!"
print('Welcome to guessing numbers bro!')

# Set the range for generating a random number
# Задаем диапазон для генерации случайного числа
x = int(input('From one to what number will we guess'))

# Check for the correctness of the entered data
# Проверка на корректность введенных данных
def is_invalid(n):  
    return n.isdigit() and int(n) in range(1, x+1)

# Main game function
# Основная функция игры
def game():
    counter = 0
    num = randint(1, x)
    
    # Main game loop
    # Основной цикл игры
    while True:
        n = input(f'Try to guess the number from one to {x}')

        # Check the validity of the entered data
        # Проверка валидности введенных данных
        if not is_invalid(n):
            print(f'Maybe we can still enter an integer from one to {x} bro?')
        else:
            counter += 1
            n = int(n)

            # Compare the entered number with the hidden one
            # Сравниваем введенное число с загаданным
            if n > num:
                print('Your number is bigger than the one you have guessed, try again')
            if n < num:
                print('Your number is less than the one you have guessed, try again')
            if n == num:
                print(f'You guessed it in {counter} attempts. Congratulations!')
                break

# Start the game
# Запуск игры
game()

# Check if the player wants to play again
# Проверка на желание играть еще раз
while True:
    print('Will you play again? (yes/no)')
    answer = input().lower()
    if answer == 'yes':
        game()
    elif answer == 'no':
        print('Thanks for playing! See you..')
    else:
        print("Sorry bro. I didn't understand you. Are you playing on?")