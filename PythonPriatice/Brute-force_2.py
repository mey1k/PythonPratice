'''
numbers 	return
17	            3
011	            2

'''

from itertools import permutations

def isPrimeNumber(n):

    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False

    return True

def solution(numbers):

    answer = 0

    numberList = []
    allCombinations = []
    result = []

    for i in  range(len(numbers)):
        numberList.append(numbers[i])

    for i in range(1,len(numberList)+1):
        allCombinations += permutations(numbers, i)

    for n in allCombinations:
        combination = str(''.join(n))
        if combination[0] == '0':
            combination = combination.replace('0','')
        if combination not in result and combination != '':
            result.append(combination)

    for n in result:
        if isPrimeNumber(int(n)):
            answer += 1

    return print(answer)

solution("011")