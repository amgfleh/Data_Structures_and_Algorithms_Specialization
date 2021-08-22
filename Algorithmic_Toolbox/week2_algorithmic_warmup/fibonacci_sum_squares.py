# Uses python3
from sys import stdin


def fibonacci_sum_squares(n):
    a = [0, 1]
    if n < 2:
        return a[n]
    pisano = 60
    n_1 = n % pisano
    if n_1 < 2:
        return a[n_1]
    for i in range(2, n_1 + 2):
        a.append((a[-1] + a[-2]) % 10)
    return (a[-1] * a[-2]) % 10


# c = input()
# print(fibonacci_sum_squares(int(c)))


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
