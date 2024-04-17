# i = 1
# while i < 101:
#   print(i)
#   i += 1

# i = 0
# while i < 101:
#   i += 1
#   if i == 51:
#     break
#   print(i)









# numbers = [5, 12, 8, 3, 15, 7, 10]

# # Инициализация переменной для максимального элемента
# max_number = numbers[0]

# # Цикл for для поиска максимального элемента
# for num in numbers:
#     if num > max_number:
#         max_number = num

# # Вывод результата
# print(f"Максимальный элемент в списке: {max_number}")


"aeiou"



# # Ввод слова от пользователя
# word = input("Введите слово: ")

# # Инициализация переменной для подсчета гласных
# count_vowels = 0

# # Цикл for для подсчета гласных
# for char in word:
#     if char.lower() in "aeiou":
#         count_vowels += 1

# # Вывод результата
# print(f"Количество гласных в слове '{word}': {count_vowels}")





# word = input("Введите слово: ")

# # Инициализация переменной для подсчета гласных
# count_vowels = 0
# index = 0

# # Цикл while для подсчета гласных
# while index < len(word):
#     if word[index].lower() in "aeiou":
#         count_vowels += 1
#     index += 1

# # Вывод результата
# print(f"Количество гласных в слове '{word}': {count_vowels}")










# Инициализация переменной для суммы четных чисел
# sum_even_numbers = 0

# # Цикл for для вывода четных чисел и подсчета их суммы
# for i in range(2, 21, 2):
#     print(i)
#     sum_even_numbers += i

# # Вывод суммы четных чисел
# print(f"Сумма четных чисел: {sum_even_numbers}")











# counter = 2
# sum_even_numbers = 0

# while counter <= 20:
#     print(counter)
#     sum_even_numbers += counter
#     counter += 2  

# print(f"Сумма четных чисел: {sum_even_numbers}")





# import random

# # Генерация случайного числа от 1 до 10
# secret_number = random.randint(1, 10)

# # Инициализация переменных
# guessed = False

# # Цикл while для угадывания числа
# while not guessed:
#     # Ввод числа от пользователя
#     guess = int(input("Угадайте число от 1 до 10: "))

#     # Проверка на угадывание
#     if guess == secret_number:
#         guessed = True
#         print("Поздравляем! Вы угадали число.")
#     else:
#         print("Попробуйте еще раз.")





# for i in range(1,11):
#     print(i)


# i = 1
# while i < 10:
#     i += 1
#     print(i)



# N = int(input("Введите число N: "))

# # Выводим таблицу умножения для заданного числа
# print(f"Таблица умножения для {N}:")
# for i in range(1, 11):
#     result = N * i
#     print(f"{i} x {N} = {result}")






# san = int(input('Введите чилсо:  '))
# for i in range(san):
#     print('*' *10)






# sib = int(input('ВВедите чилсо:  '))
# for i in range(1, 11):
#     print(f'{i}. {sib}')





# sin = int(input('ВВедите чилсо:  '))
# for i in range(sin):
#     print('Квадрат чилса  ' + str(i) + '  Равен  '+str(i**2))



# sib = int(input('Введите чилсо:  '))
# for i in range(5, 0,-1):
#     print('i' *i)




# sib = int(input('ВВедите чилсо:  '))
# dog =int(input('ВВедите чилсо:  '))
# for i in range(sib, dog, -2):
#     print(i)







# for i in range(1,10):
#     for j in range(1,10):
#         print("%4d" % (i*j), end="")
#     print()




# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# for num in range(1, 11):
#     result = factorial(num)
#     print(f"Факториал числа {num} равен: {result}")



# a = '246'
# print(a.title())




