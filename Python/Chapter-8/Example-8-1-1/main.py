# 피보나치 수열 - 다이나믹 프로그래밍 - Top Down

d = [0] * 100

def fibo(n):
    if n == 1 or n == 0:
        return 1

    if d[n] == 0:
        d[n] = fibo(n - 1) + fibo(n - 2)

    return d[n]

for i in range(0, 10 + 1):
    print(fibo(i))
