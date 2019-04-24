'''
progresses	speeds	return
[93,30,55]	    [1,30,5]	[2,1]
'''
def solution(progresses, speeds):
    answer = []
    workingDayList = []
    completedCount = 0
    index = 0
    pivotIndex = 0

    for n in range(len(progresses)):
        workingDayList.append((100-progresses[n]) // speeds[n] + 1)

    while index < len(workingDayList):
         if workingDayList[pivotIndex] < workingDayList[index]:
             answer.append(completedCount)
             completedCount = 0
             pivotIndex = index
             index -= 1
         else:
            completedCount += 1
           
         index += 1

    answer.append(completedCount)

    return print(answer)

#solution([93,30,55], [1,30,5])
#solution([95,50,1], [5,50,99])
#solution([0,50,2,4,40],[20,1,15,1,20])
#solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7])
#solution([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7])
solution([15, 1, 14, 9, 29, 25, 17, 24, 4, 27, 7, 19, 29, 14, 23, 4, 21, 3, 8, 14], [9, 11, 21, 16, 11, 21, 7, 5, 6, 30, 11, 24, 26, 18, 20, 18, 15, 30, 7, 18])

#def solution(progresses, speeds):
#    Q=[]
#    for p, s in zip(progresses, speeds):
#        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#            Q.append([-((p-100)//s),1])
#        else:
#            Q[-1][1]+=1
#    return print([q[1] for q in Q])

#solution([15, 1, 14, 9, 29, 25, 17, 24, 4, 27, 7, 19, 29, 14, 23, 4, 21, 3, 8, 14], [9, 11, 21, 16, 11, 21, 7, 5, 6, 30, 11, 24, 26, 18, 20, 18, 15, 30, 7, 18])