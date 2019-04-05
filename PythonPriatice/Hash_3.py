import itertools
hashTable = {}
combinationsOfValues = []
answerList = []
def solution(table):

    for indexTable in range(len(table)):
        if table[indexTable][1] not in hashTable.keys():
            hashTable.setdefault(table[indexTable][1], []).append(table[indexTable][0])
        else:
            hashTable.setdefault(table[indexTable][1], []).append(table[indexTable][0])

    keys = hashTable.keys() # '가' '나' '다' '라' 
    values = (hashTable[key] for key in keys)

    #values = [hashTable[key] for key in keys]  #[['1'],['2'],['3','4'],['5']]
    #combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]

    #1. All combinations of Value of keys
    for i in  range(1, len(values)+1):
        combinationsOfValues.append(list(itertools.combinations(values, i))) #[['1개 조합'],['2개 조합'],['3개 조합']- - -]
        #print(list(itertools.combinations(values, i+1))[0])

    print(list(combinationsOfValues[1]))
    #2. product each combined list
    for i in range(len(combinationsOfValues)):
        for j in range(len(list(combinationsOfValues[i]))):
            for element in itertools.product(*list(combinationsOfValues[i][j])):
                answerList.append(element)

    print(answerList)
    #arrAnswer = {1:{1:2},2:{1:3}}

    #print(arrAnswer[1].get(3))
    #for pivotKey in hashTable.keys():
    #    arrAnswer.append(hashTable.get(pivotKey))
    #    preValue = hashTable.get(pivotKey)
    #    pivot += 1
    #    for nextKeys in list(hashTable.keys())[pivot:]:
    #       preValue = preValue + " + " + hashTable.get(nextKeys)
    #       if hashTable.get(pivotKey) != hashTable.get(nextKeys):
    #           arrAnswer.append(preValue)


    #for pivotKey in hashTable.keys():
    #    preItems = {pivotKey:hashTable.get(pivotKey)}
    #    arrAnswer.update({pivot2:{pivotKey:hashTable.get(pivotKey)}})
    #    pivot += 1
    #    for nextKeys in list(hashTable.keys())[pivot:]:
    #        ssibal = nextKeys
    #        pivot2 += 1
    #        preItems.update({nextKeys:hashTable.get(nextKeys)})
    #        print(arrAnswer[0].get(nextKeys))
    #        if pivot2 == 1:
    #             arrAnswer.update({pivot2:preItems.copy()})
    #        elif arrAnswer[pivot-1].get(ssibal) != arrAnswer[pivot].get(ssibal):
    #            arrAnswer.update({pivot2:preItems.copy()})


        #   preValue = preValue + " + " + hashTable.get(nextKeys)
        #   if hashTable.get(pivotKey) != hashTable.get(nextKeys):
        #       arrAnswer.append(preValue)
        #       return print(arrAnswer)
                
            
        


solution([["1","가"],["2","나"],["3","다"],["4","다"],["5","마"]])










