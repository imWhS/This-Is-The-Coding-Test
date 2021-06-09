#큰 수의 법칙 - 1

numbers_cnt = [0] * 1000
N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))
for i in input_list:
    numbers_cnt[i] += 1
first = -1
second = -1
sum = 0

i = 1000
while i >= 0:
    i -= 1
    if numbers_cnt[i] == 0:
        continue

    if first == -1:
        first = i
        if numbers_cnt[i] > 1:
            second = i
            break
    elif second == -1:
        second = i

m = 0
first_used = 0
print("first: " + str(first) + ", second: " + str(second))
while m < M:
    m += 1
    if first_used == K:
        sum += second
        print("added " + str(second))
        first_used = 0
        continue
    sum += first
    first_used += 1
    print("added " + str(first))

print(sum)