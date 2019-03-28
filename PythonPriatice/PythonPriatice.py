import datetime
from datetime import timedelta


#def solution(lines):
#    answer = 0
#    count = 0
#    newArr = []

#    for s in lines:

#        tempArr = s.split(' ')

#        tx = tempArr[0]+' '+tempArr[1]
#        t = timedelta(seconds=float(tempArr[2][:-1]))
#        dt = datetime.datetime.strptime(tx, "%Y-%m-%d %H:%M:%S.%f")

#        tempTuple = (dt-t+timedelta(seconds=0.001), dt)
#        newArr.append(tempTuple)
#    for k in range(2):
#        for j in range(len(newArr)):
#            threshold = newArr[j][k]
#            for i in range(len(newArr)):

#                if threshold > newArr[i][0] and threshold>newArr[i][1]:
#                    pass
#                elif threshold+timedelta(seconds=0.999) < newArr[i][0] and threshold+timedelta(seconds=0.999)<newArr[i][1]:
#                    pass
#                else:
#                    count += 1
#            answer = max(count,answer)
#            count = 0

#    return print(answer)


#lines =["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

#solution(lines)

def solution(lines):

    answer = 0

    tempAnswer = 0

    sectionTime = timedelta(seconds=0.999)

    for i in range(len(lines)):
        pickedLine = lines[i].split(' ')
        pickedDateTime = datetime.datetime.strptime(pickedLine[0]+' '+pickedLine[1],"%Y-%m-%d %H:%M:%S.%f")
        pickedDelay = timedelta(seconds=float(pickedLine[2][:-1])) - timedelta(seconds=0.001)

        for j in range(len(lines)):
            allLine = lines[j].split(' ')
            allDateTime = datetime.datetime.strptime(allLine[0]+' '+allLine[1],"%Y-%m-%d %H:%M:%S.%f")
            allDelay = timedelta(seconds=float(allLine[2][:-1])) - timedelta(seconds=float(0.001))

            if pickedDateTime + sectionTime < allDateTime - allDelay:
                continue
            #elif pickedDateTime + sectionTime < allDateTime - allDelay and pickedDateTime + sectionTime < allDateTime:
             #   continue
            elif pickedDateTime > allDateTime:
                continue
            #elif pickedDateTime > allDateTime - allDelay and pickedDateTime > allDateTime:
              #  continue
            else:
                tempAnswer +=1

        answer = max(answer,tempAnswer)
        tempAnswer = 0

    return print(answer)

lines =["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

#1:00:05.000
#1:00:05.001



solution(lines)