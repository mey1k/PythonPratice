'''
operations  	        return
[I 16,D 1]  	            [0,0]
[I 7,I 5,I -5,D -1]	    [7,5]

'''

import heapq

def solution(operations):

    answer = []
    maxHeap = []
    minHeap = []

    for n in operations:
         words = n.split(" ")

         if words[0] == "I":
             heapq.heappush(minHeap,int(words[1]))
             heapq.heappush(maxHeap,(-int(words[1]),int(words[1])))
         elif int(words[1]) == 1 and minHeap:
             minHeap.remove(heapq.heappop(maxHeap)[1])
         elif minHeap:
             minValue = heapq.heappop(minHeap)
             maxHeap.remove((-minValue, minValue))

    if maxHeap:
       answer.append(heapq.heappop(maxHeap)[1])
    else:
       answer.append(0)
    
    if minHeap:
        answer.append(heapq.heappop(minHeap))
    else:
        answer.append(0)

    return print(answer)

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
