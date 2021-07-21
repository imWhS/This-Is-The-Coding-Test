'''
Dijkstra's SHORTEST ROUTE ALGORITHM
- HEAP VER.
'''

import heapq

INF = 1e9

# 그래프를 구성하는 정점 및 간선의 수 입력
N, M = map(int, input().split())

# 다른 모든 노드까지의 거리를 알아내고자 하는 시작 정점 번호 입력
first_node = int(input())

# 정점 간 연결 정보인 간선 데이터를 저장하기 위한 리스트
GRAPH = [[] for _ in range(N + 1)]

# 간선 데이터(시작 정점, 끝 정점, 두 정점 사이 거리 비용) 입력
for _ in range(M):
    start_node, end_node, distance = map(int, input().split())
    GRAPH[start_node].append((start_node, end_node))

# 최단 거리 테이블 데이터를 저장하기 위한 리스트
DISTANCE = [INF] * (N + 1)

def dijkstra(first_node):
    # HEAP 자료 구조
    Q = []

    # 자기 자신이어서 거리가 무조건 0인 시작 정점으로부터 HEAP에 삽입
    DISTANCE[first_node] = 0
    heapq.heappush(Q, (DISTANCE[first_node], first_node))

    # HEAP의 PRIORITY QUEUE에서 최단 거리를 조사할 정점이 더 이상 없을 때까지 반복
    while Q:
        # HEAP을 이용해 가장 거리 비용이 적은 정점을 추출해 현재 정점으로 지정
        current_node, current_dist = heapq.heappop(Q)

        # 삽입 순서에 상관 없이 거리 비용이 적은 순으로 추출되는 HEAP의 특성 상, 현재 정점이 이전에 이미 최소 한 번 추출되었고, 당시 조사한 최단 거리가 현재보다 더 적을 수밖에 없다면 다음 노드 조사
        if DISTANCE[current_node] < current_dist:
            continue

        # 현재 정점의 최단 거리를 이용해 인접 정점의 최단 거리도 계산하기 위해 인접 정점을 하나 씩 탐색해 조사
        for near in GRAPH[current_node]:
            # 인접 정점의 정보를 추출
            near_node, near_dist = near

            # 현재 정점을 거친 인접 정점까지의 거리 계산
            current_to_near_dist = current_dist + near_dist

            # 현재 정점을 거친 인접 정점까지의 거리가 기존 기록된 인접 정점까지의 거리보다 더 짧을 경우에만 최단 거리 테이블 업데이트 및 HEAP에 삽입
            if current_to_near_dist >= DISTANCE[near_node]:
                continue

            DISTANCE[near_node] = current_to_near_dist
            heapq.heappush(Q, (current_to_near_dist, near_node))

