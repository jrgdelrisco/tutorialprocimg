from __future__ import print_function


def collatz(n):
    print("Collatz sequence of {}:".format(n))
    while n != 1:
        if n % 2:
            tmp = 3 * n + 1
            print("n = 3 x {} + 1 = {}".format(n, tmp))
        else:
            tmp = n // 2
            print("n = {} / 2 = {}".format(n, tmp))
        n = tmp


collatz(7)
