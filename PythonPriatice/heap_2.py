'''
stock	    dates	        supplies	    k	    result
4	            [4,10,15]   	[20,5,10]	    30	2
'''
#import heapq

#def solution(stock, dates, supplies, k):
#    answer = 0
#    Day = 0
#    i=0

#    while stock < k-1:
       
#        if stock < dates[i] + (dates[i+1]-dates[i]):
#            stock += supplies[i]
#            answer += 1
#            i += 1
#        else:
#            i += 1
        

#    return print(answer)

#solution(4,[4,10,15],[20,5,10],30)
import heapq

def solution(stock, dates, supplies, k):

    answer = 0
    event = list(zip(dates, supplies)) # day, supply 합치기
    heap = []
    while stock < k: # 쌓여있는 자원이 안전할  때 까지 공급
        while event and event[0][0] <= stock:  # 공급할 자원이 남아있고 그 자원의 공급일이 현재 자원 보다 작거나 같을경우 계속 공급
            date, supply = event.pop(0)
            heapq.heappush(heap, -supply) # 최대힙
        stock += -heapq.heappop(heap)
        answer += 1
    return print(answer)

solution(4,[4,10,15],[20,5,10],30)