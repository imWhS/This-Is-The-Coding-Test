# 떡볶이 떡 만들기

# 자른 떡의 길이 총 합이 M과 같거나, 가장 근접한 값이 나오게 하는 H를 구하기 위해 이진 탐색한다.
def binary_search(array, target, start, end):
    print(f"binary_search(start: {start}, end: {end})", end = " ")

    if start > end:
        # 더 이상 H 값을 구할 수 없어, 절단기 높이 또한 도출할 수 없기 때문에 None을 반환하며 종료한다.
        return None

    # 새 H 값을 계산해, 더 나은 H가 존재하는지 확인한다.
    H = (start + end) // 2

    sum, tmp_sum = 0, 0
    for a in array:
        if a - H > 0:
            sum += (a - H)

    if sum == M:
        # 절단기 높이를 H로 정한 후 자른 떡의 길이 총 합이 M과 같다면 H 값을 반환하면서 종료한다.
        return H

    '''
    자른 떡의 총 합이 M과 같지 않다면, M과 같은 값 혹은 더 나은 값을 찾을 때까지 한 방향으로 이진 탐색을 추가 진행해야 한다.
    단, 이진 탐색을 추가 진행함으로써 발견한 더 나은 값을 반영해야 하기 때문에, 현재 단계의 H 값과 추가 진행한 이진 탐색 과정에서 나온 sum 값을 비교해야 한다.
    '''

    if sum > M:
        # 자른 떡의 길이 총 합이 M보다 더 크다면, 자른 떡의 길이 총 합을 줄이기 위해 H 값을 높인 후 이진 탐색을 계속 진행한다.
        return binary_search(array, target, H + 1, end)

    elif sum < M:
        # 자른 떡의 길이 총 합이 M보다 더 작다면, 자른 떡의 길이 총 합을 늘리기 위해 H 값을 줄인 후 이진 탐색을 계속 진행한다.
        return binary_search(array, target, start, H - 1)

N, M = map(int, input().split())
array = list(map(int, input().split()))

'''
보다 나은 성능을 위해, 절단기 높이 H를 가장 오른쪽에서부터 순차 탐색하지 않고
중간 값을 도출한 후, 조건과 부합하는지에 대한 yes, no 결과에 따라 왼쪽과 오른쪽 방향 중 한 방향으로만 이진 탐색한다.
'''

print(binary_search(array, M, 0, max(array)))