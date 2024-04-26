#class назва_класу:
#   атрибути_класу
#   методи_класу
# клас - абстрактний обєкт з загальними характеристиками, наприклад Людина, Студент, Авто
# екземпляр класу - це конкретний представник класу, наприклад, Mercedes, Audi
# self - посилання на поточний обєкт
# Властивість-сеттер визначається після властивості-геттера. Назви властивостей - однакові
class Person:

    # конструктор
    def __init__(self, name, age, level=0):
        self.__name = name
        self.__age = age

    # def set_age(self, age):
    #     if age > 0:
    #         self.__age = age
    #     else:
    #         print('Некоректний вік')
    #
    # def get_age(self):
    #     return self.__age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Некоректний вік')

    @property
    def name(self):
        return self.__name

    def print_info(self):
        print(f'{self.__name} with age {self.__age}')

    def __secret_function(self):
        print()

    def do_something(self):
        print('do something')



tetiana = Person("Tetiana", 27) #Person() - виклик конструктора, який повертає об'єкт класу
# print(tetiana.__name)
andrii = Person("Andrii", 33)
# print(andrii.name)
# andrii.name = "Oleg"
# andrii.company = "Microsoft"
# print(andrii.company)
tetiana.print_info()
# tetiana.set_age(25)
# tetiana.set_age(-10)
tetiana.age = 22
print(tetiana.age)
tetiana.print_info()


#Успадкування дозволяє створити новий клас на основі вже існуючого класу. Поряд з інкапсуляцією
#є одним з принципів ООП.
#Ключові поняття:
#Підклас, клас нащадок, дочірній клас - успадковує від суперкласу всі публічні атрибути та методи
#Суперклас (базовий клас, батьківський клас).
#class клас_нащадок (батьківський_клас):
#   методи_класу_нащадку

class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company
    def work(self):
        print(f'{self.name} works')

    def print_info(self):
        super().print_info()
        print(f'Company: {self.company}')

class Worker:
    def work(self):
        print(f'Works')
    def do(self):
        print('do work')

class Student (Person):
    def study(self):
        print(f'Studies')

    def do(self):
        print('do study')
class WorkingStudent(Student, Worker):
    pass
igor = Employee('Igor',55, 'CHNU')
igor.print_info()
# noname = WorkingStudent()
# noname.work()
# noname.study()
# noname.do()

#isinstance(object, type) , isinstance(tetiana, Student)

def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_something()


oleg = Student('Oleg', 33)
act(tetiana)
act(igor)
act(oleg)