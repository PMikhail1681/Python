import random

# List of answers for the Magic 8-Ball
# Список ответов Волшебного шара
answers = [
    'It is certain', 'As I see it, yes', 'It is unclear, try again', "Don't even think about it",
    'It is certain', 'Most likely', 'Ask again later', 'My answer is no',
    'No doubts about it', 'Outlook is good', 'Better not tell you now', 'According to my data, no',
    'Definitely yes', 'Signs point to yes', 'Cannot predict now', 'Outlook not so good',
    'You can be sure of it', 'Yes', 'Concentrate and ask again', 'Very doubtful'
]

# Greeting the user and asking for their name
# Приветствие пользователя и запрос его имени
print('Hello World, I am the Magic 8-Ball, and I have an answer to any of your questions.')
name = input('What is your name? ')
print(f'Hello, {name.capitalize()}!')

while True:
    # Asking the user about their future
    # Запрос пользователя о его будущем
    question = input('What do you want to know about your future? ')
    
    # Printing a random answer from the answers list
    # Вывод случайного ответа из списка answers
    print(random.choice(answers))
    
    # Asking the user if they want to know anything else
    # Запрос пользователя о желании задать еще один вопрос
    question2 = input('Do you want to know anything else? (yes/no) ')
    
    # If the user enters "yes," the loop continues; otherwise, the program terminates
    # Если пользователь ввел "yes", цикл продолжается, иначе программа завершает выполнение
    if question2.lower() == 'yes':
        continue
    elif question2.lower() == 'no':
        print('Come back if you have more questions!')
        break
    else:
        print('I did not understand you.. yes or no?')