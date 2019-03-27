import linked as ll

def removeDuplicates (linked):
    temp = linked.head
    #Iterate through all nodes
    while temp != None and temp.nextNode != None:
        #If the same in a row
        if temp.value == temp.nextNode.value:
            #Remove reference to duplicate node
            temp.nextNode = temp.nextNode.nextNode
            linked.length -= 1
            #Check current node with new next again
            continue
        #Otherwise go to next node
        temp = temp.nextNode


linked = ll.LinkedList.getStringList("FOLLOW UPPPP")
linked.printList()
print('')
removeDuplicates(linked)
linked.printList()
print('')
