'''
팀 결성

input
학생 별 부여 가능 최대 번호 N, 연산의 수 M
a, b 학생이 속한 팀 합치기 연산 0 a b 혹은 a, b 학생의 같은 팀 여부 확인 연산 1 a b

output
같은 팀 여부 확인 연산 결과 "YES" 혹은 "NO"
'''

N, M = map(int, input().split())
TEAM = [0] * (N + 1) # 학생 별 속해있는 팀 번호 저장 리스트.

# 학생 별 속해있는 팀 번호 저장 리스트의 모든 초기 값은 자신의 번호
for t in range(0, N + 1):
    TEAM[t] = t

def find(team, x):
    if team[x] != x:
        team[x] = find(team, team[x])
    return team[x]

def union(team, a, b):
    a = find(team, a)
    b = find(team, b)

    if a > b:
        team[a] = b
    else:
        team[b] = a


for _ in range(M):
    operation, a, b = map(int, input().split())
    if operation == 0:
        # 팀 합치기 연산
        union(TEAM, a, b)
    else:
        # 같은 팀 여부 확인 연산
        if find(TEAM, a) == find(TEAM, b):
            print("YES")
        else:
            print("NO")

