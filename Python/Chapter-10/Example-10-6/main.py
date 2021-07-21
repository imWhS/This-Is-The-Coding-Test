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

# 노드와 간선의 수 입력
V, E = map(int, input().split())

# 그래프를 구성하는 노드 별 연결 정보 저장 리스트
GRAPH = [[] for _ in range(V + 1)]

# 노드 별 진입 차수 정보 저장 리스트
INDEGREE = [0] * (V + 1)

# 노드 별 연결 정보 입력
for _ in range(E):
    start, end = map(int, input().split())
    GRAPH[start].append(end)
    INDEGREE[end] += 1

def topology_sort():
    result = []
    Q = deque()

    # 그래프를 구성하는 모든 노드를 순차 탐색
    for v in range(1, V + 1):
        # 진입 차수가 0인 노드를 Queue에 enqueue
        if INDEGREE[v] == 0:
            Q.append(v)

    # Queue가 빌 때까지 진입 차수가 0인 노드의 인접 노드 탐색
    while Q:
        current = Q.popleft()
        result.append(current)

        # 현재 노드와 인접 노드의 연결 해제를 위해 인접 노드의 진입 차수(현재 노드에서 출발하는) 1 감소 처리
        for near in GRAPH[current]:
            INDEGREE[near] -= 1

            # 1개 노드가 연결 해제된 인접 노드의 진입 차수가 0이 됐다면 Queue에 enqueue
            if INDEGREE[near] == 0:
                Q.append(near)
























# '''
# Topology Sort
# - 방향 그래프를 구성하는 모든 노드에 대해 미리 정해져있는 방향성을 지키면서 순서대로 나열하는 알고리즘
# - 진입 차수가 0인 노드를 먼저 Queue에 enqueue 하고, 인접 노드들의 진입 차수 또한 1 씩 감소시켜 연결을 끊었을 때 진입 차수가 0일 경우 enqueue 한다.
# - 이후 Queue로부터 dequeue 한 노드를 대상으로 Queue가 빌 때까지 반복한다.
#
# 필요 자료 구조
# - V: 정점의 수
# - E: 간선의 수
# - GRAPH: 노드 별 다른 노드와의 연결 정보
# - INDEGREE: 정점 별 진입 차수 정보
# - Queue
# '''
#
# from collections import deque
#
# V, E = map(int, input().split())
# GRAPH = [[] for _ in range(V + 1)]
# INDEGREE = [0] * (V + 1)
#
# # 방향 그래프를 구성하는 간선 정보 및 인접 노드의 진입 차수 정보 입력
# for e in range(E):
#     start, end = map(int, input().split())
#     GRAPH[start].append(end)
#     INDEGREE[end] += 1
#
# def topology_sort():
#     result = []
#     Q = deque()
#
#     for v in range(1, V + 1):
#         if INDEGREE[v] == 0:
#             Q.append(v)
#
#     while Q:
#         current = Q.popleft()
#         result.append(current)
#
#         for near in GRAPH[current]:
#             INDEGREE[near] -= 1
#             if INDEGREE[near] == 0:
#                 Q.append(near)
#
# topology_sort()