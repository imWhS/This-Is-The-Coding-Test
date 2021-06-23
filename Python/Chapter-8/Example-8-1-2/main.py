# 피보나치 수열 - 다이나믹 프로그래밍 - Bottom Up
num = int(input())

d = [0] * 100
d[0], d[1] = 1, 1


for n in range(0, num + 1):
    if d[n] == 0:
        d[n] = d[n - 1] + d[n - 2]

for i in range(0, num + 1):
    print(d[i])

