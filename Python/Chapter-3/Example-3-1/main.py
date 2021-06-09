#거스름돈

N = int(input())
coin_cnt = int()
coin_list = [500, 100, 50, 10]

for coin in coin_list:
  if N < coin: continue
  coin_cnt += N // coin
  N %= coin

print(coin_cnt)