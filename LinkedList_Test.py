#*********************************************************************
# 
#  AUTHOR: Roy Dabire
#  PURPOSE: Basic Test Harness For Linked List
#
#  REQUIRES: LinkedLists.py
#*********************************************************************
from LinkedList import *
import pickle

numPassed = 0
numTests = 0

ll = None 
sTestString = ""
nodeValue = None

#Test 1 - Constructor
print("\n\nTesting Normal Conditions - Constructor")
print("=======================================")
try:
    
    numTests += 1
    ll = LinkedList()
    print("Testing creation of DSALinkedList (isEmpty()):")
    if (not ll.isEmpty()):
        raise ListError("Head must be None.")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

     
#Test 2 - Insert First
print("\nTest insert first and remove first - stack behaviour")
print("=======================================")
try:
    numTests += 1
    print("Testing insertFirst():")
    ll.insertFirst("abc")
    ll.insertFirst("jkl")
    ll.insertFirst("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
    

#Test 3 - Peek First
try:
    numTests += 1
    print("Testing peek.First():")
    testString = ll.peekFirst()
    if testString != "xyz":
        raise ListError("Peek First failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")


#Test 4 - Remove first
try:
    numTests += 1
    print("Testing removeFirst():")
    testString = ll.removeFirst()
    if testString != "xyz":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "jkl":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "abc":
        raise ListError("Remove first failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 5 - Remove from empty list
try:
    numTests += 1
    print("Testing removeFirst() when empty")
    testString = ll.removeFirst()
    raise ListError("Remove first when empty failed")
    print("Failed")
except:
    numPassed += 1
    print("Passed")


#Test 6 - Insert Last 
print("\nTest insert last and remove first - queue behaviour")
print("=======================================")
try:
    numTests += 1
    print("Testing insertLast():")
    ll.insertLast("abc")
    ll.insertLast("jkl")
    ll.insertLast("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 7 - Peek Last
try:
    numTests += 1
    print("Testing peekFirst():")
    testString = ll.peekFirst()
    if testString != "abc":
        raise ListError("Peek First failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 8 - Remove first
try:
    numTests += 1
    print("Testing removeFirst():")
    testString = ll.removeFirst()
    if testString != "abc":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "jkl":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "xyz":
        raise ListError("Remove first failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 9 - Is Empty 2
try:
    numTests += 1
    print("Testing isEmpty when empty")
    testString = ll.removeFirst()
    raise ListError("Remove first when empty failed")
    print("Failed")
except:
    numPassed += 1
    print("Passed")


#Test 10 Serialisation
print("=======================================")
print("\nSaving object to a file...")
numTests += 1
try:
    ListB= LinkedList()
    ListB.insertFirst("abc")
    ListB.insertFirst("jkl")
    ListB.insertFirst("xyz")
    with open("SavedPickle", "wb") as PickleFile:
        pickle.dump(ListB, PickleFile)
    numPassed += 1
except:
     print("Error: problem pickling object!")
     print("=======================================")

#Test 11 Serialisation
print("=======================================")
print("\nLoading object...")
numTests += 1
try:
    with open("SavedPickle", "rb") as PickleFile:
        Loaded_object= pickle.load(PickleFile)
    numPassed += 1
except:
     print("Error: problem loading object!")
     print("=======================================")   

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")
