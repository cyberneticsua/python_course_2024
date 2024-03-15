# Множина зберігає тільки унікальні елементи
# Для визначення множини використовуються фігурні дужки {}
users = {'Iryna', 'Tetiana', 'Kateryna', 'Tetiana'}
print(users)

users = set()
students = ['Iryna', 'Tetiana', 'Kateryna', 'Tetiana']
print(set(students))

# Додавання елементів в множину
students = {'Iryna', 'Tetiana', 'Kateryna', 'Tetiana'}
students.add('Mariia')
students.add('Mykola')
print(students)

# Видалення елементу з множини - remove()
students.remove('Mykola')
print(students)

# discard() - видаляє елемент з множини (не генерує помилку у випадку відсутності елемента)
students.discard('Mariia')
students.discard('Mariia')
print(students)

# Видаляє всі елементи з множини
students.clear()

# Перебір всіх елементів множини
students = {'Iryna', 'Tetiana', 'Kateryna', 'Tetiana'}
for stud in students:
    print(stud)

# Операції з множинами
# копіювання
users = students.copy()

# Об'єднання множин - union()
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
students_2 = {'Dmytro', 'Yuriy', 'Igor', 'Olena'}
all_students = students.union(students_2)
print(all_students)
print(students | students_2)

# Перетин множин - спільні елементи - intersection()
stud_3 = students.intersection(students_2)
print(stud_3)
print(students & students_2)

# intersection_update()
students.intersection_update(students_2)
print(students)

# Різниця множин - повертає ті елементи, які присутні в першій множині, але відсутні в другій
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
students_2 = {'Dmytro', 'Yuriy', 'Igor', 'Olena'}
stud_3 = students.difference(students_2)
print(stud_3)
stud_3 = students_2.difference(students)
print(stud_3)
print(students - students_2)

# symetric_difference() - повертає всі елементи обох множин, виключаючи спільні елементи
stud_3 = students.symmetric_difference(students_2)
print(stud_3)
print(students ^ students_2)

# Відношення між множинами
# issubset() - дозволяє перевірити, чи є поточна множина підмножиної іншої
student = {'Olena', 'Yuriy', 'Iryna', 'Serhii', 'Dmytro', 'Igor', 'Mariia'}
st_1 = {'Olena', 'Yuriy', 'Iryna'}
print(student.issubset(st_1))
print(st_1.issubset(student))

# issuperset() - дозволяє перевірити, чи є поточна множина надмножиною іншої
print(student.issuperset(st_1))
print(st_1.issuperset(student))

# frozen set - це вид множини, який не може бути змінений
users = frozenset({'Tom', 'Bob', 'Alice'})

# my_list = [1, 2, 3, 413, 4, 5, 3, 124, 2351, 12, 3, 34, 4, 5, 34, 63, 46, 143, 46, 54, 4]
# my_new_list = []
# for item in my_list:
#     if item not in my_new_list:
#         my_new_list.append(item)
# print(my_new_list)
# my_new_list = list(set(my_list))
# print(my_new_list)