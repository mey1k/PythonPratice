'''
answers	        return
[1,2,3,4,5]	    [1]
[1,3,2,4,2]	    [1,2,3]

'''

def solution(answers):
    answer = []

    candidate1 = [1,2,3,4,5]
    candidate2 = [2,1,2,3,2,4,2,5]
    candidate3 = [3,3,1,1,2,2,4,4,5,5]

    index1 = 0
    index2 = 0
    index3 = 0

    score1 = 0
    score2 = 0
    score3 = 0

    scoreList = []

    for i in range(len(answers)):
        if index1 == 5:
            index1 = 0
        if index2 == 8:
            index2 = 0
        if index3 == 10:
            index3 = 0
        
        if answers[i] == candidate1[index1]:
            score1 += 1
        if answers[i] == candidate2[index2]:
            score2 += 1
        if answers[i] == candidate3[index3]:
            score3 += 1

        index1 += 1
        index2 += 1
        index3 += 1

    scoreList.append(score1)
    scoreList.append(score2)
    scoreList.append(score3)

    temp = [i for i,x in enumerate(scoreList) if x==max(scoreList)]

    for n in temp:
        answer.append(n+1)

    return answer

solution([1,3,2,4,2])