import linked

def getFromEnd (ll, k):
    #Find the length of the linked list
    if ll.head == None:
        return None

    length = 1
    temp = ll.head
    while temp.nextNode != None:
        temp = temp.nextNode
        length += 1


    #Get the (length - k - 1)th element
    temp = ll.head
    for i in range(length - k - 1):
        temp = temp.nextNode

    return temp.value

ll = linked.LinkedList.getStringList("THISISALIST")
ll.printList()

print('')

print("0: ", getFromEnd(ll, 0))
print("2: ", getFromEnd(ll, 2))
print("5: ", getFromEnd(ll, 5))
