# Dijkstra의 최단 경로 알고리즘 - EASY

import sys
input = sys.stdin.readline

'''
INF: 무한 값 
N M: 노드의 수와 간선(노드에 대한 다른 노드와의 연결 관계)의 수
start: 시작 노드 번호

graph: 노드 별 간선에 의해 연결된 다른 노드 번호 정보 및 비용(거리) 기록 
visited: 노드 별 방문 여부 기록 
distance: 노드 별 최단 거리 테이블 
'''


INF = int(1e9)
N, M = map(int, input().split())
start = int(input())

# 노드 별 다른 노드와의 연결 정보를 입력받는다.
graph = [[] for i in range(0, N + 1)]
for _ in range(M):
    s, f, d = map(int, input().split()) # 시작 노드 번호, 시작 노드와 연결된 끝 노드 번호, 끝 노드까지의 비용
    graph[s].append((f, d))

#노드 별 방문 여부를 기록한다.
visited = [False] * (N + 1)

#최단 거리 테이블을 초기화한다.
distance = [INF] * (N + 1)

def get_nearest():
    minimumDistance = INF
    minimumNode = 0
    for i in range(1, N + 1):
        if distance[i] >= minimumDistance or visited[i]:
            continue

        minimumDistance, minimumNode = distance[i], i

    return minimumNode

def dijkstra(start):
    # 시작 노드는 무조건 방문하기 때문에, 방문 처리를 한 후 거리도 바로 기록한다.
    visited[start] = True
    distance[start] = 0

    # 시작 노드와 간선으로 바로 연결된 인접 노드들의 비용을 우선 기록한다.
    print(f"{start}번 노드의 인접 노드: ")
    for near in graph[start]:
        print(f"{near[0]}번 노드 - 거리 {near[1]}")
        distance[near[0]] = near[1]

    # 시작 노드를 제외한 남은 N - 1 개의 노드 중 최단 거리인 노드를 방문한 후 최단 거리 테이블을 기록한다.
    for _ in range(N - 1):
        # get_nearest()를 이용해 최단 거리 테이블에 거리가 기록된 노드 중 최단 거리인 노드 번호를 가져온 후 방문 처리한다.
        current = get_nearest()
        visited[current] = True

        # current 노드와 간선으로 바로 연결된 인접 노드들의 비용을 계산한 후, 최단 거리 테이블을 이용해 더 적은 비용이라면 테이블을 새로 업데이트한다.
        for near in graph[current]:
            cost = distance[current] + near[1]
            if cost < distance[near[0]]:
                distance[near[0]] = cost






#start 노드를 시작으로 Dijkstra 알고리즘을 실행한다.
dijkstra(start)

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''