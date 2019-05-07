'''
jobs	                            return
[[0, 3], [1, 9], [2, 6]]	    9

'''


import heapq

def solution(jobs):

    answer = 0
    heap = []
    elapsedTime = 0
    elapsedList = []

    for i in range(len(jobs)):
        heapq.heappush(heap, jobs[i][1])
        
    heapq.heapify

    for j in range(len(heap)):
        elapsedTime += heapq.heappop(heap)
        elapsedSelf = elapsedTime - jobs[j][0]
        elapsedList.append(elapsedSelf)

    answer = sum(elapsedList)//len(jobs)

    return print(answer)


solution([[0, 3], [1, 9], [2, 6]])