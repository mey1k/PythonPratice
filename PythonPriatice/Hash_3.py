hashTable = {}
arrAnswer = {}
def solution(table):

    for i in range(len(table)):
        hashTable[table[i][0]] = table[i][1]

    pivot = 0
    pivot2 = 0
    preValue = ""

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


    for pivotKey in hashTable.keys():
        preItems = {pivotKey:hashTable.get(pivotKey)}
        arrAnswer.update({pivot2:{pivotKey:hashTable.get(pivotKey)}})
        pivot += 1
        for nextKeys in list(hashTable.keys())[pivot:]:
            ssibal = nextKeys
            pivot2 += 1
            preItems.update({nextKeys:hashTable.get(nextKeys)})
            print(arrAnswer[0].get(nextKeys))
            if pivot2 == 1:
                 arrAnswer.update({pivot2:preItems.copy()})
            elif arrAnswer[pivot-1].get(ssibal) != arrAnswer[pivot].get(ssibal):
                arrAnswer.update({pivot2:preItems.copy()})


        #   preValue = preValue + " + " + hashTable.get(nextKeys)
        #   if hashTable.get(pivotKey) != hashTable.get(nextKeys):
        #       arrAnswer.append(preValue)
        #       return print(arrAnswer)
                
            
        


solution([["1","가"],["2","나"],["3","다"],["4","다"],["5","마"]])










