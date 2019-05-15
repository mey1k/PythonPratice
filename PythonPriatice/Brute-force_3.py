'''
baseball	                                                                return
[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	    2

'''
def isDuplicate(number):
    if len(number) > len(set(number)):
        return True
    else:
        return False

def checkShot(shot, number):

    strike = 0
    ball = 0

    for i in range(len(number)):
        if number[i] in shot:
            if i == shot.index(number[i]):
               strike += 1
            else:
                ball += 1

    return strike, ball

def solution(baseball):
    answer = 0

    number = 123

    while number != 988:
        if not isDuplicate(str(number)) and '0' not in str(number):
            check = 0
            for n in baseball:
                shot = str(n[0])
                strike = n[1]
                ball = n[2]

                result1, result2 = checkShot(shot, str(number))

                if strike == result1 and ball == result2:
                    check += 1

                if check == len(baseball):
                    answer += 1

            number += 1
        else:
            number += 1

    return print(answer)

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])


###
#first = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3)) 3자리 중복 없는 모든 리스트