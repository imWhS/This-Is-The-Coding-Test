'''
SELECTION SORT
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort():
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum, j = j, minimum
        array[minimum], array[i] = array[i], array[minimum]


selection_sort()
print(array)