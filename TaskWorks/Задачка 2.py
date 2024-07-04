'''https://pydocs.ru/python-zadachi-dlya-nachinayushhih/?ysclid=lujjqh1jws533229496
'''
# ЗАДАЧА 2.
'''Напишите программу, которая использует цикл, для первых 10 чисел. 
В каждом цикле, ваша задача заключается в том, что бы вывести сумму,
предыдущего и текущего числа.
'''
N = int(input("Введите размер списка: "))
# Для формирования списка нужного размера можно использовать функцию range
array = list(range(0, N))
print(array)
number = 0
for i in array:
    print('Текущее Число ', 
          str(i),
          'Предыдущее число ',
          str(number),
          'Сумма ',
          str(i + number)
           )
    number = i
'''num = 0
for i in range(0,11):
    x_sum = num + i
    num = i
    print(f'Текущее число {i}, предыдущее число {num}, сумма чисел {x_sum}')'''