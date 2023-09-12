def is_valid_password(password):
    # Split the password into three parts using ':' as the delimiter
    # Разделяем пароль на три части, используя ':' в качестве разделителя
    s = password.split(':')
    
    # Check if there are exactly three parts
    # Проверяем, что имеется ровно три части
    if len(s) != 3:
        return False
    
    # Extract the three parts
    # Извлекаем три части
    a, b, c = s[0], s[1], s[2]
    
    # Initialize flags for each condition
    # Инициализируем флаги для каждого условия
    flag1, flag2, flag3 = False, False, False
    
    # Condition 1: Check if the first part 'a' is a palindrome (reads the same forwards and backwards)
    # Условие 1: Проверяем, что первая часть 'a' является палиндромом (читается одинаково слева направо и справа налево)
    if a == a[::-1]:
        flag1 = True
    
    # Condition 2: Check if the second part 'b' is a prime number
    # Условие 2: Проверяем, что вторая часть 'b' - простое число
    for i in range(2, int(b)):
        if int(b) % i == 0:
            return False  # 'b' is not a prime number, so the password is invalid
                          # 'b' не является простым числом, поэтому пароль недействителен
    flag2 = True          
    
    # Condition 3: Check if the third part 'c' is an even number
    # Условие 3: Проверяем, что третья часть 'c' - четное число
    if int(c) % 2 == 0:
        flag3 = True
    
    # The password is considered valid if all three conditions are met
    # Пароль считается действительным, если выполняются все три условия
    return flag1 and flag2 and flag3

# Prompt the user for inputting the password
# Ввод пароля от пользователя
psw = input("Введите пароль в формате 'a:b:c': ")

# Check if the password is valid and display the result
# Проверяем, является ли пароль действительным, и выводим результат
print(is_valid_password(psw))