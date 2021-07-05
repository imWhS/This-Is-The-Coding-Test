'''
EXAMPLE 1
input:
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
output:

'''

V, E = map(int, input().split()) # 그래프 내 총 간선의 수

EDGES = [] # 그래프를 구성하는 간선들의 정보 저장
for e in range(E):
    s, f, d = map(int, input().split())
    EDGES.append((d, s, f))
EDGES.sort()

PARENT = [0] * (V + 1)
for v in range(1, V + 1):
    PARENT[v] = v

RESULT = 0  # 최소 비용 저장

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

# 그래프를 구성하는 간선을 적은 비용 순으로 하나 씩 순차 탐색
for edge in EDGES:
    d, s, f = edge

    # 사이클 발생 여부 확인
    if find(PARENT, s) == find(PARENT, f):
        continue

    union(PARENT, s, f)
    RESULT += d




