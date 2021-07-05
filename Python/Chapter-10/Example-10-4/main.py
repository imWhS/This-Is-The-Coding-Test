V, E = map(int, input().split())
PARENT = [0] * (V + 1)

for v in range(1, V + 1):
    PARENT[v] = v

cycle = False

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

for e in range(E):
    a, b = map(int, input().split())

    # 사이클 여부 검사
    if find(PARENT, a) == find(PARENT, b):
        # a의 루트 노드와 b의 루트 노드가 같으면 사이클 발생 처리
        cycle = True
        break
    else:
        # 사이클이 발생하지 않는다면 union 연산 실행
        union(PARENT, a, b)




