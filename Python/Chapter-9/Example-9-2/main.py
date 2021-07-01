# Dijkstra의 최단 경로 알고리즘 - HARD

import sys
import heapq

input = sys.stdin.readline



INF = int(1e9)
N, M = map(int, input().split())
start = int(input())

graph = [[] for _ in range(0, N + 1)]
for _ in range(M):
    s, f, d = map(int, input().split())
    graph[s].append((f, d))

distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        currentDist, currentNode = heapq.heappop(q)

        #INF가 아니거나(INF보다 낮은 값은 최소 한 번 방문한 노드), 기존 기록된 거리 값보다 낮지 않으면 처리 할 필요 없다.
        if distance[currentNode] < currentDist:
            continue

        #인접한 노드들을 살펴본다.
        for near in graph[currentNode]:
            cost = currentDist + near[1]
            if distance[near[0]] <= cost:
                continue
            distance[near[0]] = cost
            heapq.heappush(q, (cost, near[0]))



