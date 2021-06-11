#왕실의 나이트

input_data = input()
r = int(input_data[1])
c = int(ord(input_data[0]) - ord('a') + 1)
cnt = int()

#수평2 수직1: 위1왼2 아래1왼2 위1오2 아래1오2
#수직2 수평1: 위2왼1 위2오1 아래2왼1 아래2오1
routes = [(-1, -2), (1, -2), (-1, 2), (1, 2),
          (-1, -1), (-2, 1), (2, -1), (2, 1)]

for route in routes:
    nr, nc = r + route[0], c + route[1]
    if nr < 1 or nc < 1 or nr > 8 or nc > 8:
        continue
    else:
        print(f"({nr}, {nc})")
        cnt += 1

print(cnt)