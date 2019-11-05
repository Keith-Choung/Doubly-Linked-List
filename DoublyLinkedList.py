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
            self.head = newNode
        
        else:
            self.head = newNode
            self.tail = newNode

        self.size += 1


    def pushback(self, newData): 
  	
        # Initialize new node
        newNode = Node(newData) 

        # If the list is not empty
        if self.head != None: 
            temp = self.tail
            temp.next = newNode
            newNode.prev = temp
            self.tail = self.tail.next

        else:
            self.head = newNode 
            self.tail = newNode

        self.size += 1


    def insertAfter(self, target, newData):

        # If the list isn't empty
        if self.head == None:
            return

        else:

            curr = self.head

            # Search for target node
            while curr.data != target:
                curr = curr.next

                if curr == None:
                    print("Target not found.")
                    return

            newNode = Node(newData)
            newNode.prev = curr
            newNode.next = curr.next

            # If curr is not the last node
            if curr.next is not None:
                curr.next.prev = newNode

            else:
                self.tail = newNode

            curr.next = newNode

        self.size += 1


    def insertBefore(self, target, newData):

        # If the list isn't empty
        if self.head == None:
            return

        else:

            curr = self.head

            # Search for target node
            while curr.data != target:
                curr = curr.next

                if curr == None:
                    print("Target not found.")
                    return

            newNode = Node(newData)
            newNode.prev = curr.prev
            newNode.next = curr

            # If curr is not the first node
            if curr.prev != None:
                curr.prev.next = newNode

            else:
                self.head = newNode

            curr.prev = newNode

        self.size += 1


    def popFront(self):
  
        # If the list is not empty
        if self.head == None:
            return
        
        else:

            # If there ISN'T only onde node
            if self.head.next != None:
                self.head = self.head.next
                self.head.prev = None

            # If there's only one node
            else:
                self.head = None
                self.tail = None

        self.size -= 1


    def popBack(self):
    
        # If the list isn't empty
        if self.head == None:
            return

        else:

            # If there ISN'T only one node
            if self.head.next != None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None

        self.size -= 1


    def pop(self, target):
        
        if self.head == None:
            return

        else:
            curr = self.head

            # Search for target
            while curr.data != target:
                curr = curr.next
                
                if curr == None:
                    print("Target not found.")
                    return

            # If curr is not the last node
            if curr.next != None:
                temp = curr.next
                curr.prev.next = temp
                temp.prev = curr.prev

            # If curr is the last/only node
            else:
                self.popBack()
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


    def printList(self, node): 

        while(node is not None): 
            print(node.data)

            # Get next node
            node = node.next


dll = DoublyLinkedList()

dll.push(3)
dll.push(4)
dll.insertBefore(3, 2)
# dll.push(3)
# dll.push(4)
dll.pushback(5)
dll.insertAfter(5,6)
print("head:", dll.head.data)
print("tail:", dll.tail.data)
# dll.pop(5)





dll.printList(dll.head)
# print("size: ", dll.size)
