import sys

WIDTH, HEIGHT = 8, 8


def newBoard():
    board = []
    for i in range(WIDTH):
        board.append(['', '', '', '', '', '', '', ''])
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


def play():
#    board = newBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


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


board = newBoard()

play()

pictureBoard(board)
