'''
Playground of Search
'''

'''
Sequential Search
'''

def sequential_search(n, target, array):
    for i in range(len(array)):
        if array[i] == target:
            return i

def binary_search(array, target, start, end):
    if end < start:
        return None

    mid = (start + end) // 2

    if array[mid] == array[target]:
        return mid

    # 찾는 값 target이 아니면서, mid보다 작은 경우
    if array[target] < array[mid]:
        return binary_search(array, target, start, mid - 1)

    elif array[mid] < array[target]:
        return binary_search(array, target, mid + 1, end)




