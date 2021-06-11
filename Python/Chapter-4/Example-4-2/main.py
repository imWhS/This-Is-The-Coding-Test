#시각

N = int(input())
cnt = int()

for h in range(0, N + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            time = str(h) + str(m) + str(s)
            if time.count('3'):
                cnt += 1  #3이 포함된 '시각의 개수'를 구해야 한다! 한 시각 안에서 '3'이 포함된 개수가 아니라!!

print(cnt)
