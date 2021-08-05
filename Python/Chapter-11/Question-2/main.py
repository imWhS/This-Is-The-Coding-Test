'''
곱하기 혹은 더하기
- S: 숫자로만 구성된 문자열
- 연산자 관계 없이 모든 연산은 왼쪽에서 오른쪽으로 진행

입력
- S

출력
- S의 왼쪽부터 오른쪽 방향 순으로 각 숫자를 확인해, * 혹은 + 연산자 삽입해 만들 수 있는 가장 큰 수
'''

S = str(input())

result = 0
for s in S:
    added = result + int(s)
    multiplied = result * int(s)

    result = added if multiplied < added else multiplied

print(result)

'''
다른 풀이
1. 왼쪽에서 arr - 1까지 arr를 탐색해 변수 a, b에 2개의 숫자를 추출한다.
2. a, b 둘 중 하나라도 0 혹은 1이라면 a + b 연산 후 b가 추출되었던 인덱스에 저장한다.
3. i가 arr - 1일 때까지 반복한다.
'''

result = 0
arr = []

for s in S:
    arr.append(int(s))

for s in range(0, len(arr) - 1):
    current, next = int(s), int(s + 1)
    a, b = int(arr[current]), int(arr[next])

    if a <= 1 or b <= 1:
        arr[next] = a + b
    else:
        arr[next] = a * b

print(result)









# for i in range(len(S) - 1):
#     print(f"compare {S[i]} with {S[i + 1]}")
#
#     multiplied = int(S[i]) * int(S[i + 1])
#     added = int(S[i]) + int(S[i + 1])
#     print(f" - multiplied: {multiplied}")
#     print(f" - added: {added}")

    # if multiplied < added:
