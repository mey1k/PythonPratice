'''
               genres	                            plays	           return
[classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

'''

hashTable = {}
def solution(genres, plays):

    answer = []
    genresScore = 0 

    for i in range(len(genres)):
        if genres[i] not in hashTable.keys():
            hashTable.setdefault(genres[i], []).append(plays[i])
        else:
            hashTable.setdefault(genres[i], []).append(plays[i])

    while len(hashTable.keys()) != 0:

        for keys, values in hashTable.items():
            if genresScore < sum(values):
                genresScore = sum(values)
                pivotGenres = keys

        #pivotGenres = max(hashTable, key = lambda x: hashTable.get(x))

        pivotPlays = hashTable[pivotGenres]
        pivotPlays.sort(reverse=True)
        if(len(pivotPlays) > 1):
            if plays.index(pivotPlays[0]) == plays.index(pivotPlays[1]):
                temp = [i for i,x in enumerate(plays) if x==pivotPlays[0]]
                answer.append(temp[0])
                answer.append(temp[1])
            else:
                answer.append(plays.index(pivotPlays[0]))
                answer.append(plays.index(pivotPlays[1]))
        else:
            answer.append(plays.index(pivotPlays[0]))
        hashTable.pop(pivotGenres)
        pivotGenres = []
        genresScore = 0

    return print(answer)

#solution(["classic", "classic", "pop", "classic", "pop", "classic"], [400,600,150,2500,500,500])
solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
#solution(["classic"], [400])