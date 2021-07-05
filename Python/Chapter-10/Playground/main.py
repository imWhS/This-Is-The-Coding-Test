def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def find_cr(parent, x):
    if parent[x] != x:
        parent[x] = find_cr(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

V, E = map(int, input().split())
PARENT = [0] * (V + 1)
for v in range(V + 1):
    PARENT[v] = v

for _ in range(E):
    a, b = map(int, input().split())
    union(PARENT, a, b)

# 각 원소가 속해있는 집합의 루트 노드 출력
for v in range(1, V + 1):
    print(f"{v}는 {find(PARENT, v)}가 루트 노드인 트리에 속해있어요.")

print("PARENT TABLE")
# PARENT 인덱스 별 값 출력
for p in range(1, V + 1):
    print(PARENT[p], end = " ")