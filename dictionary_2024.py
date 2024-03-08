# словник1 = {ключ1: значення1, ключ2: значення2}
users = {1: 'Igor', 2: 'Tetiana'}
users = {'igor@chnu.edu.ua': 'Igor'}

#Створення порожнього словника
users = {}
object = dict()

#Перетворення списку та кортежу в словник
users_list = [
    ['+3805554334', 'Tom'],
    ['+3805554322', 'Bill'],
    ['+3805554311', 'Bob'],
]
users_dict = dict(users_list)
print(users_dict)

#Звертання до елементів словника
users = {'igor@chnu.edu.ua': 'Igor',
         'tetiana@chnu.edu.ua': 'Tetiana',
         'kateryna@chnu.edu.ua': 'Kateryna'}
print(users['igor@chnu.edu.ua'])
users['bob@chnu.edu.ua'] = 'Bob'
print(users['bob@chnu.edu.ua'])

if 'george@chnu.edu.ua' in users:
    print(users['george@chnu.edu.ua'])
else:
    print('Елемент не знайдено')

print(users.get('george@chnu.edu.ua')) #повертає None, якщо елемент відсутній
print(users.get('george@chnu.edu.ua', 'Елемент не знайдено')) #повертає Елемент не знайдено

#Видалення елементів зі словника
del users['igor@chnu.edu.ua']
print(users)

#Метод pop
user = users.pop('bob@chnu.edu.ua')
print(user)
print(users)

#Очистка словника
# users.clear()

#Копіювання словника
students = users.copy()

users_2 = {'igor3@chnu.edu.ua': 'Igor',
         'tetiana2@chnu.edu.ua': 'Tetiana',
         'kateryna4@chnu.edu.ua': 'Kateryna'}

users.update(users_2)
print(users)

users['igor3@chnu.edu.ua'] = "Chernivtsi"
print(users)

#Перебір елементів словника
for key in users:
    print(f'User {key} User value {users[key]}')

for login, user_name in users.items():
    print(f'User {login} User value {user_name}')

for key in users.keys():
    print(key)

for value in users.values():
    print(value)

#Використання комплексних словників
users = {
    'Igor':
        {'phone': '+378473993',
         'email': 'igor@chnu.edu.ua'},
    'Tetiana':
        {'phone': '+378473993',
         'email': 'igor@chnu.edu.ua',
         'mobile': '+3472834001'}
}
print(users['Tetiana']['mobile'])

for user, user_info in users.items():
    print(f'User {user}')
    for info_element, info_value in user_info.items():
        print(f'{info_element} - {info_value}')
