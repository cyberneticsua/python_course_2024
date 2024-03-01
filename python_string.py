'''

'''
message = 'Hello'
message = "Hello"

text = ('Super Long text '
        'Cybernetics Chernivtsi')
print(text)

text = '''
Chernivtsi
Kyiv
'''

print('М\'яч')
print("М'яч")

# Додавання значень в рядок
user_name = "Tetiana"
user_age = 17
user = f'Name {user_name} віком {user_age}'

# Звертання до символів рядка
country = 'Ukraine'
print(country[0])
print(country[-1])

# Перебір елементів в рядку
for letter in country:
    print(letter, end=' - ')

# Отримання підрядка
# string [:end] - повертає підрядок від початку до end (не включно) [0,end)
# string [start:end] - повертає підрядок від start (включно) до end (не включно) [start,end)
# string [start:end:step] - повертає підрядок від start (включно) до end (не включно) з кроком step [start,end)

print(country[:3])
print(country[1:3])
print(country[0:5:2])

# Об'єднання рядків
name = "Igor"
surname = "Vinnychuk"
full_name = name + surname

# Повторення рядків
name = 'i' * 5
print(name)
name = 'ho' * 3
print(name)

# Порівняння рядків 1 2 ... A B ... a b
str1 = '1a'
str2 = 'aa'
str3 = 'Aa'
print(str1 > str2)  # False оскільки перший символ цифра, а цифра умовно менше будь-якої літери
print(str2 > str3)  # True оскільки літера в верхньому регістрі умовно менше літери у нижньому регістрі

str1 = "chernivtsi"
str2 = "Chernivtsi"
print(str1.lower() == str2.lower())
print(str1.upper() == str2.upper())

#Функції len i ord
print(ord('1'))
print(ord('I'))
print(ord('i'))

#Пошук в рядках
string = 'HelloUkraine'
if 'Hello' in string:
    print('ok')

# Перевірка рядків
# isalpha() - повертає True, якщо рядок складається тільки з символів абетки
# isdigit() - повертає True, якщо всі символи рядка - цифри
# isnumeric() - повертає True, якщо рядок може бути числом
# islower() - повертає True, якщо всі символи рядка в нижньому регістрі
# isupper() - повертає True, якщо всі символи рядка в верхньому регістрі

print(string.isalpha())

#startswith(str) - повертає True, якщо рядок починається з підрядка str
#endswith(str) - повертає True, якщо рядок закінчується на підрядок str
string = "Hello Ukraine"
print(string.startswith('Hello'))
print(string.endswith('Hello'))

#upper() - переводить весь рядок у верхній регістр
#lower() - переводить весь рядок у нижній регістр
#title() - переводить у верхній регістр всі слова в рядку
#capitalize() - переводить у верхній регістр тільки перше слово в рядку
string = "london is a capital of great britain. London is great city."
print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())

#lstrip() - видаляє всі пробіли на початку рядка
#rstrip() - видаляє всі пробіли в кінці рядка
#strip() - видаляє всі пробіли на початку і в кінці рядка
#ljust(width) - якщо довжина рядка менша за width, то справа до рядка додаються пробіли, щоб довжина рядка стала дорівнювати width
#rjust(width) - якщо довжина рядка менша за width, то зліва до рядка додаються пробіли, щоб довжина рядка стала дорівнювати width
#center(width) - якщо довжина рядка менша за width, то зліва та справа до рядка рівномірно додаються пробіли, щоб довжина рядка стала дорівнювати width
string = "Hello Ukraine"
print(string.ljust(20))
print(string.rjust(20))
print(string.center(20))

#Пошук в рядку
#find(str) - пошук підрядка str ведеться з початку рядка і до його кінця
#find(str, start) - пошук підрядка str ведеться з позиції start і до його кінця
#find(str, start, end) - пошук підрядка str ведеться з позиції start і до позиції end
string = "Hello Ukraine"
print(string.find('Ukr'))
print(string.find('Ukr', 8))
print(string.find('Ukr', 5, 9))

#Заміна в рядку
#replace(old, new) - замінює підрядок old на підрядок new
#replace(old, new, num) - замінює підрядок old на підрядок new num-разів
phone = "+38-050-666-55-44"
new_phone = phone.replace('-', ' ')
print(new_phone)
new_phone = phone.replace('-', ' ', 1)
print(new_phone)

#Розділення рядків
#split - повертає список рядків, розділених за допомогою певного символа
#split() - використовує як роздільник пробіл
#split(str) - використовує як роздільник символ str
#split(str, num) - використовує як роздільник символ str, а num вказує скільки входжень str використовується для розділення
string = 'London is a  capital of  Great  Britain. London is great city.'
words = string.split()
print(words)
words = string.split('  ')
print(words)
words = string.replace('.', '').replace(',', '').split()
print(words)

#З'єднання рядків
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
sentence = "|_|".join(words)
print(sentence)
