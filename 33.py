# 33.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# 1.	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def make_coef_list(n):              # создаем список коэффициентов
    coef_list = [randint(0,100) for i in range(0,n+1)]
    return(coef_list)

def make_string(lst):               # создаем строку из "перевернутого" списка
    reversed_list = lst[::-1]
    print(reversed_list)
    stroka = ''
    for i in range(1,k+1):
        pow = k+1-i
        stroka += f'{reversed_list[i-1]}*x^{pow}+'
    stroka += f'{reversed_list[-1]}=0'
    return(stroka)

def write_to_file(str):             # записываем результат (строку c многочленом) в файл 
    data = open('task33.txt', 'w')
    data.write(str)
    data.close()


k = int(input('Введите значение натуральный степени k:'))
lst = make_coef_list(k)
print(lst)
str = make_string(lst)
write_to_file(str)