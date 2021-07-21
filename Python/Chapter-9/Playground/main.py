'''
Playground of Shortest Path
'''

'''
Dijkstra's Shortest Path Algorithm
- O(E logV)
'''

import heapq

INF = 1e9
N, M = map(int, input().split())
GRAPH = [[] for _ in range(N + 1)]
DISTANCE = [INF] * (N + 1)

first = int(input())

for _ in range(M):
    start, end, distance = map(int, input().split())
    GRAPH[start].append(end, distance)

def dijkstra(first):
    Q = []
    DISTANCE[first] = 0
    heapq.heappush(Q, (0, first))

    while Q:
        current_dist, current = heapq.heappop(Q)

        if DISTANCE[current] < current_dist:
            continue

        for node in GRAPH[current]:
            near, current_to_near_dist = node
            if current_dist + current_to_near_dist < DISTANCE[near]:
                DISTANCE[near] = current_dist + current_to_near_dist
                heapq.heappush(Q, (current_dist + current_to_near_dist, near))



'''
Floyd-Warshall's Shortest Path Algorithm
- O(N^3)
'''

INF = 1e9
N, M = map(int, input().split())
GRAPH = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            GRAPH[i][j] = 0

for _ in range(M):
    start, end, distance = map(int, input().split())
    GRAPH[start][end] = distance

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            GRAPH[i][j] = min(GRAPH[i][j], GRAPH[i][k] + GRAPH[k][j])

