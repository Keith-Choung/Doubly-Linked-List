# A node of the doublly linked list 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None

# Doubly Linked-List class
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def push(self, newData):
        newNode = Node(newData)
        
        # newNode -> self.head
        newNode.next = self.head

        # If the list is not empty
        if self.head != None:
                self.head.prev = newNode
        
        else:
            self.head = newNode
            self.tail = newNode
            
        # The head is now the new node
        self.head = newNode
        self.size += 1


    def pushback(self, newData): 
  	
        # Initialize new node
        newNode = Node(newData) 

        # If the list is not empty
        if self.head is None: 
            newNode.prev = None
            self.head = newNode 
            self.tail = newNode

        else:
            temp = self.tail
            temp.next = newNode
            newNode.prev = temp
            self.tail = self.tail.next

        self.size += 1


    def insertAfter(self, prevNode, newData):

        # If the list isn't empty
        if self.head != None:
            curr = self.head

            # Search for target node
            while curr.data != prevNode:
                curr = curr.next

            # If target was found, curr != None
            if curr != None:
                newNode = Node(newData)
                newNode.prev = curr
                newNode.next = curr.next

                # If curr is not the last node
                if curr.next is not None:
                    curr.next.prev = newNode

                else:
                    self.tail = newNode

                curr.next = newNode
        else:
            return

        self.size += 1


    def popFront(self):
  
        # If the list is not empty
        if self.head != None:

            # If there ISN'T only onde node
            if self.head.next != None:
                self.head = self.head.next
                self.head.prev = None

            # If there's only one node
            else:
                self.head = None
                self.tail = None

        else:
            return 

        self.size -= 1


    def popBack(self):
    
        # If the list isn't empty
        if self.head != None:

            # If there ISN'T only onde node
            if self.head != None:
                self.tail = self.tail.prev
                self.tail.next = None
            
            # If there's only one node
            else:
                self.head = None
                self.tail = None

        else:
            return

        self.size -= 1


    def pop(self, target):
        
        if self.head != None:
            
            curr = self.head

            # Search for target
            while curr.data != target:
                curr = curr.next

            # If curr is not the last node
            if curr.next != None:
                temp = curr.next
                curr.prev.next = temp
                temp.prev = curr.prev

            # If curr is the last node
            else:
                self.popBack()
        
        else:
            return

        self.size -= 1

    
    def getSize(self):
        return self.size


    def search(self, target): 
  
        current = self.head 

        # Loop till current not equal to None 
        while current != None: 
            if current.data == target: 
                return True # Data found 

            current = current.next

        return False # Data Not found 


    def reverse(self): 
        temp = None
        curr = self.head
        self.tail = curr
        
        # Swap next and prev for all nodes of  
        # doubly linked list 
        while curr is not None: 
            temp = curr.prev  
            curr.prev = curr.next
            curr.next = temp 
            curr = curr.prev

        # Before changing head, check for the cases like  
        # empty list and list with only one node 
        if temp is not None: 
            self.head = temp.prev


    def printList(self, nd): 
        while(nd is not None): 
            print(nd.data)
            nd = nd.next


dll = DoublyLinkedList()
dll.push(1)
dll.push(2)
dll.push(3)
dll.push(4)
dll.pushback(5)
# [4, 3, 2, 1, 5]
dll.insertAfter(3, 2.5)
# [4, 3, 2.5, 2, 1, 5]
dll.popFront()
# [3, 2.5, 2, 1, 5]
dll.popBack()
# [3, 2.5, 2, 1]
# print(dll.head.data)
# print(dll.head.prev.data)
dll.popFront()
# [2.5, 2, 1]
dll.pop(2)
# [2.5, 1]
dll.insertAfter(1, 0)
# dll.reverse()   
# print(dll.search(1))

dll.printList(dll.head)
print("size: ", dll.size)
