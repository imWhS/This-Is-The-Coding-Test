# array에 대한 특정 값 target 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) / 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, mid + 1, end)
    elif target < array[mid]:
        return binary_search(array, start, mid - 1)























# def binary_search(array, target, start ,end):
#     if start > end:
#         return None
#
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif target < array[mid]:
#         return binary_search(array, target, start, mid - 1)
#     elif array[mid] < target:
#         return binary_search(array, target, mid + 1, end)
#
#




# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# #SELECTION SORT
# for i in range(len(array)):
#     minimum = i
#     for j in range(i, len(array)):
#         if array[minimum] > j:
#             minimum = j
#     array[i], array[minimum] = array[minimum], array[i]
#
# #INSERTION SORT
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j - 1] > array[j]:
#             array[j - 1], array[j] = array[j], array[j - 1]
#         else:
#             break
#
# #QUICK SORT
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     pivot, left, right = start, start + 1, end
#
#     #left, right 엇갈릴 수도 있는 경우의 수를 위해 =를 추가해야 한다.
#     while left <= right:
#         #left는 end 이하의 위치까지 움직일 수 있는데, pivot보다 작은 수에 있는 경우 한 칸 이동할 명분이 생긴다.
#         while left <= end and array[pivot] > array[left]:
#             left += 1
#         #rignt는 start + 1 이상의 위치까지 움직일 수 있는데, pivot보다 큰 수에 있는 경우 한 칸 이동할 명분이 생긴다.
#         while start < right and array[pivot] < array[right]:
#             right -= 1
#         #left, right가 움직인 후 엇갈렸다면 right와 pivot을 swap 한다.
#         if right < left:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             #엇갈리지 않았다면 left, right를 swap 한다.
#             array[left], array[right] = array[right], array[left]
#
#     #분할한다.
#     quick_sort(array, start + 1, right - 1)
#     quick_sort(array, right + 1, end)
#
#
