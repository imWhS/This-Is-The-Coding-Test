'''
BINARY SEARCH
'''

def binary_search(array, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    if target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, start)

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

