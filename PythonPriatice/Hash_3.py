import itertools
hashTable = {}
def solution(table):

    answer = 1

    for indexTable in range(len(table)):
        if table[indexTable][1] not in hashTable.keys():
            hashTable.setdefault(table[indexTable][1], []).append(table[indexTable][0])
        else:
            hashTable.setdefault(table[indexTable][1], []).append(table[indexTable][0])
    
    keys = hashTable.keys() # '가' '나' '다' '라' 
    values = [hashTable[key] for key in keys]
    
    ####only value
    #for i in  range(len(values)):
    #    answer *= len(values[i]) + 1

    ### value + string
    for i in  range(1, len(hashTable.values())+1):
        for n in itertools.combinations(values,i): #[['n==1'],['n==2'],['n==3']- - -]
            for element in itertools.product(*n):
                print(element)
                answer += 1
             
    #### once
    #for i in  range(1, len(hashTable.values())+1):
    #    listlist = (list(itertools.product(*n)) for n in itertools.combinations(list(values),i))
    #    print(list(listlist))    

    answer -= 1

    print(answer)


          
solution([["1","가"],["2","나"],["3","다"],["4","다"],["5","마"]])










