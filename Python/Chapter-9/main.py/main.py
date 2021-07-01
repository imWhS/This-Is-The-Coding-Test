# 전보

'''
Example

input:
3 2 1
1 2 4
1 3 2

output:
2 4
'''

import heapq

INF = 1e9
N, M, C = map(int, input().split())
GRAPH = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    GRAPH[X].append((Y, Z))
DISTANCE = [INF] * (N + 1)

def dijkstra(C):
    Q = []

    # 메시지를 보내고자 하는 도시 C는 무조건 처음 전보를 받기 때문에 가장 먼저 방문 처리한다.
    DISTANCE[C] = 0
    heapq.heappush(Q, (0, C))

    # 도시 C를 제외한 남은 도시들을 모두 방문할 때까지 반복한다.
    while Q:

        # 도시 C로부터 가장 거리가 가까운 도시를 하나 방문한다.
        current_dist, current = heapq.heappop(Q)

        # 만약 이전에 이미 최소 한 번 방문한 도시면서, 당시의 거리가 더 짧을 경우 더 진행할 필요가 없기에 다른 도시를 방문한다.
        if DISTANCE[current] < current_dist:
            continue

        # 현재 방문 중인 도시를 거쳐 이동할 수 있는, 인접 도시들을 탐색한다.
        for near in GRAPH[current]:

            near_dist = current_dist + near[1]

            # 만약 이전에 이미 최소 한 번 방문한 인접 도시며 당시의 거리가 현재 방문 중인 도시를 거쳐갈 때보다 더 거리가 짧을 경우 다른 인접 도시를 탐색한다.
            if DISTANCE[near[0]] <= near_dist:
                continue

            DISTANCE[near[0]] = near_dist
            heapq.heappush(Q, (near_dist, near[0]))

dijkstra(C)

cnt_cities, maximum_time = 0, 0

for i in range(1, len(DISTANCE)):
    if DISTANCE[i] >= INF or i == C:
        continue

    if maximum_time < DISTANCE[i]:
        maximum_time = DISTANCE[i]

    cnt_cities += 1


print(f"{cnt_cities} {maximum_time}")



