'''

      arrangement	            return
()(((()())(())()))(())	         17

'''

import queue

def solution(arrangement):
    answer = 0
    Ironstick = queue.Queue()
    arrangement = arrangement.replace('()', 'l') # l(((ll)(l)l))(l)
    for pivot in arrangement:
        if pivot == '(':
            Ironstick.put('(')
            answer += 1
        elif pivot == ')':
            Ironstick.get()
        elif pivot == 'l':
            answer += Ironstick.qsize()
            
    return answer

solution("()(((()())(())()))(())")