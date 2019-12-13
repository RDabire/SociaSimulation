# HeapTest Harness
from Heaps import *
numpassed = 0
numtests = 0

# Test case 1 - Adding to Heap Table
print("### Test case 1 - Adding to Heap Table ###")
numtests += 1
H = Heap(10)
try:
    H.add(5, "five")
    H.add(4, "four")
    H.add(1, "one")
    H.add(11, "eleven")
    H.add(10, "ten")
    H.add(3, "three")
    H.add(2, "two")
    H.add(16, "sixteen")
    H.add(12, "twelve")
    H.add(19, "nineteen")
    H.display()
    print()
    numpassed += 1

except:
    print("FAILED: could not add to heap")


# Test case 2 - Remove from table
print("### Test case 2 - Remove from table ####")
numtests += 1
try:
    H.remove()
    H.display()
    print()
    numpassed += 1
except:
    print("FAILED: Could remove from heap table")

# Test case 3 Heapify
print("### Test 3 Heapify ###")
numtests += 1
H2 = Heap(9)
try:
    arr = [5, 4, 1, 11, 10, 3, 2, 16, 12]
    H2.heapify(arr)
    H2.display()
    print()
    numpassed += 1
except:
    print("FAILED: could not heapify")


# Test case 4 HeapSort
print("### Test 4 HeapSort ###")
numtests += 1
H2 = Heap(8)
try:
    arr = [5, 4, 1, 11, 10, 2, 16, 12]
    H2.heapSort(arr)
    print()
    numpassed += 1
except:
    print("FAILED: could not HeapSort")

# Test case 5 HeapSort
print("### Test 5 HeapSort ###")
numtests += 1
H2 = Heap(14)
try:
    arr = [12, 11, 13, 5, 6, 7, 1, 2, 17, 19, 21, 29, 32, 20]
    H2.heapSort(arr)
    print()
    numpassed += 1
except:
    print("FAILED: could not HeapSort")

# Test case 6 FileIo
#print("### Test 6 HeapSort from a file ###")
#numtests += 1
#try:
#    H2 = Heap(6170)
#    H2.fileIO()
#    print()
#    numpassed += 1
#except:
#    print("FAILED: could not HeapSort file")

# Results
print("\nPassed ", numpassed, "of", numtests, "tests: ", 100 * numpassed / numtests, "%\n")

