names = 'Name1 Surname1, Name2 Surname2'
names_list = names.split(',')
print(names)
print(names_list)

name_parts = names.split(',')
names_list = [name.strip() for name in name_parts]
print(names_list)
'''
Она используется для возврата копии исходной строки путем удаления начальных и 
конечных пробелов, символов, переданных в функцию strip().
если программист не передает какой-либо параметр функции strip(), она удаляет начальные и конечные пробелы из строк.

'''