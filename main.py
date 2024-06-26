WIDTH, HEIGHT = 8, 8


def pictureBoard():
    print('12345678')
    print('+--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print([x][y], end='')
            print('%s|' % (y+1))
    print('+--------+')
    print('12345678')


print('Это игра Реверси')
pictureBoard()
