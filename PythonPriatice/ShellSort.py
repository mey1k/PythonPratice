def gapInsertionSort(x, start, gap):
    for target in range(start+gap, len(x), gap):
        val = x[target]
        i = target
        while i > start:
            if x[i-gap] > val:
                x[i] = x[i-gap]
            else:
                break
            i -= gap
        x[i] = val

def shellSort(x):
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(x, start, gap)
        gap = gap // 2
    print(x)

shellSort([12,312,321,312,3,123,123,12,312,312,3])
