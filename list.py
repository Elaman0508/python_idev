#Тема: Список(list) -- Тизме
"""Список(list) - Бул ирээтелген жана озгоруучу коллекция деп айтсак болот, мындайча айтканда список ар кандай объекттерди озуго камтышы мумкун (анын ичинде ички тизмелер да кирет) же эч нерсе сакталбашы мумкун.
Python тилинде список торт бурчтук каша менен жазылат![]"""

""" Списки (list):

Упорядоченные изменяемые последовательности.
Примеры:"""  

my_list = [1, 2, 3, 'Python', True,[' list']]



    
#Добавление элементов:

#append(): Добавляет элемент в конец списка.

my_list = [1, 2, 3]
my_list.append(4)  # my_list = [1, 2, 3, 4]


#insert(): Вставляет элемент по указанному индексу.

numbers = [1, 2, 3]
numbers.insert(1, 10)  # numbers = [1, 10, 2, 3]


#append(): Добавляет элемент в конец списка.

my_list = [1, 2, 3]
my_list.append(4)  # my_list = [1, 2, 3, 4]


#remove(): Удаляет первое вхождение элемента из списка.

numbers = [1, 2, 3, 2, 4]
numbers.remove(2)  # numbers = [1, 3, 2, 4]


#index(): Возвращает индекс первого вхождения элемента в списке.

fruits = ['яблоко', 'груша', 'апельсин']
index_pear = fruits.index('груша')  # index_pear = 1


#sort(): Сортирует элементы списка.

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # numbers = [1, 1, 2, 3, 4, 5, 9]


#Срезы (Slices):

#Получение подсписка с определенным диапазоном индексов.

my_list = [1, 2, 3, 4, 5]
sublist = my_list[1:4]  # sublist = [2, 3, 4]


#Шаг среза (взятие каждого второго элемента).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_numbers = numbers[1:8:2]  # sliced_numbers = [2, 4, 6, 8]







""" Задача: Удаление элемента

Создайте список чисел. Удалите из него второй элемент. Выведите результат.


Создайте список строк. Добавьте к нему новую строку. Выведите результат.
Задача: Срез списка

Создайте список чисел. Выведите его последние два элемента.
Задача: Объединение списков

Создайте два списка. Объедините их в третий список. Выведите результат.
Задача: Замена элемента

Создайте список строк. Замените вторую строку на новую. Выведите результат.
"""








#Ответы

1
numbers = [1, 2, 3, 4, 5]
print(numbers.pop(1))


2
strings = ["apple", "banana", "cherry"]
strings.append("orange")
print("Результат:", strings)


3
numbers = [10, 20, 30, 40, 50]
result_list = numbers[-2:]
print("Результат:", result_list)


4
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Результат:", combined_list)


5
strings = ["apple", "banana", "cherry"]
strings[1] = "grape"
print("Результат:", strings)












'1'
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Объединенный список:", combined_list)


'2'
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print("Список с уникальными элементами:", unique_list)


'3'
numbers = list(range(1, 11))
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Список без четных чисел:", odd_numbers)


'4'
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = [a + b for a, b in zip(list1, list2)]
print("Список с суммой элементов:", sum_list)


'5'
numbers = [7, 2, 9, 1, 6]
min_value = min(numbers)
max_value = max(numbers)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)



