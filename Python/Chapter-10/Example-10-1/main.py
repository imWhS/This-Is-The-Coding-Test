'''
DISJOINT SETS ALGORITHM

자료 구조
- V: 노드의 수
- E: 간선의 수
- PARENT: 부모 노드 번호 저장 테이블로, 1번부터 V번 노드를 표현하기 위해 최대 V + 1 개 필요
'''

# UNION 연산을 위한 FIND
def find(parent, x):
    # PARENT에 자신과 다른 노드의 번호가 기록되어 있다면 다른 부모를 가지고 있음을 의미하기에, 해당 노드 번호를 이용해 다시 FIND 연산 진행
    if x != parent[x]:
        return find(parent, parent[x])

    return x


# 주어진 원소 번호로 UNION 연산 실행
def union(parent, a, b):
    # 주어진 원소들의 루트 노드를 이용해 연결해야 하기 때문에, 각자의 루트 노드 탐색
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
PARENT = [0] * (V + 1)

# PARENT 각 인덱스를 노드 자신 번호로 초기화
for i in range(1, V + 1):
    PARENT[i] = i

# 입력으로 주어진 원소 번호로 UNION 연산 실행
for e in range(E):
    a, b = map(int, input().split())
    union(PARENT, a, b)

# 각 원소가 속해있는 집합 출력
for v in range(1, V + 1):
    p = find(PARENT, v)
    if v == p:
        print(f"{v}번 원소는 트리의 루트입니다.")
    else:
        print(f"{v}번 원소는 {p}번 원소가 트리의 루트인 집합에 속해있습니다.")

print()

