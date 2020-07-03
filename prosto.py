from math import sqrt
import itertools
import sys


def is_prime(merged):
    flag = True
    for j in range(merged[0], merged[-1]):
        if j in merged:
            n = j
            if n < 2:
                flag = False
            if n == 2:
                pass
            limit = sqrt(n)
            i = 2
            while i <= limit:
                if n % i == 0:
                    flag = False
                    break
                i += 1
            if flag is False:
                print("В списке есть не простое число: " + str(n))
                break
    if flag is True:
        print("В списке все простые числа!")


if __name__ == '__main__':
    limit = (sys.argv[1])
    with open(limit) as f:
        lis = [list(map(int, x.split())) for x in f if x.strip()]
        merged = list(itertools.chain.from_iterable(lis))
        is_prime(merged)
