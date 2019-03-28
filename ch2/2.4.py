import linked

def partitionList(ll, partition):
    #Remove nodes < partion and put them at the beginning
    
    if ll.head == None:
        return None
    
    temp = ll.head
    while temp.nextNode != None:
        if temp.nextNode.value < partition:
            #Save node after next node
            nextNode = temp.nextNode.nextNode
            #Send nextNode to front of list
            temp.nextNode.nextNode = ll.head
            ll.head = temp.nextNode
            #Tie node after next node to current node
            temp.nextNode = nextNode
            continue
        #Go onto next node
        temp = temp.nextNode

    return ll


array = [1,5,7,2,4,9,1,3,7,3,7,8,2,9,1,0,5,1]
ll = linked.LinkedList.getArrayList(array)
ll.printList()
print('\n')
print('Partition: ', 5)
partitionList(ll, 5)
ll.printList()
print('\n')
ll = linked.LinkedList.getArrayList(array)
print('Partition: ', 2)
partitionList(ll, 2)
ll.printList()
print('\n')
ll = linked.LinkedList.getArrayList(array)
print('Partition: ', 8)
partitionList(ll, 8)
ll.printList()
print('\n')
