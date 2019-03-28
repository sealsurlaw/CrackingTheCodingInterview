import linked

def isPalendrome (ll1):
    #Create a reversed list
    #Check if each element is the same
    
    ll2 = linked.LinkedList()

    #Reverse list
    temp = ll1.head
    while temp != None:
       ll2Temp = ll2.head
       ll2.head = linked.Node(temp.value)
       ll2.head.nextNode = ll2Temp
       temp = temp.nextNode

    #Compare each value
    temp1 = ll1.head
    temp2 = ll2.head
    while temp1 != None:
        if temp1.value != temp2.value:
            return False
        temp1 = temp1.nextNode
        temp2 = temp2.nextNode

    return True

ll = linked.LinkedList.getStringList('RACECAR')
print(ll.toString(), ': ', isPalendrome(ll))

ll = linked.LinkedList.getStringList('Racecar')
print(ll.toString(), ': ', isPalendrome(ll))

ll = linked.LinkedList.getStringList('watermelon')
print(ll.toString(), ': ', isPalendrome(ll))
