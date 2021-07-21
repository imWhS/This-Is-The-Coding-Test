'''
Kruskal Algorithm
- 그래프의 모든 정점을 최소 거리 비용으로 연결할 신장 트리를 찾는 알고리즘
- 거리 비용이 적은 순으로 간선을 선택한 후, UNION-FIND 자료 구조를 이용해 사이클을 발생시키지 않으면 신장 트리에 포함시킨다.

필요 자료 구조
- V: 정점의 수
- E: 간선의 수
- EDGES: 간선 별 두 정점 간 연결 정보 (두 정점 간 거리 비용, 시작 정점, 끝 정점)
- PARENT: 노드 별 부모 노드 번호 정보
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

# 노드와 간선의 수 입력
V, E = map(int, input().split())

# 노드 간 연결 정보를 표현하는 간선 데이터 저장 리스트
EDGES = []

# 간선 데이터 입력
for _ in range(E):
    distance, start, end = map(int, input().split())
    EDGES.append((distance, start, end))

# 최소 비용 순으로 간선 데이터 정렬
EDGES.sort()

# UNION-FIND를 위한 노드 별 루트 노드 번호 정보 저장 리스트
PARENT = [0] * (V + 1)

# PARENT의 노드 별 루트 노드 번호는 자신의 번호로 초기화
for v in range(1, V + 1):
    PARENT[v] = v

# 최소 비용의 합 저장
result = 0

# 최소 비용 순으로 간선을 하나씩 탐색
for edge in EDGES:
    distance, start, end = edge

    # 사이클 발생 시 최소 비용의 합에 미포함
    if find(PARENT, start) == find(PARENT, end):
        continue

    union(PARENT, start, end)
    result += distance