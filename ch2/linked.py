class Node:
    def __init__ (self, value, nextNode=None):
        self.value = value
        if nextNode != None:
            self.nextNode = nextNode
        else:
            self.nextNode = None

    def __str__ (self):
        return self.value

class LinkedList:
    def __init__ (self, ll=None):
        self.head = None
        self.length = 0
        if ll != None:
            self.head = ll.head
            self.length = ll.length

    def getLength (self):
        if self.head == None:
            return 0
        temp = self.head
        length = 1
        while temp.nextNode != None:
            temp = temp.nextNode
            length += 1
        return length

    def pushBack (self, value):
        #Check if list is empty
        if self.head == None:
            #Create the first node
            self.head = Node(value)
            self.length += 1
            return

        #Start at the head
        temp = self.head
        #Find the end
        while temp.nextNode != None:
            temp = temp.nextNode
        
        #Add new node to the end
        temp.nextNode = Node(value)
        self.length += 1
        return temp.nextNode

    def pushFront (self, value):
        #Check if list is empty
        if self.head == None:
            #Create the first node
            self.head = Node(value)
            self.length += 1
            return

        #Add to beginning
        temp = self.head
        self.head = Node(value, temp)
        self.length += 1
        return self.head

    def popBack (self):
        #Check if list is empty
        if self.length == 0:
            return None

        #Remember last node
        poppedNode = self.get(self.length - 1).value
        #Decrement length
        self.length -= 1
        #Remove nextNode from last node
        self.get(self.length - 1).nextNode = None
        return poppedNode

    def popFront (self):
        #Check if list is empty
        if self.length == 0:
            return None

        #Remember head value
        poppedNode = self.head.value
        #Set head to next node
        self.head = self.head.nextNode
        #Decrement length
        self.length -= 1
        return poppedNode


    def get (self, index):
        temp = self.head
        for i in range(index):
            if temp == None:
                return None
            temp = temp.nextNode
        return temp

    def printList (self):
        for i in range(self.getLength()):
            print(self.get(i).value, end='')

    @staticmethod
    def getStringList (string):
        ll = LinkedList()
        for char in string:
            ll.pushBack(char)
        return ll

    @staticmethod
    def getArrayList (array):
        return LinkedList.getStringList(array)

