#트리의 시작 인덱스는 1이다.
#따라서 리스트에 값을 접근할 때는 index-1 임에 유의하자.

class MinHeap: 
    def __init__(self):
        self.queue = [] #초기화
        self.resultHeapSort = []

    @staticmethod
    def parent(index): #index에 해당하는 원소의 부모 index를 리턴해주는 함수
        return index//2

    def insert(self, n):
        self.queue.append(n)
        i =  len(self.queue) # Last index
        while i>1:
           parent = self.parent(i) 
           if self.queue[i-1] < self.queue[parent-1]: 
               self.queue[i-1], self.queue[parent-1] = self.queue[parent-1], self.queue[i-1]
               i = parent
           else: # 만약 부모가 더 작으면 거기서 끝.
              break

    def delete(self):
        self.queue[0], self.queue[len(self.queue) - 1] = self.queue[len(self.queue) - 1] , self.queue[0] #마지막 원소와 root를 바꿔주고
        self.resultHeapSort.append(self.queue[-1]) # heap_Sort Result, O(nlogn)
        self.queue.pop(len(self.queue)-1) #마지막 원소를 제거한다.
        self.minHeapify(1) #root index에서 heapify를 시작한다.

    @staticmethod
    def leftchild(index): #왼쪽자식 index를 리턴
        return index*2

    @staticmethod
    def rightchild(index): #오른쪽자식 index를 리턴
        return index*2 + 1

    def minHeapify(self, i): #이 함수가 결국 자식들과 비교해 가면서 내려가는 함수입니다.
        left = self.leftchild(i)
        right = self.rightchild(i)
        smallest = i #일단은 가장 작은 것을 자신으로 놓고
        if left <= len(self.queue) and self.queue[left - 1] < self.queue[smallest-1]: #만약 왼쪽 자식이 존재하고, 가장 작은 것보다 더 작으면
            smallest = left #가장작은 것은 왼쪽자식이 된다.
        if right <= len(self.queue) and self.queue[right - 1] < self.queue[smallest-1]: #만약 오른쪽 자식도 존재하고, 그것이 현재까지 최소보다 더 작으면
            smallest = right #가장 작은 것은 오른쪽 자식
        if smallest != i: #만약 자신이 가장 작은 것이 아니면,
            self.queue[i-1], self.queue[smallest-1] = self.queue[smallest-1], self.queue[i-1] #자식들 중 가장 작은 것과 바꿔주고
            self.minHeapify(smallest) #recursive call을 하여 내려가서 다시 진행

import random

minheap = MinHeap()

for _ in range(10):
    minheap.insert(random.randint(1,50))

print(minheap.queue)

for _ in range(10): #넣었던 원소들을 하나씩 지우면서 queue를 출력합니다. 결국 작은것부터 지워져나가야겠죠?
    minheap.delete()
    print(minheap.queue)

print(minheap.resultHeapSort)
