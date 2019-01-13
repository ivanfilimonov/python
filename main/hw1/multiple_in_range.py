#!/usr/bin/python3


def multiple_in_range(x, y):
    list = []
    if (type(x) is not int or type(y) is not int): raise TypeError
    for i in range(x, y + 1):
        if (i % 7 == 0 and i % 5 != 0):
            list.append(i)
    print(list)
    return list
