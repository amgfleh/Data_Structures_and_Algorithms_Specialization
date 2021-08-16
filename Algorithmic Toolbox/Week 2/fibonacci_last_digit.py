# Uses python3
import sys


def fibonacci_last_digit(n):
    a = [0, 1]
    if n < 2:
        return a[n]
    for i in range(2, n + 1):
        a.append((a[-1] + a[-2])%10)
    return a[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_last_digit(n))
