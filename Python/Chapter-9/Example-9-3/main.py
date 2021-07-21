'''
Floyd-Warshall's SHORTEST ROUTE ALGORITHM
'''

INF = 1e9

# 그래프를 구성하는 정점과 간선의 수 입력
N, M = map(int, input().split())

# 정점 간 연결 정보인 간선 정보를 저장하는 2차원 리스트
GRAPH = [[INF] * (N + 1) for _ in range(N + 1)]

# 2차원 리스트의 행 번호과 열 번호가 같은 원소를 모두 0으로 초기화
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            GRAPH[i][j] = 0

# 간선 정보 입력
for _ in range(M):
    start, end, distance = map(int, input().split())
    GRAPH[start][end] = distance

# Floyd-Warshall

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 정점 i에서 j로 바로 이동할 때의 거리보다 정점 k를 거쳐서 j로 이동할 떄의 거리가 더 가까우면 해당 거리를 최단 거리로 업데이트
            GRAPH[i][j] = min(GRAPH[i][j], GRAPH[i][k] + GRAPH[k][j])
