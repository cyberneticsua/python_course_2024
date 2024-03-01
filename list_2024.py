# list - список []
# tuple - кортежі ()
# dict - словник {}
# set - множина {}

# Оголошення порожнього списку
numbers = []
numbers = list()

people = ["Igor", "Oleg", "Andrii"]
numbers = [1, 2, 3, 4]

objects = [1, 7.7, True, 'Ukraine']
print(people)

country = "New Zealand"
country_letters = list(country)
print(country_letters)

# Використання * при створенні списку
numbers11 = [1] * 11
print(numbers11)

name = ["Igor", "Tetiana"] * 7
print(name)

# Звертання до елементів списку здійснюється за індексом. Індекс першого елементу масиву - 0
print(name[3])

print(name[-1])
print(name[-3])

# Розкладання списку
people = ["Igor", "Oleg", "Andrii"]
igor, oleg, andrii = people
print(igor)

# Перебір елементів списку
people = ["Igor", "Oleg", "Andrii"]
for person in people:
    print(person)
    person += "!"
print(people)

# len() - повертає кількість елементів в списку
i = 0
while i < len(people):
    print(people[i])
    people[i] += "!"
    i += 1
print(people)

# Перевірка списків на рівність
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])

if numbers1 == numbers2:
    print('two lists are equal')
else:
    print('not equal')

# Отримання частини списку (slice)
# people [:end] - повертає список від початку до end (не включно) [0,end)
# people [start:end] - повертає список від start (включно) до end (не включно) [start,end)
# people [start:end:step] - повертає список від start (включно) до end (не включно) з кроком step [start,end)
people = ["Tom", "Bill", "Alice", "Sam", "Ross", "Monica"]

slice_1 = people[:4]
print(slice_1)

slice_2 = people[1:5]
print(slice_2)

slice_3 = people[1:10:2]
print(slice_3)

slice_4 = people[:-1]
print(slice_4)

slice_5 = people[-3:-1]
print(slice_5)

# Методи для роботи зі списками
# Додавання та видалення елементів зі списку
people = ['Tetiana', 'Kateryna']
# append() - додавання елементу в кінець списку
people.append('Olga')
print(people)

# extend() - розширює існуючий список іншим списком
people.extend(['Iryna', 'Olena'])
print(people)

people.append(['Iryna', 'Olena'])
print(people)
print(people[5][0])

# insert() - додавання елемента на вказану позицію
people.insert(2, 'Nadiia')
print(people)

# index() - повертає індекс елемента
index_of_iryna = people.index('Iryna')
print(index_of_iryna)

# pop() - видаляє елемент за вказаним індексом
removed_element = people.pop(3)
print(people)
print(removed_element)
people.pop()
print(people)

# remove() - видаляє елемент за вказаним значенням
people.remove('Olena')
print(people)

# clear() - повністю очищує список
people.clear()
print(people)

# Перевірка на наявність елемента в списку
people = ['Tetiana', 'Kateryna', 'Iryna', 'Olena']
if 'Kateryna' in people:
    people.remove('Kateryna')

del people[-1]
print(people)

# Підрахунок кількості входжень елементу в список
people = ['Tetiana', 'Kateryna', 'Iryna', 'Olena', 'Tetiana']
tetiana_count = people.count('Tetiana')
print(tetiana_count)

# Сортування
people.sort()
print(people)
people.reverse()
print(people)

people = ['Tetiana', 'kateryna', 'alice', 'Iryna', 'Olena', 'Tetiana']
people.sort()
print(people)

# сортування без врахування регістру
people.sort(key=str.lower)
print(people)

# пошук мінімального та максимального значення
numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))
print(max(numbers))

# Об'єднання двох списків
people1 = ["Tom", "Bob", "Alice"]
people2 = ["Tom", "Sam", "Tim", "Bill"]
people_3 = people1 + people2
print(people_3)

# Список списків
people_with_age = [['Igor', 18], ['Alice', 19], ['Tetiana', 25]]

print(people_with_age[1][1])
people_with_age[1].append('+38043948345')

for person in people_with_age:
    for item in person:
        print(item, end=" |")
    print()

# List Comprehension
# syntax: new_list = [вираз for елемент in iterable]
# syntax: new_list = [вираз for елемент in iterable [if умова]]
x = [1, 2, 3, 4, 5, 6]
x2 = []
for y in x:
    x2.append(y * y)
print(x2)

x2 = [y * y for y in x]
print(x2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_a)

# Фільтрування списку
# filter(fun, iter) - fun - функція-умова, в яку передається кожен елемент з колекції і яка повертає значення True, якщо елемент відповідає певній умові, в іншому випадку - False. iter - колекція
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
numbers_greater_than_1 = [number for number in numbers if number > 1]
print(numbers_greater_than_1)


def condition_1(number):
    # if number > 1:
    #     return True
    # else:
    #     return False
    return number > 1

numbers_greater_than_1_v2 = list(filter(condition_1, numbers))
print(numbers_greater_than_1_v2)

#Проєкція списку
#map(fun, iter) - fun - функція перетворення, в яку передається кожен елемент з колекції, iter - колекція
def square(number):
    return number * number

result = list(map(square, numbers))
print(result)