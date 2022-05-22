# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file_n.txt в одной строке одно число

from functools import reduce
import math


n = 5

lst = [e for e in range(-n,n+1)]

with open ('file_n.txt', 'r') as f:
    positions = f.read().replace('\n','')

print(f'Произведение элементов: {reduce(lambda x,y:x*y,[lst[int(i)] for i in positions])}')
print(f'Произведение элементов: {math.prod([lst[int(i)] for i in positions])}')