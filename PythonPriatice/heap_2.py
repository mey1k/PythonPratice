'''
stock	    dates	        supplies	    k	    result
4	            [4,10,15]   	[20,5,10]	    30	2
'''

def solution(stock, dates, supplies, k):
    answer = 0
    limit = 0

    for n in supplies:
        limit += stock + n
        answer +=1
        if k-1 <= limit:
            break

    return print(answer)

solution(4,[4,10,15],[20,5,10],30)