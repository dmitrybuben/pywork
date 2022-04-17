# Найти максимальное из пяти чисел
from random import randint

a = randint(0,100)
print(a)
b = randint(0,100)
print(b)
c = randint(0,100)
print(c)
d = randint(0,100)
print(d)
e = randint(0,100)
print(e)
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print('Максимальное число:',max)