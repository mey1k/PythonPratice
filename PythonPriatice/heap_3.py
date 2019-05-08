'''
jobs	                            return
[[0, 3], [1, 9], [2, 6]]	    9

'''


#import heapq

#def solution(jobs):

#    answer = 0
#    heap = []
#    workingTime = 0
#    elapsedList = []
#    sortedList = []

#    for i in range(len(jobs)):
#        heapq.heappush(heap, (jobs[i][1], jobs[i][0]))


#    while heap:
#        elapsedTime, startTime = heapq.heappop(heap)
#        workingTime += elapsedTime
#        elapsedSelf = workingTime - startTime
#        if elapsedSelf > 0:
#            elapsedList.append(elapsedSelf)

#    answer = sum(elapsedList)//len(jobs)

#    return print(answer)


#solution([[0, 3], [1, 9], [2, 6], [4, 3]])

from heapq import heappush, heappop
import random

def solution1(jobs):
    jobs.sort(key=lambda x: x[0], reverse=True)
    nums = len(jobs)
    workingTime = 0
    heap = []
    time = 0

    while jobs:
        while jobs and jobs[-1][0] <= time:
            start, duration = jobs.pop()
            heappush(heap, (duration, start))
        if not heap:
            start, duration = jobs.pop()
            heappush(heap, (duration, start))
            time = start
        duration, start = heappop(heap)
        print([duration,start])
        time += duration
        workingTime += time - start
    
    while heap:
        duration, start = heappop(heap)
        print([duration,start])
        time += duration
        workingTime += time - start

    return print(workingTime//nums)

def solution2(jobs):
    jobs.sort(key=lambda x: x[0])
    nums = len(jobs)
    workingTime = 0
    heap = []
    time = 0

    while jobs:
        while jobs and jobs[0][0] <= time:
            start, duration = jobs.pop(0)
            heappush(heap, (duration, start))
        if not heap:
            start, duration = jobs.pop(0)
            heappush(heap, (duration, start))
            time = start
        duration, start = heappop(heap)
        print([duration,start])
        time += duration
        workingTime += time - start
    
    while heap:
        duration, start = heappop(heap)
        print([duration,start])
        time += duration
        workingTime += time - start

    return print(workingTime//nums)

#jobs = []

#for _ in range(10):
#    jobs.append([random.randint(1,50), random.randint(1,50)])

#jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
#jobs = [[34,15],[2,15],[26,1]]

print(jobs)

solution1(jobs.copy())
solution2(jobs.copy())
