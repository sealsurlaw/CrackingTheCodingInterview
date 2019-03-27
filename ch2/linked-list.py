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

    def get (self, index):
        temp = self.head
        for i in range(index):
            if temp == None:
                return None
            temp = temp.nextNode
        return temp

    def printList (self):
        for i in range(self.length):
            print(self.get(i))

'''
ll = LinkedList()
ll.pushFront("cat")
ll.pushFront("dog")
ll.pushBack("bear")
ll.pushBack("snake")
ll.pushBack("fish")

ll.printList()
'''
