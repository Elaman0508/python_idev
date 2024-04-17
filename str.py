""" Строковые типы (str):

Последовательность символов внутри кавычек (одинарных или двойных).
Примеры:
"""
s1 = "Привет, мир!"
s2 = 'Python'


# upper(): Преобразует все символы строки в верхний регистр.

text = "Привет, мир!"
upper_text = text.upper()  # upper_text = "ПРИВЕТ, МИР!"
print(upper_text)

# lower(): Преобразует все символы строки в нижний регистр.

message = "Python"
lower_message = message.lower()  # lower_message = "python"


# count(): Возвращает количество вхождений подстроки в строке.

sentence = "Python - прекрасный язык программирования, Python!"
count_python = sentence.count("Python")  # count_python = 2


# replace(): Заменяет все вхождения одной подстроки на другую.

phrase = "Я люблю Python"
updated_phrase = phrase.replace("Python", "программирование")  # updated_phrase = "Я люблю программирование"


#Получение подстроки с определенным диапазоном индексов.

text = "Python Programming"
substring = text[0:6]  # substring = 'Python'


#Обращение строки.

word = "hello"
reversed_word = word[::-1]  # reversed_word = 'olleh'





""" Задача: Удаление символа

1. Напишите  программу, которая принимает строку от пользователя и удаляет первый символ. Выведите результат.
Задача: Добавление символа

2. Напишите программу, которая принимает строку и добавляет к ней символ "!" в конец. Выведите результат.
Задача: Срез строки

3. Напишите программу, которая принимает строку и выводит ее первые три символа.
Задача: Объединение строк

4. Создайте две строки и объедините их в одну. Выведите результат.
Задача: Замена символа

5. Напишите программу , которая принимает строку и заменяет все пробелы на символ "_". Выведите результат.
 
"""







#Ответы

1
user_input = input("Введите строку: ")
result_string = user_input[1:]
print("Результат:", result_string)


2
user_input = input("Введите строку: ")
result_string = user_input + "!"
print("Результат:", result_string)


3
user_input = input("Введите строку: ")
result_string = user_input[:3]
print("Результат:", result_string)


4
str1 = "Hello"
str2 = "World"
result_string = str1 + str2
print("Результат:", result_string)


5
user_input = input("Введите строку: ")
result_string = user_input.replace(" ", "_")
print("Результат:", result_string)









""" Задача: Обратная строка   lvl : 'HARD'

1. Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
Задача: Подсчет гласных

2. Напишите программу, которая считает количество гласных букв в заданной строке. Гласными считайте только буквы (a, e, i, o, u).
Задача: Палиндром

3. Напишите программу, которая проверяет, является ли заданная строка палиндромом (читается одинаково слева направо и справа налево).
Задача: Замена подстроки

4. Напишите программу, которая принимает строку и заменяет в ней все вхождения подстроки "Python" на "Java".
Задача: Счетчик слов

5. Напишите программу, которая принимает текст от пользователя и подсчитывает количество слов в тексте.
"""




#Ответы на эти задание
'1'
user_input = input("Введите строку: ")
reversed_string = user_input[::-1]
print("Обратная строка:", reversed_string)


'2'
user_input = input("Введите строку: ")
vowels_count = sum(1 for char in user_input if char.lower() in 'aeiou')
print("Количество гласных:", vowels_count)


'3'
user_input = input("Введите строку: ")
is_palindrome = user_input.lower() == user_input[::-1].lower()
print("Является ли строка палиндромом:", is_palindrome)


'4'
user_input = input("Введите строку: ")
modified_string = user_input.replace("Python", "Java")
print("Модифицированная строка:", modified_string)



'5'
user_input = input("Введите текст: ")
words_count = len(user_input.split())
print("Количество слов в тексте:", words_count)


# def mirror_string(input_str):
#     # Используем срезы для создания зеркальной строки
#     mirrored_str = input_str[::-1]
#     return mirrored_str

# # Получаем ввод от пользователя
# user_input = input("Введите строку: ")

# # Получаем зеркальное представление строки
# mirrored_input = mirror_string(user_input)




