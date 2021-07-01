# 미래 도시

''''
Example 1
input:
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
result:
3

Test Case 2
input:
4 2
1 3
2 4
3 4
result:
-1

'''

INF = 1e9
N, M = map(int, input().split())
GRAPH = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            GRAPH[i][j] = 0

for _ in range(M):
    s, f = map(int, input().split())
    GRAPH[s][f] = 1
    GRAPH[f][s] = 1

X, K = map(int, input().split())

for i in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            GRAPH[a][b] = min(GRAPH[a][b], GRAPH[a][i] + GRAPH[i][b])

result = GRAPH[1][K] + GRAPH[K][X]
if result >= INF:
    result = -1

print(result)

