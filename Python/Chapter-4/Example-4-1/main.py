#상하좌우

N = int(input())
route_plan = input().split()

#0 L, 1 R, 2 U, 3 D 이동 구현을 위한 route_types, dr, dc
d_route_types = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

r, c = 1, 1

for rp in route_plan:
    nr, nc = r + dr[d_route_types[rp]], c + dc[d_route_types[rp]]
    if nr < 1 or nc < 1 or nr > N or nc > N:
        continue
    r, c = nr, nc

print(r, c)