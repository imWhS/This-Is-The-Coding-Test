'''
도시 분할 계획

input
집의 수 N, 길의 수 M
집 A, 집 B, A와 B를 연결하는 길의 유지비 C

output
길을 없앤 후 남은 집들의 유지비 합 최소 값

example
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''

N, M = map(int, input().split())

VILIAGE = [0] * (N + 1)
for n in range(1, N + 1):
    VILIAGE[n] = n

ROADS = []
for m in range(M):
    A, B, C = map(int, input().split())
    ROADS.append((C, A, B))
ROADS.sort()

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

sum = 0
maximum_cost = 0
roads_selected = []

for road in ROADS:
    C, A, B = road

    if find(VILIAGE, A) == find(VILIAGE, B):
        continue

    union(VILIAGE, A, B)
    sum += C
    maximum_cost = C

print(sum - maximum_cost)


