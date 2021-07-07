'''
Topology Sort
- 방향 그래프를 구성하는 모든 노드에 대해 미리 정해져있는 방향성을 지키면서 순서대로 나열하는 알고리즘
- 진입 차수가 0인 노드를 먼저 Queue에 enqueue 하고, 인접 노드들의 진입 차수 또한 1 씩 감소시켜 연결을 끊었을 때 진입 차수가 0일 경우 enqueue 한다.
- 이후 Queue로부터 dequeue 한 노드를 대상으로 Queue가 빌 때까지 반복한다.

필요 자료 구조
- V: 정점의 수
- E: 간선의 수
- GRAPH: 노드 별 다른 노드와의 연결 정보
- INDEGREE: 정점 별 진입 차수 정보
- Queue
'''

from collections import deque

V, E = map(int, input().split())
GRAPH = [[] for _ in range(V + 1)]
INDEGREE = [0] * (V + 1)

# 방향 그래프를 구성하는 간선 정보 및 인접 노드의 진입 차수 정보 입력
for e in range(E):
    start, end = map(int, input().split())
    GRAPH[start].append(end)
    INDEGREE[end] += 1

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

topology_sort()