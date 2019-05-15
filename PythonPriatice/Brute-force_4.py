'''
brown	    red	    return
10	        2	        [4, 3]
8	            1	        [3, 3]
24	        24	    [8, 6]

'''

def solution(brown, red):

    answer = []
    area = brown + red
    max_length = int(area**(1/2)) + 1 ## width * height = area -> we know that Height From minheight to maxHeight and minHeight >= 3 because redHeight >= 1

    for b in range(3, max_length): ## 3~7 -> 3,4,5,6 so we need  plus 1
        if area % b:
            continue
        a = area // b
        if red == (a - 2) * (b - 2):
            return print([a, b])

solution(24,24)