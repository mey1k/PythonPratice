'''
scoville	                    K	    return
[1, 2, 3, 9, 10, 12]	    7	    2

'''
#def leftChild(index):
#    return index*2

#def rightChild(index):
#    return index*2+1

#def parent(index):
#    return index//2

#def minInsert(array, value):
#    array.append(value)
#    lastIndex = len(array)
#    while lastIndex > 1:
#        parentIndex = parent(lastIndex)
#        if array[lastIndex-1] < array[parentIndex-1]:
#            array[lastIndex-1], array[parentIndex-1] = array[parentIndex-1], array[lastIndex-1]
#            lastIndex = parentIndex
#        else:
#            break

#def minHeapify(array, index):
#    left = leftChild(index)
#    right = rightChild(index)
#    smallest = index
#    if left <= len(array) and array[left-1] < array[smallest-1]: #주의
#        smallest = left
#    if right <= len(array) and array[right-1] < array[smallest-1]:
#        smallest = right
#    if smallest != index:
#        array[index-1], array[smallest-1] = array[smallest-1], array[index-1]
#        minHeapify(array, smallest)

#def createHeapTree(array):
#    for index in range(len(array)//2, 0, -1):
#        minHeapify(array,index)

#def popMinValue(array):
#    array[0], array[-1] = array[-1], array[0]
#    value = array.pop(-1)
#    minHeapify(array,1)

#    return value

#def getMinValue(array):
#    return array[0]

#def mixDishes(array, k):
#    answer = 0 
#    while 1:
#        try:
#             newDishValue = popMinValue(array) + popMinValue(array)*2
#             minInsert(array,newDishValue)
#             answer += 1
#             if getMinValue(array) >= k:
#                 return answer
#        except:
#             return -1

#def solution(scoville, k):
     
#    createHeapTree(scoville)
#    answer = mixDishes(scoville, k)

#    return print(answer)

import heapq

def mixDishes(array, k):
    answer = 0 
    while 1:
        try:
             newDishValue = heapq.heappop(array) + heapq.heappop(array)*2
             heapq.heappush(array, newDishValue)
             answer += 1
             if array[0] >= k:
                 return answer
        except:
             return -1

def solution(array, k):
    
    heapq.heapify(array)
    answer = mixDishes(array, k)
    
    return answer

solution(	[1, 2, 3, 9, 10, 12], 7)