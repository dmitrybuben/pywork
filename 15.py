# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def makelist (n):
    list = []
    pr = 1
    for i in range(1,n+1):
        pr = pr*i
        list.append(pr)
    print(list)

x = int(input('Введите N:'))
makelist(x)
