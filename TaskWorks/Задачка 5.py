# ЗАДАЧА 5. Совпадает ли первый и последний номер в списке?
'''
Напишите функцию, которая возвращает True, если первый и последний номер в списке совпадает
В случае, если не совпадает, верните значение False. К примеру:
list1 = [10,20,30,40,50,10]
list2 = [10,20,30,40,50,60]
#Ожидаемый результат
List1 - True
List2 - False
'''

def commparator(arr):
    if arr[0] == arr[-1]:
        return True
    return False
        
list1 = [10,20,30,40,50,10]
list2 = [10,20,30,40,50,60]
#print(commparator(list1))
#print(commparator(list2))

arr = [list1, list2]
print(arr)
for i in arr:
    print(commparator(i))
