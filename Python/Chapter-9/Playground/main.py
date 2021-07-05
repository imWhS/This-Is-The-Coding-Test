'''
QUICK SORT
- AVERAGE O(NlogN)
- WORST O(N^2)
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if (start < end) == False:
        return

    pivot = start
    left, right = start + 1, end

    # left, right가 엇갈리는 경우도 발생할 수 있기 때문에, 이를 고려해 left가 right의 '이하' 조건으로 설정
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] <= array[right]:
            right -= 1

        # 다 이동하고 봤더니, left보다 오른쪽에 있어야 할 right가 더 왼쪽에 있는 경우(엇갈리는 경우)
        if right < left:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

print(array)


# '''
# INSERTION SORT
#
# - WORST O(N^2)
# - BEST O(N)
#
# 6 7 9 0 3
# '''
#
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j - 1] <= array[j]:
#             break
#         array[j - 1], array[j] = array[j], array[j - 1]
#
#
#
# print(array)


# '''
# SELECTION SORT
# - O(N^2)
# '''
#
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# for i in range(len(array)):
#     minimum = i
#     for j in range(i + 1, len(array)):
#         if array[j] < array[minimum]:
#             minimum = j
#     array[i], array[minimum] = array[minimum], array[i]
#
# print(array)


# '''
# Floyd-Marshall의 최단 거리 알고리즘
# '''
#
# INF = 1e9
# N, M = map(int, input().split())
# GRAPH = [[INF] * (N + 1) for _ in range(N + 1)]
# for i in range(N + 1):
#     for j in range(N + 1):
#         if i == j:
#             GRAPH[i][j] = 0
# for m in range(M):
#     a, b = map(int, input().split())
#     GRAPH[a][b] = 1
#     GRAPH[b][a] = 1
# X, K = map(int, input().split())
#
# #Floyd-Marshall's ALGORITHM
#
# for i in range(N + 1):
#     for a in range(N + 1):
#         for b in range(N + 1):
#             GRAPH[a][b] = min(GRAPH[a][b], GRAPH[a][i] + GRAPH[i][b])
#
# print(f"1번 회사에서 K 회사로 이동하는 최단 거리: {GRAPH[1][K]}")
# print(f"K 회사에서 X 회사로 이동하는 최단 거리: {GRAPH[K][X]}")
#
# if INF <= GRAPH[1][K] + GRAPH[K][X]:
#     print("-1")
# else:
#     print(GRAPH[1][K] + GRAPH[K][X])
#
#
#
# # '''
# # Dijkstra의 최단 거리 알고리즘 - PRIORITY QUEUE
# # '''
# #
# # import heapq
# #
# # INF = 1e9
# # N, M, C = map(int, input().split())
# # GRAPH = [[] for _ in range(N + 1)]
# # for _ in range(M):
# #     X, Y, Z = map(int, input().split())
# #     GRAPH[X].append((Y, Z))
# #
# # DISTANCE = [INF] * (N + 1)
# #
# # def dijkstra(C):
# #     Q = []
# #     heapq.heappush(Q, (0, C))
# #     DISTANCE[C] = 0
# #
# #     while Q:
# #         current_distance, current_node = heapq.heappop(Q)
# #
# #         if DISTANCE[current_node] < current_distance:
# #             continue
# #
# #         for near in GRAPH[current_node]:
# #             near_distance, near_node = current_distance + near[1], near[0]
# #             if DISTANCE[near_node] <= near_distance:
# #                 continue
# #             DISTANCE[near_node] = near_distance
# #             heapq.heappush(Q, (near_distance, near_node))
# #
# # dijkstra(C)
# #
# # cnt, maximum = 0, 0
# # for d in DISTANCE:
# #     if 0 < d < INF:
# #         cnt += 1
# #         if maximum < d:
# #             maximum = d
# #
# # print(f"모든 도시로 전달하는 데까지 걸린 시간: {maximum}, 전달한 도시의 수: {cnt}")
# #
# # # '''
# # # Dijkstra의 최단 경로 알고리즘 - EASY
# # # '''
# # #
# # # INF = 1e9
# # #
# # # # 정점의 수 N, 간선의 수 M
# # # N, M = map(int, input().split())
# # #
# # # # 시작 노드 start
# # # start = int(input())
# # #
# # # # 그래프
# # # GRAPH = [[] for _ in range(N + 1)]
# # # for _ in range(M):
# # #     s, f, d = map(int, input().split())
# # #     GRAPH[s].append((f, d))
# # #
# # # # 방문 여부 기록 리스트
# # # VISITED = [False] * (N + 1)
# # #
# # # # 최단 거리 테이블
# # # DISTANCE = [INF] * (N + 1)
# # #
# # # def find_nearest():
# # #     # 최단 거리 테이블 전 범위에서 방문하지 않은 노드 중 가장 최단 거리인 노드 번호를 반환
# # #     nearest_node, nearest_distance = 0, 0
# # #
# # #     for current_node in range(1, N + 1):
# # #         current_distance = DISTANCE[current_node]
# # #
# # #         if VISITED[current_node] or nearest_distance >= current_distance:
# # #             continue
# # #
# # #         nearest_node, nearest_distance = current_node, current_distance
# # #
# # #     return nearest_node
# # #
# # #
# # #
# # # def dijkstra(start):
# # #     VISITED[start] = True
# # #     DISTANCE[start] = 0
# # #
# # #     for near in GRAPH[start]:
# # #         DISTANCE[near[0]] = near[1]
# # #
# # #     for _ in range(N - 1):
# # #         current = find_nearest()
# # #         VISITED[current] = True
# # #
# # #         for near in GRAPH[current]:
# # #             if DISTANCE[near[0]] <= DISTANCE[current] + near[1]:
# # #                 continue
# # #
# # #             DISTANCE[near[0]] = DISTANCE[current] + near[1]
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # ''' Dijkstra의 최단 경로 알고리즘 정리 '''
# # #
# # # '''
# # # Dijkstra의 최단 경로 알고리즘 - HEAP을 이용한 PRIORITY QUEUE VERSION
# # #
# # # 특징
# # # - 방문하지 않았으면서 가장 가까운 노드의 번호를 순차 탐색하지 않고, 우선 순위 큐로 빠르게 알아낼 수 있도록 개선
# # # - 우선 순위 큐에는 방문하지 않은 노드만 enqueue 되고, 방문한(할) 노드는 dequeue 되기 때문에, 기존 VISITED 리스트를 우선 순위 큐로 대체
# # #
# # # 필수 자료 구조
# # # - GRAPH: 노드와 노드 사이의 간선 존재 여부를 기록해 그래프로 구현한 리스트
# # # - Q: HEAP을 이용해 거리가 가까운 노드부터 빠르게 탐색할 수 있게 하는 우선 순위 큐를 구현하기 위한 자료 구조
# # #      (노드 번호, 거리) 튜플 타입으로 관리
# # # - DISTANCE: 시작 노드부터 1번이라도 방문한 노드까지의 거리를 업데이트하며 최단 거리 테이블을 구현한 리스트
# # # '''
# # #
# # # import sys
# # # import heapq
# # #
# # # # 무한대 상수
# # # INF = 1e9
# # #
# # # # 그래프를 구성하는 노드의 수 N, 간선의 수 M
# # # N, M = map(int, input().split())
# # #
# # # # 시작 노드 번호
# # # start = int(input().split())
# # #
# # # # 1번부터 N번까지 존재할 노드 별 간선 정보(시작 노드 번호, 끝 노드 번호, 노드 간 거리)를 입력받아 그래프 구현
# # # GRAPH = [[] for _ in range(N + 1)]
# # # for _ in range(N + 1):
# # #     s, f, d = map(int, input().split())
# # #     GRAPH[s].append((f, d))
# # #
# # # # 최단 거리 테이블
# # # DISTANCE = [INF] * (N + 1)
# # #
# # # def dijkstra(start):
# # #     # 우선 순위 큐를 위한 리스트
# # #     Q = []
# # #
# # #     # 시작 노드를 방문 처리하며 초기화
# # #     heapq.heappush(Q, (0, start))
# # #     DISTANCE = [0]
# # #
# # #     # 더 이상 우선순위 큐에 enqueue 할 노드가 없을 때까지 다른 노드들을 가까운 거리 순으로 방문
# # #     while Q:
# # #         current_distance, current = heapq.heappop(Q)
# # #
# # #         # 인접 노드 접근 전, 기존 enqueue 시점에 의해 이미 INF가 아닌, 현재보다 더 최단 거리가 기록되어 있는 경우 다른 데이터를 enqueue
# # #         if DISTANCE[current] < current_distance:
# # #             continue
# # #
# # #         # 인접 노드 접근
# # #         for near in GRAPH[current]:
# # #             tmp_distance = DISTANCE[current] + near[1]
# # #
# # #             if tmp_distance < DISTANCE[near[0]]:
# # #                 DISTANCE[near[0]] = tmp_distance
# # #                 heapq.heappush(Q, (tmp_distance, near[0]))
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # '''
# # # Dijkstra의 최단 경로 알고리즘 - O^2 VERSION
# # #
# # # 필수 자료 구조
# # # - GRAPH: 노드와 노드 사이의 간선 존재 여부를 기록해 그래프를 구현한 리스트
# # # - VISITED: 기존 방문 여부를 노드 별로 저장할 수 있는 리스트
# # # - DISTANCE: 시작 노드부터 1번이라도 방문한 노드까지의 거리를 업데이트하며 최단 거리 테이블을 구현한 리스트
# # # '''
# # #
# # # # # 무한대 상수
# # # # INF = int(1e9)
# # # #
# # # # # 그래프를 구성하는 노드의 수 N, 간선의 수 M
# # # # N, M = map(int, input().split())
# # # #
# # # # # 시작 노드의 번호
# # # # start = int(input())
# # # #
# # # # # 1번부터 N번까지 존재할 노드 별 간선 정보(시작 노드 번호, 끝 노드 번호, 노드 간 거리)를 입력받아 그래프 구현
# # # # GRAPH = [[] for _ in range(N + 1)]
# # # # for _ in range(M):
# # # #     s, f, d = map(int, input().split())
# # # #     GRAPH[s].append((f, d))
# # # #
# # # # # 노드 별 방문 여부 저장
# # # # VISITED = [False] * (N + 1)
# # # #
# # # # # 최단 거리 테이블
# # # # DISTANCE = [INF] * (N + 1)
# # # #
# # # # # VISITED, DISTANCE를 이용해 방문하지 않았으면서 가장 가까운 인접 노드 번호 반환
# # # # def find_nearest():
# # # #     nearest, nearest_distance = 0, INF
# # # #
# # # #     for i in range(N + 1):
# # # #         if VISITED[i]:
# # # #             continue
# # # #         if DISTANCE[i] < nearest_distance:
# # # #             nearest, nearest_distance = i, DISTANCE[i]
# # # #
# # # #     return nearest
# # # #
# # # #
# # # # def dijkstra(start):
# # # #     # 시작 노드를 방문 처리하며 초기화
# # # #     VISITED[start] = True
# # # #     DISTANCE[start] = 0
# # # #
# # # #     # GRAPH를 이용해 초기화와 동시에 방문 처리한 시작 노드와 인접한 노드 번호 탐색
# # # #     # 시작 노드와 인접한 노드의 '시작 노드에서부터의 거리'를 구한 후, 최단 거리 테이블 업데이트
# # # #     for near in GRAPH[start]:
# # # #         DISTANCE[near[0]] = near[1]
# # # #
# # # #     # 방문하지 않았으면서, 가장 가까운 인접 노드를 찾은 후, '해당 노드에서부터 인접 노드까지의 거리'를 구한 값으로 최단 거리 테이블 업데이트
# # # #     # 시작 노드를 제외한 나머지 노드 N - 1개 모두 반드시 한 번 방문 처리 필요
# # # #     for _ in range(N - 1):
# # # #         current = find_nearest()
# # # #         VISITED[current] = True
# # # #
# # # #         # 현재 노드의 인접 노드 탐색 후, 해당 노드로부터의 거리를 구한 값으로 최단 거리 테이블 업데이트
# # # #         for near in GRAPH[current]:
# # # #             tmp_distance = DISTANCE[current] + near[1]
# # # #             if tmp_distance < DISTANCE[near[0]]:
# # # #                 DISTANCE[near[0]] = tmp_distance
# # #
# # #
# # #
# # #
