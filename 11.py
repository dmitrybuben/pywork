# 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('Введите N:'))
numbers = [1]
for e in range(1, n):
    e = numbers[e-1] * -3
    numbers.append(e)
print(numbers)

