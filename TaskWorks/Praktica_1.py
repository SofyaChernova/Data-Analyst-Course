# -*- coding: utf-8 -*-

#Задача 1
#Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)


#Задача 2
#Даны списки:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13]

#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# Можно воспользоваться функцией filter()
resalt = list(filter(lambda i: i in a, b))
print(resalt)
# А можно привести оба списка в множества и найти их пересечение
resalt = list(set(a)&set(b))
print(resalt)
'''однако в таком случае каждый элемент встретится 
в результирующем списке лишь один раз, так как множество
поддерживает уникальность входящий в него элементов.
Решение с фильтрацией оставит все дубли на своих местах'''


#Задача 3
#Отсортируйте словарь по значению в порядке возрастания и убывания.
   # Импортируем нужный модуль и объявляем словарь:
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Сортируем в порядке возрастания:
resalt = dict(sorted(d.items(), key = operator.itemgetter(1)))

Ks = input()
print('Ks = ', Ks)


worker = {'Sonya', 'Chernova', 5}
user_name = worker[0]
user_family = worker[1]
position = ['junior', 'middle', 'senior']
if worker[3] < 2:
    current_position = position[0]
elif worker[3] > 2 and worker[3] <= 5:
    current_position = position[1]
else:
    current_position = position[2]

status = f"{user_name} {user_family} is {current_position}"


user_name = worker[0]
user_family = worker[1]
position = worker[3]
if position < 2:
    position = 'junior'
elif position > 2 and position <= 5:
    position = 'middle'
else:
    position = 'senior'

status = f"{user_name} {user_family} is {position}"


values = [10, 5, 3, 100]
tens = [num for num in values if num % 10 == 0]
tens = [10, 0, 5]
for i in values:
    if i % 10 == 0:
        tens.append(i)

'''
values = [12, 134, 10, 47, 100, 20, 50, 160, 210]
tens = []
for i in  values:
    if i % 10 == 0:
       tens.append(i)
print(tens)
'''

workers = []
for human in workers:
    name = human[0]
    family = human[1]
    experience = human[3]
    if experience < 2:
        position = 'junior'
    elif experience >= 2 and experience <=5:
        position = 'middle'
    else:
        position = 'senior'

print(f'{name} {family} is {position}')
