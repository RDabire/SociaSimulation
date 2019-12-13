class HeapEntry():
    def __init__(self, inPriority, inValue):
        self.priority = inPriority
        self.value = inValue


class Heap:
    def __init__(self, maxSize):
        self.count = 0
        self.capacity = int(maxSize)
        self.heapArr = [HeapEntry(0, "base") for i in range(maxSize)]  # how do i make the array with the heap entries
        # What ive done above ^ is hard coded

    def add(self, priority, value):
        self.heapArr[self.count] = HeapEntry(priority, value)
        self.count += 1
        self.trickleUp()

    def remove(self):
        temp = self.heapArr[0]
        self.count -= 1
        self.heapArr[0] = self.heapArr[self.count]
        self.trickleDown()
        self.heapArr[self.count] = HeapEntry(0, "base")
        return temp

    def heapify(self, arr):
        for i in arr:
            self.add(i, "None")

        #for i in self.heapArr:
            #print(i.priority)

    def heapSort(self, arr):
        self.heapify(arr)
        Sorted = [self.remove() for ii in self.heapArr]

       # for i in Sorted:
        #    print(i.priority)

        return Sorted

    def trickleUp(self):  # what goes in brackets
        self._trikleUpRec(self.heapArr, self.count - 1)

    def _trikleUpRec(self, heapArr, curIdx):
        parentIdx = (curIdx - 1) // 2
        if curIdx > 0:
            if heapArr[curIdx].priority > heapArr[parentIdx].priority:
                temp = heapArr[parentIdx]
                heapArr[parentIdx] = heapArr[curIdx]
                heapArr[curIdx] = temp
                self._trikleUpRec(heapArr, parentIdx)

    def trickleDown(self):
        self._trickleDownRec(self.heapArr, 0, self.count - 1)

    def _trickleDownRec(self, heapArr, curIdx, numItems):
        lChildIdx = curIdx * 2 + 1
        rChildIdx = lChildIdx + 1
        if lChildIdx < numItems:
            largeIdx = lChildIdx
            if rChildIdx < numItems:
                if heapArr[lChildIdx].priority < heapArr[rChildIdx].priority:
                    largeIdx = rChildIdx
            if heapArr[largeIdx].priority > heapArr[curIdx].priority:
                temp = heapArr[largeIdx]
                heapArr[largeIdx] = heapArr[curIdx]
                heapArr[curIdx] = temp
                self._trickleDownRec(heapArr, largeIdx, numItems)

    def display(self):
        for items in self.heapArr:
            print(items.priority)

    def NumberOfItems(self):
        print(self.count)

    








