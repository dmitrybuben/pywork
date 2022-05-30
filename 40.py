board = list(range(1, 10))

win_coords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9),
              (1, 5, 9), (3, 5, 7)]


def deck_draw():
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
    print('-------------')


def take_input(player_letter):
    while True:
        value = input(f'Куда поставить {player_letter} ? ')
        if value not in '1,2,3,4,5,6,7,8,9':
            print('Введено неверное значение')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
            print('Клетка занята')
            continue
        board[value-1] = player_letter
        break


def check_win():
    for each in win_coords:
        if board[each[0]-1] == board[each[1]-1] == board[each[2]-1]:
            return board[each[1]-1]
    else:
        return False


def main():
    counter = 0
    while True:
        deck_draw()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                deck_draw()
                print(f'{winner} выйграл')
                break
        counter += 1            # иначе, если после 3-х ходов нет выгрыша - ходим далее
        if counter > 8:         # условие завершения если после > 8 ходов нет победителя
            deck_draw()
            print('Ничья')
            break


main()
