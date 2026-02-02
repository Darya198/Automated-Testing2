import math


x = int(input("Введите сторону квадрата: "))


def square(x):
    return math.ceil(x * x)


print(square(x))
