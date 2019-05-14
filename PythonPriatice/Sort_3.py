'''
citations	        return
[3, 0, 6, 1, 5]	3

'''

def solution(citations):
    answer = 0
    
    citations.sort()   
    
    for i in range(len(citations)):
        answer = citations[i]
        if answer >= len(citations) - i:
           return print(len(citations) - i)

    return 0

solution([7,0,5,3,9])