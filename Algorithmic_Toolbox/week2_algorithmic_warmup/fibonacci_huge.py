# Uses python3
import sys


def calc_fib_modulo(n, m):
    a = [0, 1]
    if n < 2:
        return a[n]
    for i in range(2, n + 1):
        a.append((a[-1] + a[-2]) % m)
        if a[-1] == 1 and a[-2] == 0:
            pisano = len(a[:-2])
            n_1 = n % pisano
            return a[n_1]
    return a[-1]


# c, d = input().split()
# print(calc_fib_modulo(int(c), int(d)))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(calc_fib_modulo(n, m))
