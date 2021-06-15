#게임 개발

N, M = map(int, input().split())
r, c, d = map(int, input().split())

#게임 맵 정보 입력
game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

#방문 정보 기록을 위한 맵 초기화
visited = [[0] * M for _ in range(N)]

#(0, 0) 시작 지점 방문 처리
visited[r][c] = 1
result = 1

#방향 별 이동 정보: 0 U, 1 R, 2 D, 3 L
rotate = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn():
    global d
    d = (d - 1) % 4

# 1단계: 현재 방향 d를 기준으로 왼쪽 방향으로 돌며 갈 곳 정한다.

while 1:
    is_avail = False

    for i in range(0, 3):
        turn()
        i += 1
        nr, nc = r + rotate[d][0], c + rotate[d][1]

        if nr < 0 or nc < 0 or nr > N or nc > M:
            continue

        if game_map[nr][nc]:
            continue

        if visited[nr][nc]:
            continue

        r, c = nr, nc
        visited[r][c] = 1
        is_avail = True
        result += 1
        break

    if is_avail:
        continue

    r, c = r - rotate[d][0], c - rotate[d][1]
    if r < 0 or c < 0 or r > N or c > M or game_map[r][c] or visited[r][c]:
        break


print(result)
















