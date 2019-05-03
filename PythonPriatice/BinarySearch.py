# 비재귀적 이진탐색의 Python 코드
def binary_search (arr, val):
    first, last = 0, arr.len()
    while first<=last:
        mid = (first + last) // 2
        if arr[mid] == val: return mid
        if arr[mid] > val: last = mid-1
        else: first = mid+1
    return -1
