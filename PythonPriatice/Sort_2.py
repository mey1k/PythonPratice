'''
numbers 	            return
[6, 10, 2]	                6210
[3, 30, 34, 5, 9]	    9534330

'''

#from itertools import permutations

#def solution(numbers):
#    aswer = ""

#    candidateList = []
#    allCombination = list(permutations(numbers, len(numbers)))

#    for combination in allCombination:
#        strValue = ''.join(str(e) for e in combination)
#        candidateList.append(int(strValue))

#    answer = str(max(candidateList))

#    return print(answer)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # 숫자 문자열 비교 221221 < 222 를 이용하여 정렬
    numbers = int(''.join(numbers))
    return str(numbers)

solution([3, 30, 34, 5, 9])