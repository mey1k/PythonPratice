def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    participantTable = {}
    completionTable = {}

    for i in range(len(participant)):
       participantTable.setdefault(i, participant[i]) 
    
    for j in range(len(completion)):
        completionTable.setdefault(j, completion[j])

    for key in participantTable.keys():
        if key not in completionTable:
            answer = participantTable[key]
            break
        elif (participantTable[key] != completionTable[key]):
            answer = participantTable[key]
            break
    
    print(answer)

#-2
#import collections

#def solution(participant, completion):
    
#    answer = collections.Counter(participant) - collections.Counter(completion)
    
#    print(answer)
    

#    a = collections.Counter('ccaaccbbccdd')
#    b = collections.Counter('abbbcce')
#    c = collections.Counter(['leo','jand','leo'])
#    print(a-b)
#    print(c)
#    return list(answer.keys())[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])