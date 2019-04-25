'''
heights	return
[6,9,5,7,4]	[0,0,2,2,4]
[3,9,9,3,5,7,2]	[0,0,0,3,3,3,6]
[1,5,3,6,7,6,5]	[0,0,2,0,0,5,6]
'''

def solution(heights):
    answer = []

    pivotIndex = 0

    while pivotIndex != len(heights) :
        for index in range(pivotIndex,-1,-1):
           if  heights[index] > heights[pivotIndex]:
               answer.append(index+1)
               break   
        pivotIndex += 1
        if len(answer) < pivotIndex:
            answer.append(0)

    return print(answer)

solution([1,5,3,6,7,6,5])

#best answer 
#def solution(h):
#    ans = [0] * len(h)
#    for i in range(len(h)-1, 0, -1):
#        for j in range(i-1, -1, -1):
#            if h[i] < h[j]:
#                ans[i] = j+1
#                break
#    return ans