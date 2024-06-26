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


print('Это игра Реверси')
board = newBoard()
pictureBoard(board)
