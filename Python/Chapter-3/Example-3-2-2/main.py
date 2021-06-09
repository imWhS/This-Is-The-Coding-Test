#큰 수의 법칙 - 2

numbers_cnt = [0] * 1000
N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))
for i in input_list:
    numbers_cnt[i] += 1
first = -1
second = -1

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

print("first: " + str(first) + ", second: " + str(second))

#총 길이 M 중에서 K + 1 길이의(first, second로 구성된) 수열이 반복되는 횟수에 K를 곱하면 하나의 수열을 구성하는 first 개수 도출
first_cnt = int(M / (K + 1)) * K

#총 길이 M 중에서 K + 1 길이보다 적은(꼬리 부분의) 수열을 구성하는 수는 모두 first 개수에 포함. second는 오직 K + 1 길이의 수열에서 마지막에 위치하기 때문
first_cnt += M % (K + 1)

#총 M개 중 first 개수를 제외한 값이 second 개수
second_cnt = M - first_cnt

sum = (first_cnt * first) + (second_cnt * second)
print(sum)