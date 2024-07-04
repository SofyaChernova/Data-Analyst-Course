users_dict = {'mvolkova': {'name': 'Masha',
                           'surname': 'Volkova',
                           'age': 25,
                           'salary': 60000,
                           'position': 'junior'}}

# В уже созданный список добавляем остальных аналитиков
users_dict['pvoronov'] = {'name': 'Peter',
                          'surname': 'Voronov',
                          'age': 27,
                          'salary': 100000,
                          'position': 'junior'}

users_dict['pparker'] = {'name': 'Peter',
                         'surname': 'Parker',
                         'age': 35,
                         'salary': 150000,
                         'position': 'middle'}

users_dict['akarpov'] = {'name': 'Anatoly',
                         'surname': 'Karpov',
                         'age': 30, 
                         'salary': 250000,
                         'position': 'senior'}

print(users_dict['mvolkova']['name'] + ' ' + str(users_dict['mvolkova']['age']))

