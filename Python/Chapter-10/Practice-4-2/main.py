'''
커리큘럼 - CODE B

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
import copy

N = int(input())
INDEGREE = [] * (N + 1)
LECTURE_GRAPH = [[] for _ in range(N + 1)]
LECTURE_TIME = [0] * (N + 1)

for n in range(1, N + 1):
    tmp_inputs = list(map(int, input().split()))
    LECTURE_TIME[n] = tmp_inputs[0]

    for t in tmp_inputs[1 : -1]:
        INDEGREE[n] += 1
        LECTURE_GRAPH[t].append(n)

def topology_sort():
    result = copy.deepcopy(LECTURE_TIME)
    Q = deque()

    for n in range(1, N + 1):
        if INDEGREE[n] == 0:
            Q.append(n)

    while Q:
        current = Q.popleft()

        for near in LECTURE_GRAPH[current]:
            if result[near] < result[current] + LECTURE_TIME[near]:
                result[near] = result[current] + LECTURE_TIME[near]
            INDEGREE[near] -= 1
            if INDEGREE[near] == 0:
                Q.append(near)
        



