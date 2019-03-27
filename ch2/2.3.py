import linked

def deleteNode (node):
    #Copy value and nextNode from nextNode
    #Let garbage collection take care of nextNode
    #(If language with no garbage collection, remember nextNode and release memory)
    node.value = node.nextNode.value
    node.nextNode = node.nextNode.nextNode

ll = linked.LinkedList.getStringList("Going to delete this ->X node")
ll.printList()

print('')

node = ll.get(23)
print('Node to be deleted: ', node)

deleteNode(node)

ll.printList()
print('') 
