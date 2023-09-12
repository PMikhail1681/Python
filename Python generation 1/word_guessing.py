import random

# List of words to choose from
# Список слов для выбора
word_list = ['year', 'person', 'time', 'thing', 'life', 'day', 'hand', 'time', 'work', 'word', 'place', 'face',
            'friend', 'eye', 'question', 'home', 'side', 'country', 'world', 'case', 'head', 'child', 'power', 'end',
            'view', 'system', 'part', 'city', 'relationship', 'woman', 'money', 'earth', 'car', 'water', 'father',
            'problem', 'hour', 'right', 'leg', 'decision', 'door', 'image', 'history', 'authority', 'law', 'war',
            'god', 'voice', 'thousand', 'book', 'possibility', 'result', 'night', 'table', 'name', 'area', 'article',
            'number', 'company', 'people', 'wife', 'group', 'development', 'process', 'court', 'condition', 'means',
            'beginning', 'light', 'time', 'path', 'soul', 'level', 'form', 'connection', 'minute', 'street', 'evening',
            'quality', 'thought', 'road', 'mother', 'action', 'month', 'state', 'language', 'love', 'look', 'mother',
            'century', 'school', 'goal', 'society', 'activity', 'organization', 'president', 'room', 'order', 'moment',
            'theatre', 'letter', 'morning', 'help', 'situation', 'role', 'ruble', 'meaning', 'state', 'apartment',
            'organ', 'attention', 'body', 'work', 'son', 'measure', 'death', 'market', 'program', 'task', 'enterprise',
            'window', 'conversation', 'government', 'family', 'production', 'information', 'position', 'center', 'answer',
            'husband', 'author', 'wall', 'interest', 'federation', 'rule', 'management', 'man', 'idea', 'party', 'council',
            'account', 'heart', 'movement', 'thing', 'material', 'week', 'feeling', 'head', 'science', 'row', 'newspaper',
            'cause', 'shoulder', 'price', 'plan', 'speech', 'point', 'basis', 'comrade', 'culture', 'data', 'opinion',
            'document', 'institute', 'course', 'project', 'meeting', 'director', 'term', 'finger', 'experience', 'service',
            'fate', 'girl', 'queue', 'forest', 'composition', 'member', 'quantity', 'event', 'object', 'hall', 'creation',
            'meaning', 'period', 'step', 'brother', 'art', 'structure', 'number', 'example', 'research', 'citizen', 'game',
            'chief', 'growth', 'theme', 'principle', 'method', 'type', 'film', 'edge', 'guest', 'air', 'character', 'struggle',
            'use', 'size', 'education', 'boy', 'blood', 'region', 'sky', 'army', 'class', 'representative', 'participation',
            'girl', 'politics']

# Function to get a random word from the word list
# Функция для получения случайного слова из списка
def get_word():
    word = random.choice(word_list).upper()
    return word

# Function to display the hangman based on the number of tries left
# Функция для отображения виселицы в зависимости от количества попыток
def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

# Function to play the word guessing game
# Функция для игры в игру "Угадай слово"
def play(word):
   while True:
      word_completion = ['_' for _ in word]  # Create a list of underscores to represent the word
                                             # Создаем список подчеркиваний для представления слова
                                             
      guessed = False                        # Flag to check if the word is guessed
                                             # Флаг для проверки, угадано ли слово
                                       
      guessed_letters = []                   # List to store guessed letters
                                             # Список для хранения угаданных букв
                                             
      guessed_words = []                     # List to store guessed words
                                             # Список для хранения угаданных слов
                                             
      tries = 6                              # Number of tries allowed
                                             # Количество попыток
                                             
      print('Let\'s play a word guessing game!')
      print(display_hangman(tries))          # Display the initial hangman status
                                             # Выводим начальное состояние виселицы
                                             
      print(word_completion)                 # Display the word as underscores
                                             # Выводим слово как подчеркивания
                                             
      while tries < 6:
         symbol_input = input('Enter a letter or word:').upper()
         
         # Check if the input is a valid letter or word
         # Проверка на валидность ввода (буква или слово)
         if not symbol_input.isalpha():
            print('You can only enter a letter or word:')
            continue
         if symbol_input == word:
            print('Congratulations, you guessed the word!')
            break
         else:
            guessed_words.append(symbol_input)
            tries -= 1
            print(f'Incorrect! You have {tries} attempts left')
            if tries == 0:
               print('Unfortunately, you have no more attempts left.')
               break
         if symbol_input in guessed_letters or symbol_input in guessed_words:
            print('You\'re repeating yourself, it was already guessed!')  
            continue
         if symbol_input not in word:
            print('There is no such letter, try again. You have {tries} attempts left.')   
         if symbol_input in word:
            guessed_letters.append(symbol_input)
            tries -= 1
            
          # Update word_completion with correctly guessed letters
          # Обновляем word_completion с правильно угаданными буквами
         for i in range(len(word)):
            if word[i] == symbol_input:
               word_completion[i] = symbol_input 
               
               # Check if the word is completely guessed
               # Проверяем, угадано ли слово полностью
               if ''.join(word_completion).upper() == word:
                  print('Congratulations, you guessed the word!')
                  break

      att = input('Do you want to play again? yes/no').lower()
      if att == 'no':
         print('See you again!')
         break
      else:
         continue

# Get a random word and start the game
# Получаем случайное слово и начинаем игру
word = get_word()
play(word)