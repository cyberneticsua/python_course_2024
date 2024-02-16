# Цикли:
# while - перевіряє умови чи вона істинна і якщо так, то виконує тіло циклу
# for
# while умова:
#     тіло циклу
# Ітерація - це одноразове виконання тіла циклу
number = 1
while number <= 5:
    print(f'number={number}')
    number += 1
print('Цикл завершено')

# Для циклу while можна додати умову else
number = 6
while number <= 5:
    print(f'number={number}')
    number += 1
else:
    print('Щось')

# Синтаксис циклу for
# for змінна in набір_значень:
#   інструкції

word = "Cybernetics"
for letter in word:
    print(letter)

# range() - генерує числову послідовність
for n in range(10):
    print(n, end=" ")
print()
# range(end) - генерується числова послідовність від 0 до end (не включно). [0, end)
# range(start, end) - генерується числова послідовність від start до end (не включно). [start, end)
# range(start, end, step) - генерується числова послідовність від start до end (не включно) з кроком step. [start, end)

for n in range(3, 9):
    print(n, end=" ")
print()

for n in range(3, 9, 2):
    print(n, end=" ")
print()

# Для циклу for можна також задати блок else
word = "Cybernetics"
for letter in word:
    print(letter)
else:
    print(f'Last symbol {letter}. Loop ended')

# Вкладені цикли
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i * j, end='\t')
        j += 1
    print('\n')
    i += 1
# Вихід з циклу
# continue та break
# break - здійснює вихід з циклу (припиняє його виконання)
# continue - здійснює перехід до наступної ітерації циклу
print('break')
number = 0
while number < 5:
    number += 1
    if number == 3:
        break
    print(number)


print('continue')
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

m = 0
for i in range(10):
    m+=i
print(m)

#len() - повертає розмір рядка, списку