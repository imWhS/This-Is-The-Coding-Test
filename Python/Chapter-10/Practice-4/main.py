'''
커리큘럼 - CODE A

inputs
N
lecture time, prerequisite lecture number

examples
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''


from collections import deque

N = int(input())
LECTURE_TIME = [0] * (N + 1)
LECTURE_PREREQUISITE = [[] for _ in range(N + 1)]

GRAPH = [[] for _ in range(N + 1)]
INDEGREE = [0] * (N + 1)

for n in range(1, N + 1):
    input_tmp = list(map(int, input().split()))


    LECTURE_TIME[n] = input_tmp[0]
    for i in range(1, len(input_tmp)):
        if input_tmp[i] == -1:
            break
        LECTURE_PREREQUISITE[n].append(input_tmp[i])
        GRAPH[input_tmp[i]].append(n)
        INDEGREE[n] += 1

for n in range(1, N + 1):
    print(f"{n} is connected: {GRAPH[n]}")
    print(f"  indegree: {INDEGREE[n]}")

#
# for n in range(1, N + 1):
#     print(f"time of {n}: {LECTURE_TIME[n]}")
#     print(" - prerequisites:", end = " ")
#     print(f"{LECTURE_PREREQUISITE[n]} (indegree: {len(LECTURE_PREREQUISITE[n])})")

result = [0] * (N + 1)
def topology_sort():
    course = []
    Q = deque()

    for n in range(1, N + 1):
        if INDEGREE[n] == 0:
            Q.append(n)

    while Q:
        current = Q.popleft()
        print(f"current studying: {current}")
        course.append(current)
        result[current] += LECTURE_TIME[current]
        print(f"time to end current lecture: {result[current]}")

        for near in GRAPH[current]:
            INDEGREE[near] -= 1
            print(f" - near lecture: {near}")
            print(f" - time to end near lecture: {result[near]} + {result[current]}")
            result[near] += result[current]

            if INDEGREE[near] == 0:
                Q.append(near)
                print(" - appended")


topology_sort()
