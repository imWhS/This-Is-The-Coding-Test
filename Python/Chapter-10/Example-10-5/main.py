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

V, E = map(int, input().split())

EDGES = []
for _ in range(E):
    distance, start, end = map(int, input().split())
    EDGES.append((distance, start, end))
EDGES.sort()

PARENT = [] * (V + 1)
for v in range(1, V + 1):
    PARENT[v] = v

result = 0 # 최소 비용 저장

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 그래프를 구성하는 간선을 적은 거리 비용 순으로 하나 씩 순차 탐색
for edge in EDGES:
    distance, start, end = edge

    # 사이클 발생 여부 확인
    if find(PARENT, start) == find(PARENT, end):
        continue

    # 사이클을 발생시키지 않으면 신장 트리에 포함
    union(PARENT, start, end)
    result += distance