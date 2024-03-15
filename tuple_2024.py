#Кортеж - tuple, послідовність елементів, які не можна змінювати
igor = ("Igor", 23)
print(igor)

igor = "Igor", 23, 45
print(igor)

#tuple() - створення кортежу з іншої структури
my_list = ['Tetiana', 33, 'Ukraine', 'Cybernetics']
tetiana = tuple(my_list)
print(tetiana)

print(len(tetiana))

#Звернення до елементів кортежу здійснюється за їхнім індексом
print(tetiana[0])
print(tetiana[1])
print(tetiana[2])
print(tetiana[-1])
# print(tetiana[5])

print(tetiana[1:3])

name, age, country, company = tetiana
print(name)
print(age)
print(country)
print(company)

for item in tetiana:
    print(item)

def get_user_data():
    name = 'Iryna'
    age = '33'
    company = 'Ukraine'
    return name, age, company

user = get_user_data()
print(user)

def print_information(name, age, company):
    print(f'Name {name} age {age} company {company}')

print_information('Tetiana', 19, 'Microsoft')
tetiana = ('Tetiana', 19, 'Microsoft')
print_information(*tetiana)

#Перевірка наявності значення в кортежі
if 'name' in tetiana:
    print('Елемент присутній')

tetiana[0] = 'Iryna'
