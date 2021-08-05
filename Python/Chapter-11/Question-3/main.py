'''
문자열 뒤집기

1. S의 모든 숫자가 같은지 확인
2. S의 숫자가 모두 같지 않다면, 연속된 숫자 구간 수 카운트
3. 0의 연속된 숫자 구간 수와 1의 연속된 숫자 구간 수 중 더 적은 수를 계산
'''

S = str(input())
cnt_0, cnt_1 = 0, 0
before_s = S[0]
for s in S:
    if s != before_s and before_s == '0':
        cnt_0 += 1
    elif s != before_s and before_s == '1':
        cnt_1 += 1

    before_s = s

if before_s == '0':
    cnt_0 += 1
else:
    cnt_1 += 1

result = cnt_0 if cnt_0 < cnt_1 else cnt_1
print(result)