'''
               genres	                            plays	           return
[classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

'''

hashTable = {}
def solution(genres, plays):

    answer = []

    for i in range(len(genres)):
        if genres[i] not in hashTable.keys():
            hashTable.setdefault(genres[i], []).append(plays[i])
        else:
            hashTable.setdefault(genres[i], []).append(plays[i])

    while len(hashTable.keys()) != 0:
        pivotGenres = max(hashTable, key = lambda x: hashTable.get(x))
        pivotPlays = hashTable[pivotGenres]
        pivotPlays.sort(reverse=True)
        if(len(pivotPlays) > 1):
            answer.append(plays.index(pivotPlays[0]))
            answer.append(plays.index(pivotPlays[1]))
        else:
            answer.append(plays.index(pivotPlays[0]))
        hashTable.pop(pivotGenres)

    return answer

solution(["classic", "pop", "classic", "classic", "pop", "pop"], [500, 600, 150, 800, 2500, 250])