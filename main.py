import random

WIDTH, HEIGHT = 8, 8


def newBoard():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def pictureBoard(board):
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')


def play(playerFishka, computerFishka):
    board = newBoard()
    turn = ''
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
    pictureBoard(board)
    print()

    if random.randint(0, 1) == 0:
        turn = 'Компьютер'
        print('Компьютер ходит первым')
    else:
        turn = 'Человек'
        print('Человек ходит первым')

    if turn == 'Человек':
        print('test human')
    else:
        print('test computer')


def ValidXod(board, x, y):
    # Проверка (возвращает False), если ход игрока в клетку c координатами x, y - недопустимый.)
    # True е



def inputFishka():
    Fishka = ''
    print('Вы играете за X или O ?')
    Fishka = input().upper()

    if Fishka == 'X':
        return ['X', 'O']
    else:
        return ['O', 'x']


print('Это игра Реверси')

playerFishka, computerFishka = inputFishka()
play(playerFishka, computerFishka)


