# 10.	Найти расстояние между двумя точками пространства
print('Введите координаты точки 1:')
x1 = float(input('х1:'))
y1 = float(input('y1:'))
z1 = float(input('z1:'))
print('Введите координаты точки 2:')
x2 = float(input('х2:'))
y2 = float(input('y2:'))
z2 = float(input('z2:'))
dist = ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5
print(f'Расстояние между точками 1 и 2 составляет:{dist}')