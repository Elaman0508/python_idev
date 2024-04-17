# num = int(input('Введите число ! '))
# print(f'Таблица умнодения {num}')

# for i in range(1, 11):
#     result = i * num
#     print(f'{i} x {num} = {result}')


num = int (input('Введите первое число! '))
oper = input('Выберите оператора ')
num2 = int(input('Введите второе число! '))
if oper == '+':
    result = num + num2
    print(f'Результат {num} + {num2} = {result}')