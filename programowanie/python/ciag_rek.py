#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a1 = 2
# an = an - 1 * n^2 + 1

def ciag_rek(n):
    if n == 1 :
        return 2
    return ciag_rek (ciag_rek*n - 1 * n^2 + 1 )


def main(args):
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
