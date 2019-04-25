'''
prices	            return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''

def solution(prices):
    
    #answer = [0] * len(prices)
    answer = []
    good = 0

    for n in range(len(prices)):
        for j in range(n+1, len(prices),1):
            if prices[n] <= prices[j]:
                good += 1
            else:
                good += 1
                break
        answer.append(good)
        good = 0

    return print(answer)

solution([1, 2, 3, 2, 3])

