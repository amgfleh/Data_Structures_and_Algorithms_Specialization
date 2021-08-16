# Uses python3

def calc_fib(n):
    a = [0, 1]
    if n < 2:
        return a[n]
    for i in range(2, n + 1):
        a.append(a[-1] + a[-2])
    return a[-1]


m = int(input())
print(calc_fib(m))
