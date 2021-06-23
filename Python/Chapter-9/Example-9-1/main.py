# Dijkstra의 최단 경로 알고리즘 - EASY

import sys

input = sys.stdin.readline
INF = int(1e9)

# N은 노드 수, M은 간선 수
N, M = map(int, input().split())

# 출발 노드 번호(최단 거리 측정 시작 노드 번호)
start = int(input())

# 노드 별 연결 정보(끝 노드 번호 e, 비용 d) 저장 그래프
graph = [[] for i in range(N + 1)]

# 노드 별 방문 여부 정보 저장 리스트
visited = [False] * (N + 1)

# 노드 별 최단 거리 테이블
distance = [INF] * (N + 1)

# 그래프에 노드 간 연결 정보 (간선) 입력
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

# 미 방문 노드들을 대상으로, 최단 거리 테이블을 탐색해 가장 최단 거리가 짧은 노드 번호를 반환하는 함수
def get_shortest_node():
    minimum = INF
    node = 0

    for i in range(0, N + 1):
        if visited[i] or distance[i] >= minimum:
            continue
        index, minimum = i, distance[i]

    return node

# Dijkstra의 최단 경로 알고리즘 함수
def dijkstra(start):
    # 시작 노드는 거리가 0이기에 무조건 방문 처리
    visited[start] = True
    distance[start] = 0

    # 방문한 시작 노드와 인접한 다른 노드로 가는 거리를 최단 거리 테이블에 반영
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 무조건 방문 처리된 시작 노드를 거쳐 방문할 다른 노드 n - 1개 탐색 시작
    for _ in range(N - 1):
        current = get_shortest_node()
        visited[current] = True

        # 최단 거리 테이블을 이용해 current 자신을 거쳐 인접한 노드들로 가기 위한 거리 비용 확인
        for i in graph[current]:
            cost = distance[current] + i[1]

            # 기존 거리 비용보다 더 적은 경우, 최단 거리 테이블에 반영
            if cost < distance[i[0]]:
                distance[i[0]] = cost

dijkstra(start)




