'''
Fluyd-Warshall 알고리즘

특징
- 특정 노드에서 중간 노드를 거쳐 다른 노드로 향할 때의 거리가
  초기 GRAPH에 기록된, 특정 노드에서 다른 노드로 향하는 거리보다 더 짧으면
  중간 노드로 거칠 때의 최단 거리로 GRAPH를 업데이트한다.

필수 자료 구조
- GRAPH: 모든 노드에 대해 다른 모든 노드까지의 거리 정보를 담기 위한 2차원 리스트
'''

# 무한대 상수
INF = 1e9

# 그래프를 구성하는 노드의 수 N, 간선의 수 M
N, M = map(int, input().split())

# 1번부터 N번까지 존재 노드와 다른 노드를 연결하는 간선의 정보를 포함하는 그래프를 2차원 리스트로 구현
GRAPH = [[INF] * (N + 1) for _ in range(N + 1)]

# 그래프에서 같은 노드 사이의 거리를 0으로 초기화
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            GRAPH[i][j] = 0

# 1번부터 N번까지 존재할 노드 별 간선 정보(시작 노드 번호, 끝 노드 번호, 노드 간 거리)를 입력받아 2차원 리스트로 그래프 구현
for _ in range(M):
    s, f, d = map(int, input().split())
    GRAPH[s][f] = d

# Floyd-Warshall 알고리즘
for i in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            GRAPH[a][b] = min(GRAPH[a][b], GRAPH[a][i] + GRAPH[i][b])
