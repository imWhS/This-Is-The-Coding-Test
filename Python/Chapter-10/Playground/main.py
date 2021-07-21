'''
Playground of UNION-FIND data structure
'''

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

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


'''
Kruskal Algorithm
- O(E logE)
'''

V, E = map(int, input().split())
PARENT = [0] * (V + 1)
EDGES = []

for v in range(V + 1):
    PARENT[v] = v

for _ in range(E):
    distance, start, end = map(int, input().split())
    EDGES.append((distance, start, end))

EDGES.sort()

for edge in EDGES:
    result = []
    distance, start, end = edge

    if find(PARENT, start) == find(PARENT, end):
        continue

    union(PARENT, start, end)
    result.append(distance)




