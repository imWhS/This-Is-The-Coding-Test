#부품 찾기 - 계수 정렬

N = int(input())
# storeParts = list(map(int, input().split()))
storeParts = [0] * 1000000

for i in map(int, input().split()):
    storeParts[i] = 1

M = int(input())
customerParts = list(map(int, input().split()))

for m in range(0, M):
    # print(f"Find {customerParts[m]}")
    if storeParts[customerParts[m]] == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")
