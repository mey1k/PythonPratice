'''
array	                    commands	                        return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]   	[5, 6, 3]

'''

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        operators = commands[i]
        arrayClone = array.copy()
        arrayClone = arrayClone[operators[0]-1:operators[1]]
        arrayClone.sort()
        answer.append(arrayClone[operators[2]-1])

    return print(answer)

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])


##best
#def solution(array, commands):
#    answer = []
#    for com in commands:
#        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
#    return answer