'''
UNION-FIND
'''

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 및 간선의 개수 입력
V, E = map(int, input().split())

# 노드 별 루트 노드 번호 정보 기록을 위한 리스트 생성 후 각 원소를 노드 자신의 번호로 초기화
PARENT = [0] * (V + 1)

for v in range(V + 1):
    PARENT[v] = v

# 간선의 개수만큼 UNION 연산 입력 및 실행
for e in range(E):
    a, b = map(int, input().split())
    union(PARENT, a, b)