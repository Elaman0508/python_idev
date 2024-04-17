""" Кортежи (tuple):

Упорядоченные неизменяемые последовательности.
Примеры: """

my_tuple = (1, 'apple', 3.14)

#count(): Возвращает количество вхождений элемента в кортеже.

my_tuple = (1, 2, 3, 2, 4)
count_2 = my_tuple.count(2)  # count_2 = 2


#index(): Возвращает индекс первого вхождения элемента в кортеже.

items = ('apple', 'banana', 'apple', 'orange')
index_banana = items.index('banana')  # index_banana = 1


#__len__: Возвращает длину кортежа.

fruits = ('apple', 'banana', 'orange')
length = fruits.len()  # length = 3


#__getitem__: Получение элемента по индексу.

my_tuple = (10, 20, 30)
item = my_tuple.getitem(1)  # item = 20


#__str__: Представление кортежа в виде строки.

# pair = ('key', 'value')
# str_representation = pair.str()  # str_representation = "('key', 'value')"