# Uses python3
import sys


def fibonacci_last_digit_sum(n, m=10):
    a = [0, 1]
    if n < 2:
        return a[n]
    sum = 1
    pisano = 60
    n_1 = n % pisano
    if n_1 == 0:
        return 0
    if n_1 == 1:
        return 1
    for i in range(2, n_1 + 1):
        a.append((a[-1] + a[-2]) % m)
        sum += a[-1]
    return sum % 10


def fibonacci_partial_sum(n, m):
    a = [0, 1]
    if n in a and m in a:
        return a[m] + a[n]
    if n == 0:
        return fibonacci_last_digit_sum(m)
    sum = fibonacci_last_digit_sum(m) - fibonacci_last_digit_sum(n-1)
    return sum % 10


# c, d = input().split()
# print(fibonacci_partial_sum(int(c), int(d)))


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))