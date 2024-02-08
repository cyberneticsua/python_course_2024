# Імя змінної містить букви, цифри і знак підкреслення _. Python чутливий до регістру.
# Імена змінних не містять букв у верхньому регістрі
a = 19
b = 5
c = a + b
print(c)
count_of_students = 55
count_of_students = 55
first_number = 1
second_number = 1
result = first_number + second_number
# Underscore Case - count_of_students
# Camel Case - countOfStudents
# Pascal Case - CountOfStudents
# Типи даних - в Python динамічна типізація
# int
a = 5
print(type(a))
# float
a = 5.0
print(type(a))
# str
a = "Hello"
a = 'Hello'
print(type(a))
# bool
a = True
a = False
print(type(a))
# Оператори +, -, *, /, **
a = 19
b = 5
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
# піднесення до степеня **
c = a ** b
print(c)
# цілочислове ділення
c = a // b
print(c)
# остача від ділення ділення
c = a % b
print(c)
c = a + b
# Виведення інформації
print(f'{a}+{b}={c}')
print(f'{a}+b={c}')
print('{}+{}={}'.format(a, b, c))
print(f'Language \n Python \n C#')
print(f'Language \t Python \t C# \' \" \\ ')

#Введення інформації
# count = input()
# print(type(count))
# count = int(input())
# print(type(count))
# count = float(input())
# print(type(count))
# count = bool(input())
# print(count)
# count = bool(input())
# print(count)
a = input()
b = input()
c = a+b
print(f'{a}+{b}={c}')
c = a*b
print(f'{a}*{b}={c}')

#Оператори порівняння >, <, >=, <=, ==, !=
a = 5
b = 10
c = a > b
print(c)
c = a < b
print(c)

#Умовний оператор if
#if умова:
#    оператор
if a > b:
    print(f'{a}>{b}')
    print('In if')
if a == b:
    print(f'{a}<{b}')
    print('In if')
print('Not in if')