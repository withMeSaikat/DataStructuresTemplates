from math import floor

class Heap:
    def __init__(self, arr, minHeap=True):
        self.arr = arr
        self.size = len(arr)
        self.minHeap = minHeap
        self.heap = None
        
    def parent(self, ind):
        return floor((ind - 1) / 2)

    def heapifyBU(self): # bOTTOM-UP Approach
        self.heap = self.arr.copy()

        for i in range(floor(self.size / 2) - 1, -1, -1):
            self.heapifyDown(i, self.size)
    
    def heapifyTD(self):
        self.heap = [0] * self.size
        curr = 0
        for i in range(len(self.arr)):
            self.heap[curr] = self.arr[i]
            self.heapifyUp(curr)
            curr += 1

    def heapifyDown(self, ind, size):
        # if ind >= floor(self.size / 2):
        #     return
    
        s = ind
        left = 2 * ind + 1
        right = 2 * ind + 2
        
        if left < size:
            if (self.minHeap and self.heap[s] > self.heap[left]) or ((not self.minHeap) and self.heap[s] < self.heap[left]):
                s = left

        if right < size:
            if (self.minHeap and self.heap[s] > self.heap[right]) or ((not self.minHeap and self.heap[s] < self.heap[right])):
                s = right
            
        if s != ind:
            self.heap[s], self.heap[ind] = self.heap[ind], self.heap[s]
            self.heapifyDown(s, size)
    
    def heapifyUp(self, ind):
        while ind > 0:
            p = self.parent(ind)
            if (self.minHeap and self.heap[ind] < self.heap[p]) or (not self.minHeap and self.heap[ind] > self.heap[p]):
                self.heap[ind], self.heap[p] = self.heap[p], self.heap[ind]
                ind = p
            else:
                break
                  
    def printHeap(self):
        for num in self.heap:
            print(num, end=" ")
        print()

    def heapSort(self, inplace=False):
        sortedHeap = self.heap.copy()
        for i in range(self.size-1, -1, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heapifyDown(0, i)

        if inplace:
            self.heap = sortedHeap

    def insert(self, val):
        self.arr.append(val)
        self.heap.append(val)
        self.size += 1
        self.heapifyUp(self.size-1)

    def popHead(self):
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        head = self.heap.pop(self.size - 1)
        self.size -= 1
        self.heapifyDown(0, self.size)
        return head

arr = [3, 5, 6, 0, 10, 14]
arr = list([ord(s) for s in 'trnqf'])
heap = Heap(arr[:3])
heap.heapifyTD()
heap.printHeap()
heap.heapSort()
heap.printHeap()
heap.heapifyBU()
heap.printHeap()
heap.insert(15)
heap.printHeap()

print(heap.popHead())
print(heap.popHead())
print(heap.popHead())
print(heap.popHead())