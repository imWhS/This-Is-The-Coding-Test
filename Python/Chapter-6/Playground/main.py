'''
Playground of Sorting Algorithm
'''



'''
QUICK SORT
- NORMAL: O(N logN)
- WORST: O(N^2)
'''

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot, left = start, start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] <= array[right]:
            right -= 1

        if right < left:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)



'''
INSERTION SORT
- WORST: O(N^2)
- BEST: O(N)
'''

def insertion_sort():
    for i in range(1, len(ARRAY)):
        for j in range(i, 0, -1):
            if ARRAY[j] < ARRAY[j - 1]:
                ARRAY[j], ARRAY[j - 1] = ARRAY[j - 1], ARRAY[j]
            else:
                break



'''
SELECTION SORT
- O(N^2)
'''

def selection_sort():
    for i in range(len(ARRAY)):
        min = i
        for j in range(i + 1, len(ARRAY)):
            if ARRAY[j] < ARRAY[min]:
                min = j
        ARRAY[i], ARRAY[min] = ARRAY[min], ARRAY[i]
