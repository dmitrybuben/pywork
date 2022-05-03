# 32.	Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# list = [1, 3, 10, 12, 3, 4, 10, 3]
from random import randint

def sortedlist(coll):
    sortedlist = []
    for i in coll:
        if coll.count(i) == 1:
            sortedlist.append(i)
            i +=1
    return(sortedlist)

list = [randint(1,20) for i in range(1,11)]
print(list)
print(sortedlist(list))