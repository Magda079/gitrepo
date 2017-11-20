#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nwd_v1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main(args):
    a = int(input('Podaj liczbę naturalną'))
    b = int(input('Podaj liczbę naturalną '))
    assert nwd_v1(5, 10) == 5
    assert nwd_v1(3, 9) == 3
    assert nwd_v1(4, 8) == 4
    print("NWD({:d}, {:d}) = {:d}".format(a, b, nwd_v1(a, b)))
    print('Największy wspolny dzielnik', nwd_v1(a, b))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
