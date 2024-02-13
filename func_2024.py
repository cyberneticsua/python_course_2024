import math


def addition(param1, param2):
    # type your code here
    return


# оголошення функції:
# def імя_функції([параметри]):
#    тіло_функції
def first_function():
    print("**********")
    print("Hello")
    print("**********")


x = 10
y = 19
f = x + y
first_function()
first_function()


def first_function_name(name):
    print("**********")
    print(f"Hello {name}")
    print("**********")


first_function_name("Cybernetics")
my_name = "Chernivtsi"
first_function_name(my_name)
first_function()


def triangle_square(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

a = 4
b = 5
c = 6
print(triangle_square(4, 5, 6))
r = 3
t = 4
i = 5
s = triangle_square(r, t, i)
print(s)
