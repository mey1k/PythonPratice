#한글 git 옵션 utf-8로 변경 필요하다.
def parent(index):
    return index//2

def leftchild(index):
    return index*2

def rightchild(index):
    return index*2 + 1

def minInsert(array, n): # return minHeap
        array.append(n)
        lastIndex =  len(array) # Last index
        while lastIndex>1: #부모와 비교하며 올라가는 함수.
           parentIndex = parent(lastIndex) 
           if array[lastIndex-1] < array[parentIndex-1]: 
               array[lastIndex-1], array[parentIndex-1] = array[parentIndex-1], array[lastIndex-1]
               lastIndex = parentIndex
           else: # 만약 부모가 더 작으면 거기서 끝.
              break

def maxInsert(array, n): # return maxHeap
        array.append(n)
        lastIndex =  len(array) # Last index
        while lastIndex>1: #부모를 확인하면서 올라가는 함수
           parentIndex = parent(lastIndex) 
           if array[lastIndex-1] > array[parentIndex-1]: 
               array[lastIndex-1], array[parentIndex-1] = array[parentIndex-1], array[lastIndex-1]
               lastIndex = parentIndex
           else: # 만약 부모가 더 작으면 거기서 끝.
              break 

def minDelete(array):
    array[0], array[len(array) - 1] = array[len(array) - 1] , array[0] #마지막 원소와 root를 바꿔주고
    array.pop(len(array)-1) #마지막 원소를 제거한다.
    minHeapify(array, 1) #root index에서 heapify를 시작한다.

def maxDelete(array):
    array[0], array[len(array) - 1] = array[len(array) - 1] , array[0] #마지막 원소와 root를 바꿔주고
    array.pop(len(array)-1) #마지막 원소를 제거한다.
    maxHeapify(array, 1) #root index에서 heapify를 시작한다.

def minHeapify(array, index): #이 함수가 결국 자식들과 비교해 가면서 내려가는 함수입니다.
    left = leftchild(index)
    right = rightchild(index)
    smallest = index #일단은 가장 작은 것을 자신으로 놓고
    if left <= len(array) and array[left - 1] < array[smallest-1]: #만약 왼쪽 자식이 존재하고, 가장 작은 것보다 더 작으면
        smallest = left #가장작은 것은 왼쪽자식이 된다.
    if right <= len(array) and array[right - 1] < array[smallest-1]: #만약 오른쪽 자식도 존재하고, 그것이 현재까지 최소보다 더 작으면
        smallest = right #가장 작은 것은 오른쪽 자식
    if smallest != index: #만약 자신이 가장 작은 것이 아니면,
        array[index-1], array[smallest-1] = array[smallest-1], array[index-1] #자식들 중 가장 작은 것과 바꿔주고
        minHeapify(array, smallest) #recursive call을 하여 내려가서 다시 진행

def maxHeapify(array, index):
    left = leftchild(index)
    right = rightchild(index)
    biggest = index #일단은 가장 큰 것을 자신으로 놓고
    if left <= len(array) and array[left - 1] > array[biggest-1]: #만약 왼쪽 자식이 존재하고, 가장 큰 것보다 더 크면
        biggest = left #가장큰 것은 왼쪽자식이 된다.
    if right <= len(array) and array[right - 1] > array[biggest-1]: #만약 오른쪽 자식도 존재하고, 그것이 현재까지 최대보다 더 크면
        biggest = right #가장 큰 것은 오른쪽 자식
    if biggest != index: #만약 자신이 가장 큰 것이 아니면,
        array[index-1], array[biggest-1] = array[biggest-1], array[index-1] #자식들 중 가장 큰 것과 바꿔주고
        maxHeapify(array, biggest) #recursive call을 하여 내려가서 다시 진행

def minHeapCreate(array):
    for i in range(len(array)//2, 0, -1):
        minHeapify(array, i)

def maxHeapCreate(array):
    for i in range(len(array)//2, 0, -1):
        maxHeapify(array, i)

def maxHeapSort(array): # 최대값(우선순위), 최소값(우선순위), 우선순위 큐
    result = []

    maxHeapCreate(array)

    while array:
        array[0], array[len(array) - 1] = array[len(array) - 1] , array[0] #마지막 원소와 root를 바꿔주고
        result.append(array[-1]) # heap_Sort Result, O(nlogn)
        array.pop(len(array)-1) #마지막 원소를 제거한다.
        maxHeapify(array, 1) #root index에서 heapify를 시작한다.

    return result # 내림차순 결과 큐

def minHeapSort(array): # 최대값(우선순위), 최소값(우선순위), 우선순위 큐
    result = []
    
    minHeapCreate(array)

    while array:
        array[0], array[len(array) - 1] = array[len(array) - 1] , array[0] #마지막 원소와 root를 바꿔주고
        result.append(array[-1]) # heap_Sort Result, O(nlogn)
        array.pop(len(array)-1) #마지막 원소를 제거한다.
        minHeapify(1) #root index에서 heapify를 시작한다.

    return result # 오름차순 결과 큐

##############################################
##############################################

import random

array = []

for _ in range(10):
    maxInsert(array, random.randint(1,50))

print(array)
copyArray = array.copy()

for _ in range(10):
    maxDelete(array)
    print(array)

maxHeapCreate(copyArray)

print(copyArray)

print(maxHeapSort(copyArray))