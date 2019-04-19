'''
priorities	         location	  return
[2, 1, 3, 2]	         2	        1
[1, 1, 9, 1, 1, 1]  	 0	        5

'''

import collections

def solution(priorities, location):
    answer = 0
    hashTable = collections.OrderedDict()
    sortedHashTable = collections.OrderedDict()

    for n in range(len(priorities)):
        hashTable.setdefault(n, priorities[n])

    print(max(hashTable, key=hashTable.values))

    while(len(hashTable) != 0):
        if list(hashTable)[0] == max(hashTable, key=hashTable.get):
            pivotKey = list(hashTable)[0]
            pivotValue = hashTable.pop(list(hashTable)[0])
            sortedHashTable.setdefault(pivotKey, pivotValue)
            print(sortedHashTable)
        else:
            hashTable.move_to_end(list(hashTable)[0])
            print(hashTable)

    answer = list(sortedHashTable.keys()).index(location) + 1


    return print(answer)

solution([1, 1, 9, 1, 1, 1], 0)