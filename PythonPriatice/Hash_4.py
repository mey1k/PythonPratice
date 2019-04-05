'''
               genres	                            plays	           return
[classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

'''

HashOfHashTable = {}
def solution(genres, plays):

    answer = []

    HashTable = {}

    #for i in range(len(genres)):
    #    HashTable.setdefault(genres[i], plays[i])
    #    HashOfHashTable.setdefault(i, {genres[i]:plays[i]})

    for i in range(len(genres)):
        HashOfHashTable.setdefault(plays[i], {genres[i]:i})

    plays.sort(reverse=True)

    answer = [HashOfHashTable.get(n) for n in plays]

    

    print(answer[0].keys())

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])