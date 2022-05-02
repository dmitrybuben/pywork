# 31.	Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

def makelist(n):
    multlist = []
    i = 2
    while i < n+1: 
        if n % i == 0:
            multlist.append(i)
            n = n/i
        else:
            i += 1
    return(multlist)

x = int(input('Введите N:'))
print('Список простых множителей введенного числа:',makelist(x))