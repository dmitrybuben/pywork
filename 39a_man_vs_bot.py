# 39.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

# --------------------------
# ИГРА ЧЕЛОВЕКА ПРОТИВ БОТА
# --------------------------


import random

def game(cands,max_step,min_step,pls_list):
    turn = random.randint(0,1)
    while cands > 0:                                                                        # проверка кто ходит первым
        if pls_list[turn] == 'БОТ':
            print(f'{pls_list[turn]}, возьмите конфеты, от {min_step} до {max_step}:')
            step = random.randint(min_step, max_step)
            if step > cands:
                step = cands
            cands -= step
            print(f'{pls_list[turn]} взял {step} конфет')
        else:
            step = int(input(f'{pls_list[turn]}, возьмите конфеты, от {min_step} до {max_step}:'))
            if step >= min_step and step <= max_step and step <= cands:
                cands -= step
            else:
                print('Не то количество - начинаем заново')
                break
        if cands == 0:
            print(f'Конфет не осталось, победил {pls_list[turn]}')
        else:
            print(f'Осталось {cands} конфет')
        if cands > 0:
            if pls_list[not turn] == 'БОТ':
                print(f'{pls_list[not turn]}, возьмите конфеты, от {min_step} до {max_step}:')
                step = random.randint(min_step, max_step)
                cands -= step
                print(f'{pls_list[not turn]} взял {step} конфет')
            else:
                step = int(input(f'{(pls_list[not turn])}, возьмите конфеты, от {min_step} до {max_step}:'))
                if step >= min_step and step <= max_step and step <= cands:
                    cands -= step
                else:
                    print('Не то количество - начинаем заново')
                    break
            if cands == 0:
                print(f'Конфет не осталось, победил {pls_list[not turn]}')
            else:
                print(f'Осталось {cands} конфет')
    return


cands = int(input('Сколько конфет разыгрываем? '))
max_step = int(input('Сколько конфет можно брать за один ход? '))
min_step = 1
pls_list = ['игрок_1','БОТ']
game(cands,max_step,min_step,pls_list)