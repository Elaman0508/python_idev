# print("Добро пожаловать! Вы хотите посетить магазин или ресторан?")

# choice = input("Введите 'магазин' или 'ресторан': ")

# if choice.lower() == "магазин":
#     print("Вы пошли в магазин. Приятных покупок!") 
    
#     print("Выберите категорию товаров:")
#     print("1. Продукты питания")
#     print("2. Товары для дома")

#     category_choice = input("Введите номер категории: ")

#     if category_choice == "1":
#         print("Вы выбрали продукты питания. Приятных покупок!")
#     elif category_choice == "2":
#         print("Вы выбрали товары для дома. Удачных покупок!")
#     else:
#         print("Извините, но такой категории нет.")

# elif choice.lower() == "ресторан":
#     print("Вы решили посетить ресторан. Приятного аппетита!")
    
#     print("Меню ресторана:")
#     print("1. Завтраки")
#     print("2. Обеды")
#     print("3. Ужины")

#     menu_choice = input("Введите номер блюда: ")

#     if menu_choice == "1":
#         print("Вы заказали завтрак. Приятного аппетита!")
#     elif menu_choice == "2":
#         print("Вы заказали обед. Приятного аппетита!")
#     elif menu_choice == "3":
#         print("Вы заказали ужин. Приятного аппетита!")
#     else:
#         print("Извините, но такого блюда нет.")

# else:
#     print("Извините, но такого варианта нет. Пожалуйста, выберите 'магазин' или 'ресторан'.")


# def
# 1. Пользователден 3 жолу суроо талап кылуу
# 2. Пользователь жазган сандын ичинде масималдуу санды чыгаруу

# 2
# 4
# 6
# a = int(input("1.Введите цумму: "))
# b = int(input("2.Введите вторую сумму: "))
# c = int(input("3.Введите третию цумму: "))

# def num(a,b,c):
#     if a and b < c:
#         print(c)
#     elif c and b < a:
#         print(a)
#     else:
#         print(b)
# num(a,b,c)
    




# while True:
#     print("Простой калькулятор")
#     print("Доступные операции:")
#     print("1. Сложение")
#     print("2. Вычитание")
#     print("3. Умножение")
#     print("4. Деление")
#     print("5. Выход")

#     operation = input("Выберите операцию (1/2/3/4/5): ")
#     if operation == '5':

#         print("Выход из калькулятора.")
#         break

#     if not operation.isdigit() or int(operation) not in range(1, 6):
#         print("Ошибка: Введите число от 1 до 5")
#         continue

#     operation = int(operation)
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))

#     if operation == 1:
#         result = num1 + num2
#         print("Результат сложения:", result)
#     elif operation == 2:
#         result = num1 - num2
#         print("Результат вычитания:", result)
#     elif operation == 3:
#         result = num1 * num2
#         print("Результат умножения:", result)
#     elif operation == 4:
#         if num2 != 0:
#             result = num1 / num2
#             print("Результат деления:", result)
#         else:
#             print("Ошибка: Деление на ноль невозможно")
#     else:
#         print("Ошибка: Неверная операция. Выберите число от 1 до 5")





# login = "islam"
# password = 12345
# a = str(input("Введите логин? "))
# b = int(input("Введите пароль? "))
# if a == login and b == password:
#     print("успешно")
# else:
#     print("Неверный")
















# grade = int(input("Введите Балл: "))

# if grade >= 90:
#      print("5")
# elif 80 <= grade < 90:
#         print("4")
# elif 70 <= grade < 80:
#         print("3")
# elif 60 <= grade < 70:   
#         print("2")
# else:
#         print("Вы не сдали модул")








# login = 'Ernisov Elaman'
# password = 200508
# user = str(input('Введите логин ! '))
# user2 = int(input('Введите пароль'))
# if user == login:
#     print('Доступ открыт')
# elif user2 == password:
#     print(None)
# else:
#     print("Невреный пароль логин")











# num = int(input("Введите число: "))

# if num % 2 == 0:
#     print("Число четное.")
# else:
#     print("Число нечетное.")













# hour = int(input("Введите текущий час (от 0 до 24): "))

# if 5 <= hour < 12:
#     print("Доброе утро!")
# elif 12 <= hour < 18:
#     print("Добрый день!")
# elif 18 <= hour < 24 or 0 <= hour < 5:
#     print("Добрый вечер!")
# else:
#     print("Некорректный ввод времени.")
   







# variable = input("Введите значение: ")

# if variable.isdigit():
#     print("Это целое число.")
# elif variable.replace(".", "").isdigit():
#     print("Это float.")
# elif variable.isalpha():
#     print("Это строка.")
# else:
#     print("Это какой-то другой тип данных.")




# income = float(input("Введите свой доход: "))
# if income <= 10000:
#     tax_rate = 0.1
# elif income <= 50000:
#     tax_rate = 0.2
# else:
#     tax_rate = 0.3
# tax = income * tax_rate
# print(f"Сумма налога: {tax}")







# day_number = int(input("Введите номер дня недели (1-7): "))

# if day_number == 1:
#     print("Понедельник")
# elif day_number == 2:
#     print("Вторник")
# elif day_number == 3:
#     print("Среда")
# elif day_number == 4:
#     print('четверг')
# elif day_number == 5:
#     print('пятница')
# elif day_number == 6:
#     print('суббота')
# elif day_number == 7:
#     print('восскерсения')
# elif day_number == 8:
#     print('salam')
# #и так далее для остальных дней
# else:
#     print("Некорректный номер дня.")








# age = int(input("Введите свой возраст: "))
# if age < 18:
#     print("Вы ребенок или подросток.")
# elif age < 65:
#     print("Вы взрослый.")
# else:
#     print("Вы пожилой человек.")








# a = int(input("Введите длину стороны A: "))
# b = int(input("Введите длину стороны B: "))
# c = int(input("Введите длину стороны C: "))

# if a == b == c:
#     print("Треугольник равносторонний.")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный.")
# else:
#     print("Треугольник разносторонний.")





# year = int(input("Введите год: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Год високосный.")
# else:
#     print("Год не високосный.")





# number = float(input("Введите число: "))
# if number > 0:
#     print("Число положительное.")
# elif number == 0:
#     print("Число равно нулю.")
# else:
#     print("Число отрицательное.")




# x = float(input("Введите x: "))
# y = float(input("Введите y: "))
# if x > 0 and y > 0:
#     print("Точка находится в первом квадранте.")
# elif x < 0 and y > 0:
#     print("Точка наход")




# my_list = [1, 2, 3, 4, 5]
# element = int(input("Введите число: "))
# if element in my_list:
#     print("Элемент найден в списке")
# else:
#     print("Элемент не найден в списке")




#Попросите пользователя ввести два числа и проверьте, какое из них больше.
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# if num1 > num2:
#     print(f"{num1} больше, чем {num2}.")
# elif num1 < num2:
#     print(f"{num2} больше, чем {num1}.")
# else:
#     print("Числа равны.")







# password = 12345
# login = 'Elaman'
# user = int(input("Введите пароль :  "))
# user1 = str(input('Введите логин ;  '))
# if  user == password:
    #print('Доступ открыт')
# elif  user1 == login:
#     print('Доступ открыт')
# else:
#     print("Доступ закрыт")










# login = 'Ernisov1x'
# password = 12345
# user = str(input('Введите логин! '))
# user2 = int(input('Введите пароль! '))
# if user == login:
#     print('Доступ открыт!')
# elif user2 == password:
#     None
# else:
#     print('Неверны пароль и логин !!!!!')






# old = int(input("Сколько вашему ребёнку?"))
# if -1< old <3:
#     print("Проходите бесплатно")
# elif 3< old <8:
#         print("100 сом")
# elif 8< old <18:
#       print("200 сом")
# else:
#       print("500 сом")








# name = "Kurmash"
# password = "1310954602050403"
# use = str(input("Введите логин:"))
# use2 = int(input("Введите пароль:"))
# if use == name:
#     print("Добро Пожаловать")
#     if use  name:
#         print("Неправильный ввод логина")
# elif use == name:
#     print(f"{use} Неправильный ввод пароли")
# elif use2 == password:
#     print("Добро пожаловать")
#     None
# else:
#     None




# def check_credentials(name, password):
#  password = int(input("Введите пароль"))
# name = str(input("Введите логин"))
# if name == name and password == password:
#         return True
# elif name != name and password != password:
#   print("Неверный логин и пароль.") 
#         return False
# elif name != name:
#         print("Неверный логин.")
#         return False
# elif password != password:
#         print("Неверный пароль.")
#         return False
# else:
#        print("")




# def check_credentials(username, password):
#     valid_username = "kuma"
#     valid_password = "12345"

#     if username == valid_username and password == valid_password:
#         return True
#     elif username != valid_username and password != valid_password:
#         print("Неверный логин и пароль.")
#         return False
#     elif username != valid_username:
#         print("Неверный логин.")
#         return False
#     elif password != valid_password:
#         print("Неверный пароль.")
#         return False

# # Пример использования:
# login_input = input("Введите логин: ")
# password_input = input("Введите пароль: ")

# if check_credentials(login_input, password_input):
#     print("Вход выполнен успешно!")
# else:
#     print("Вход не выполнен. Пожалуйста, проверьте логин и пароль.")








# Получение даты рождения от пользователя
# день = int(input("Введите день рождения: "))
# месяц = int(input("Введите месяц рождения: "))


# if месяц < 1 or месяц > 12:
#     print("Ошибка: Некорректный месяц.")
# elif (месяц == 2 and (день < 1 or день > 29)) or \
#         ((месяц == 4 or месяц == 6 or месяц == 9 or месяц == 11) and (день < 1 or день > 30)) or \
#         ((месяц == 1 or месяц == 3 or месяц == 5 or месяц == 7 or месяц == 8 or месяц == 10 or месяц == 12) and (день < 1 or день > 31)):
#     print("Ошибка: Некорректный день.")
# else:
    
#     if (месяц == 3 and 21 <= день <= 31) or (месяц == 4 and 1 <= день <= 19):
#         знак_зодиака = "Овен"
#     elif (месяц == 4 and 20 <= день <= 30) or (месяц == 5 and 1 <= день <= 20):
#         знак_зодиака = "Телец"
#     elif (месяц == 5 and 21 <= день <= 31) or (месяц == 6 and 1 <= день <= 20):
#         знак_зодиака = "Близнецы"
#     elif (месяц == 6 and 21 <= день <= 30) or (месяц == 7 and 1 <= день <= 22):
#         знак_зодиака = "Рак"
#     elif (месяц == 7 and 23 <= день <= 31) or (месяц == 8 and 1 <= день <= 22):
#         знак_зодиака = "Лев"
#     elif (месяц == 8 and 23 <= день <= 31) or (месяц == 9 and 1 <= день <= 22):
#         знак_зодиака = "Дева"
#     elif (месяц == 9 and 23 <= день <= 30) or (месяц == 10 and 1 <= день <= 22):
#         знак_зодиака = "Весы"
#     elif (месяц == 10 and 23 <= день <= 31) or (месяц == 11 and 1 <= день <= 21):
#         знак_зодиака = "Скорпион"
#     elif (месяц == 11 and 22 <= день <= 30) or (месяц == 12 and 1 <= день <= 21):
#         знак_зодиака = "Стрелец"
#     elif (месяц == 12 and 22 <= день <= 31) or (месяц == 1 and 1 <= день <= 19):
#         знак_зодиака = "Козерог"
#     elif (месяц == 1 and 20 <= день <= 31) or (месяц == 2 and 1 <= день <= 18):
#         знак_зодиака = "Водолей"
#     else:
#         знак_зодиака = "Рыбы"

#     print("Ваш знак зодиака:", знак_зодиака)



# import random

# secret_number = random.randint(1, 100)  # Генерация случайного числа от 1 до 100
# attempts = 0

# print("Привет! Давай поиграем в угадай число.")
# print("Я загадал число от 1 до 100. Попробуй угадать!")

# while True:
#     user_guess = int(input("Твоё предположение: "))
#     attempts += 1
#     if user_guess == secret_number:
#         print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
#         break
#     elif user_guess < secret_number:
#         print("Попробуй ввести большее число.")
#     else:
#         print("Попробуй ввести меньшее число.")




# a = 'ela'
# s = 123

# l = str(input('wertyui'))
# p = int(input('dfgh'))

# if a == l and p == s:
#     print(True)
# else:
#     print(False)








