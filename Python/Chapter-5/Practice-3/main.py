from collections import deque

#UP DOWN LEFT RIGHT
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


N, M = map(int, input().split())
ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input())))

visited = [[False] * M for _ in range(N)]
result = 0

def BFS(r, c):
    ice_map[r][c] = 1
    queue = deque()
    queue.append((r, c))

    while(queue):
        cr, cc = queue.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if ice_map[nr][nc]:
                continue

            ice_map[nr][nc] = 1
            queue.append((nr, nc))


for r in range(N):
    for c in range(M):
        if ice_map[r][c]:
            continue

        BFS(r, c)
        result += 1

print(result)
