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
stack = []

for i in range(len(S) - 1, -1, -1):
    stack.append(int(S[i]))

print(stack)
print(stack.pop())
print(len(stack))

while(len(stack)):

    a = stack[-1]
    stack.pop()

    b = 0
    if len(stack) > 0:
        b = stack[-1]
        stack.pop()

    b = stack[-2]
    stack.pop()

    print(f"{a}, {b}")









# for i in range(len(S) - 1):
#     print(f"compare {S[i]} with {S[i + 1]}")
#
#     multiplied = int(S[i]) * int(S[i + 1])
#     added = int(S[i]) + int(S[i + 1])
#     print(f" - multiplied: {multiplied}")
#     print(f" - added: {added}")

    # if multiplied < added:
