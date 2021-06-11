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

#방향 별 이동 정보: 0 U, 1 R, 2 D, 3 L
rotate = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(f"초기 방향: ({r + rotate[d][0]}, {c + rotate[d][1]})")

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

r_cnt = 0
nd = d

while 1:
    print(f"현재 위치: ({r}, {c})")
    #왼쪽 방향 회전 -> visited 확인 -> 가보지 않은 칸이라면 한 칸 전진 -> 가 본 칸이라면 왼쪽 방향 추가 회전
    nd = (d - 1) % 4
    r_cnt += 1

    #회전한 방향의 지점 좌표 계산
    nr, nc = r + rotate[nd][0], c + rotate[nd][1]
    # tmp = input()
    print(f"회전 후 방향: ({nr}, {nc})")


    #가 본 칸이거나 바다라면 다시 회전
    if (visited[nr][nc] == 1) or (game_map[nr][nc] == 1):
        print("- 가본 칸이거나 바다 ")
        #이미 4 방향 모두 회전한 상태였다면, 한 칸 뒤로 후진 먼저 한 후 다시 회전해야 한다.
        if r_cnt == 3:
            print("  - 4 방향 모두 회전")
            nr, nc = r - rotate[d][0], c - rotate[d][1]
            #한 칸 뒤로 후진할 수 없는 경우 움직임을 멈춘다.
            if nr < 0 or nc < 0 or nr > 4 or nc > 4:
                break
            r, c = nr, nc
            r_cnt = 0

        #다시 회전한다.
        continue

    #가보지 않은 칸이라면 해당 방향으로 한 칸 전진
    r, c = nr, nc
    visited[r][c] = 1
    r_cnt = 0
    d = nd





