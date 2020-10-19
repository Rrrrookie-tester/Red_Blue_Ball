from random import sample, choice


def output(num, redB, blueB):
    print('----------第' + str(num+1) + '注----------')
    print('红球为：')
    print(*redB, sep=' ')
    print('蓝球为：')
    print(blueB)


def getBall():
    redBalls = \
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    redres = sample(redBalls, 5)
    blueBalls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    blueres = choice(blueBalls)
    res = []
    res.append(redres)
    res.append(blueres)
    return res


for i in range(0, 6):
    result = getBall()
    redB = result[0]
    blueB = result[1]
    output(i, redB, blueB)