
# ЗАДАЧА 1.
''' Верните результат умножения если, сумма равна 
или больше 1000, в противном случае верните значение суммы двух чисел.
'''
a = int(input())
b = int(input())
if (a + b) >= 1000:
    print('c = ' + str(a * b))
else:
    print('c = ' + str(a + b))

'''
# ЗАДАЧА 2.
Напишите программу, которая использует цикл, для первых 10 чисел. 
В каждом цикле, ваша задача заключается в том, что бы вывести сумму,
предыдущего и текущего числа.

N = int(input("Введите размер списка: "))
# Для формирования списка нужного размера можно использовать функцию range
massiv = list(range(0, N))
print(massiv)
for i in massiv:
    print('Текущее Число ', 
          str(a = massiv[i]),
          'Предыдущее число ',
          str(b = massiv[i] - 1),
          'Сумма '
           )
'''