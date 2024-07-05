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

def isonboard(x,y):
    # вернуть True если координаты есть на игровом поле
    if x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1:
        return True


def ValidXod(board, fishka, xstart, ystart):
    # Проверка (возвращает False), если ход игрока в клетку c координатами x, y - недопустимый.)
    # True если это допустимый ход, вернётся список клеток которые стали бы принадлежать игроку, если бы он сделал ход
    if board[x][y] != ' ' or not isonboard(xstart, ystart):
        return False

    if fishka == 'X':
        overfishka = 'O'
    else:
        overfishka = 'X'

        fiskatoflip = []

    for xdirection, ydirection in [[0,1],[1,1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isonboard(x, y) and board[x][y] == overfishka:
            # Продолжаем двигаться в направлении x, y
            x += xdirection
            y += ydirection
            if isonboard(x, y) and board[x][y] == fishka:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    fiskatoflip.append([x, y])

    if len(fiskatoflip) == 0:
        return False
    return fiskatoflip


def inputFishka():
    fishka = ''
    print('Вы играете за X или O ?')
    fishka = input().upper()

    if fishka == 'X':
        return ['X', 'O']
    else:
        return ['O', 'x']


print('Это игра Реверси')

playerFishka, computerFishka = inputFishka()
play(playerFishka, computerFishka)


