#숫자 카드 게임

N, M = map(int, input().split())
maximum = int()
for n in range(0, N):
    cards = list(map(int, input().split()))
    maximum = max(min(cards), maximum)
print(maximum)

# minimums = list()
# for n in range(0, N):
#     cards = list(map(int, input().split()))
#     cards.sort()
#     print(f"최소 값: ", cards[0])
#     minimums.append(cards[0])
#
# print(f"최소 값들: ")
# for m in range(0, len(minimums)):
#     print(minimums[m])
#
# minimums.sort()
#
# print(f"최소 값: {minimums[-1]}")



