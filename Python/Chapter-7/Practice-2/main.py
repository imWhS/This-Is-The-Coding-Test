#부품 찾기

def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)


N = int(input())
storeParts = list(map(int, input().split()))

M = int(input())
customerParts = list(map(int, input().split()))

for m in range(M):
    result = binary_search(storeParts, customerParts[m], 0, N - 1)
    if result == None:
        print("no", end = " ")
    else:
        print("yes", end = " ")




