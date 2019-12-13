# LinkedList

class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def _isEmpty(self):
        return self.head is None

    def insertFirst(self, data):
        if self._isEmpty():
            new_node = ListNode(data)
            new_node.previous = None
            self.head = new_node  # Done
            self.tail = new_node

        else:
            new_node = ListNode(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.previous = None

    def insertLast(self, data):
        if self._isEmpty():
            new_node = ListNode(data)
            new_node.previous = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(data)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None

    def peekFirst(self):
        if self._isEmpty():
            raise EmptyList("INVALID: Empty Linked List")
        else:
            nodeValue = self.head.data
        print(nodeValue)
        return nodeValue

    def peekLast(self):
        if self._isEmpty():
            raise EmptyList("INVALID: Empty Linked List")
        else:
            nodeValue = self.tail.data
        print(nodeValue)
        return nodeValue

    def removeFirst(self):
        if self._isEmpty():
            raise EmptyList("INVALID: Empty Linked List")

        elif self.head.next is None:
            nodeValue = self.head
            nodeValue = self.tail
            self.head = None
            self.tail = None

        else:
            nodeValue = self.head
            self.head = self.head.next
            self.head.previous = None
        return nodeValue.data
                                #Inspired from:
    def removeMiddle(self, node): #https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
        temp = self.head
        if temp is not None:
            if temp.data == node:           #Method allows removal of post or user
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == node:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
                                #Inspired from:
    def search(self, node):  #https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
        # Initialize current to head
        current = self.head
        while current != None:
            if current.data == node:
                print(current.data)
                return current.data  
            current = current.next
        print("Post cannot be found")  

    def __iter__(self):
        self._cur = self.head
        return self

    def __next__(self):
        if self._cur is None:
            raise StopIteration  
        else:
            curval = self._cur.data
            self._cur = self._cur.next
        return curval

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


class Error(Exception):
    pass


class EmptyList(Error):
    """ Exception raised if stack is overfull.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


