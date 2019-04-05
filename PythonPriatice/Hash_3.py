import itertools
hashTable = {}
combinationsOfValues = []
answerList = []
def solution(table):

    answer = 0

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
    for i in  range(1, len(hashTable.values())+1):
        #combinationsOfValues.append(list(itertools.combinations(values, i))) #[['1개 조합'],['2개 조합'],['3개 조합']- - -]
        #print(list(itertools.combinations(values, i+1))[0])

        #answer += len(list(itertools.product(itertools.combinations(values,i))))
        #print(list(itertools.product(itertools.combinations(values,i))))
        #for n in itertools.combinations(values,i):
            #print(n)
            #print(list(itertools.product(*n)))
            #answer += len(list(itertools.product(*n)))
            #for element in itertools.product(*n):
                #print(element)
                 #answer += 1

        print(list(values))
        print(list(itertools.combinations(list(values),3)))

        listlist = (len(list(itertools.product(*n))) for n in itertools.combinations(list(values),i))
        answer += sum(list(listlist))    

        #print(list(listlist))
        #answer += (len(list(listlist)))
    #print(list(combinationsOfValues[1]))

    #2. product each combined list
    #for i in range(len(combinationsOfValues)):
    #    for j in range(len(list(combinationsOfValues[i]))):
    #        for element in itertools.product(*list(combinationsOfValues[i][j])):
    #            answerList.append(element)

    print(answer)


          
solution([["1","가"],["2","나"],["3","다"],["4","다"],["5","마"]])










