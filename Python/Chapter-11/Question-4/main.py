'''
만들 수 없는 금액
- 주어진 동전의 화폐 단위 중 비어있는 금액대를 조사한다.
- 주어진 동전들을 높은 단위 순으로 이용해 비어있는 금액대를 만들 수 있는지 조사한다.
'''

N = int(input())

coins = list(map(int, input().split()))
coins.sort(reverse = True)

coins_cnt_table = dict()
for coin in coins:
    if coin in coins_cnt_table:
        coins_cnt_table[coin] += 1
    else:
        coins_cnt_table[coin] = 1

value = 0
while True:
    value += 1

    if value in coins_cnt_table:
        continue

    current_value = value
    is_avail = False
    for coin in coins:
        if current_value < coin:
            continue

        current_value = current_value - coin

        if current_value == 0:
            coins_cnt_table[value] = 0
            is_avail = True
            break

    if is_avail == False:
        break

print(value)








