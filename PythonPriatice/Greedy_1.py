'''

n	    lost	    reserve	return
5	    [2, 4]	[1, 3, 5]	5
5	    [2, 4]	[3]	        4
3	    [3]	    [1]	        2

예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

'''

def isPossible(lostStudent, reserveStudents,lost):

    flag = False

    for n in reserveStudents:
        if n -1 == lostStudent:
            if n in lost:
                return False
            reserveStudents.remove(lostStudent+1)
            return True
        elif n +1 == lostStudent:
            reserveStudents.remove(lostStudent-1)
            return True
        elif n == lostStudent:
            reserveStudents.remove(lostStudent)
            return True

    return flag
    
def solution(n,lost,reserve):

    answer = n

    for i in range(len(lost)):
        if not isPossible(lost[i],reserve,lost):
            answer -= 1

    return print(answer)

solution(5,[2,4], [3,5])