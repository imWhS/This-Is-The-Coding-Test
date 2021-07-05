from collections import deque

# 노드의 수, 간선의 수
V, E = map(int, input().split())

# 노드 별 진입 차수의 수 기록 테이블
INDEGREE = [0] * (V + 1)

# 노드 별 다른 노드와의 연결 정보(간선) 기록 리스트
GRAPH = [[] for _ in range(V + 1)]

# 방향 그래프의 모든 간선 정보 및 도착 노드의 진입 차수 정보 입력
for _ in range(E):
    s, f = map(int, input().split())
    GRAPH[s].append(f)
    INDEGREE[f] += 1

# 위상 정렬
def topology_sort():
    result = []
    Q = deque()
    for v in range(1, V + 1):
        if INDEGREE[v] == 0:
            Q.append(v)

    while Q:
        current = Q.popleft()
        result.append(current)
        for near in GRAPH[current]:
            INDEGREE[near] -= 1
            if INDEGREE[near] == 0:
                Q.append(near)



