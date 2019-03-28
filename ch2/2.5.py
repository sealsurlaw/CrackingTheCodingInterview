import linked

def addLists (ll1, ll2):
    #Add one node value with the other
    #Save the remainder
    #Add the next two node values and the remainder

    temp1 = ll1.head
    temp2 = ll2.head
    result = linked.LinkedList()
    remainder = 0
    while temp1 != None or temp2 != None:
        #Check if one number has run out of digits
        if temp1 == None:
            result.pushBack(temp2.value + remainder)
            remainder = 0
            temp2 = temp2.nextNode
            continue
        if temp2 == None:
            result.pushBack(temp1.value + remainder)
            remainder = 0
            temp1 = temp1.nextNode
            continue

        digitSum = temp1.value + temp2.value + remainder
        remainder = int(digitSum / 10)
        if digitSum > 9:
            digitSum = digitSum - 10
        temp1 = temp1.nextNode
        temp2 = temp2.nextNode

        result.pushBack(digitSum)

    return result

l1 = [1,9,6]
l2 = [4,0,0,9]

ll1 = linked.LinkedList.getArrayList(l1)
ll2 = linked.LinkedList.getArrayList(l2)

print('Num1: ', ''.join(str(e) for e in l1[::-1]))
print('Num2: ', ''.join(str(e) for e in l2[::-1]))

result = addLists(ll1, ll2)
print('Rslt: ', ''.join(str(e) for e in result.toList()[::-1]))

print('')

l1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
l2 = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,0,9]

ll1 = linked.LinkedList.getArrayList(l1)
ll2 = linked.LinkedList.getArrayList(l2)

print('Num1: ', ''.join(str(e) for e in l1[::-1]))
print('Num2: ', ''.join(str(e) for e in l2[::-1]))

result = addLists(ll1, ll2)
print('Rslt: ', ''.join(str(e) for e in result.toList()[::-1]))
