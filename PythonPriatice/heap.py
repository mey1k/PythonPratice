def downheap(i, size):
    while 2*i <= size:
        k = 2*i
        print(k)
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] > a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i=k

def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize // 2+1)):
        #print(i, hsize)
        downheap(i,hsize)

    #print(a)


a = [-1,54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20] # len = 17
create_heap(a)