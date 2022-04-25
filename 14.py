# 14.	Подсчитать сумму цифр в вещественном числе.

num = input('Введите вещественное число:')
num = int(num.replace('.',''))
sum = 0
while num != 0:
    sum += num % 10
    num //= 10
print('Сумма цифр числа:',sum)

