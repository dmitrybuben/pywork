# 39.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"


import random

def game(cands,max_step,min_step,pls_list):
    turn = random.randint(0,1)
    while cands > 0:
        step = int(input(f'{pls_list[turn]},возьмите конфеты, от {min_step} до {max_step}:'))
        if step >= min_step and step <= max_step and step <= cands:
            cands -= step
        else:
            print('Не то количество - начинаем заново')
            break
        if cands > 0:
            print(f'Осталось {cands} конфет')
            step = int(input(f'{(pls_list[not turn])},возьмите конфеты, от {min_step} до {max_step}:'))
            if step >= min_step and step <= max_step and step <= cands:
                cands -= step
            else:
                print('Не то количество - начинаем заново')
                break
        if cands > 0:
            print(f'Осталось {cands} конфет')
        else:
            print('Конфеты закончились')
            print(f'Победил {pls_list[turn]}')
    # print(f'Победил_ {pls_list[not turn]}')
    return


cands = int(input('Сколько конфет разыгрываем? '))
max_step = int(input('Сколько конфет можно брать за один ход? '))
min_step = 1
pls_list = ['игрок_1','игрок_2']
game(cands,max_step,min_step,pls_list)