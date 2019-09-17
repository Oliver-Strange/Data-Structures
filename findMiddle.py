'''
some list of unknown length 

take list head 
first var = current_slow
second var = current_fast 
both start at head 

while current_fast 
    current_slow increments once, current_fast increments twice
return current_slow.data
'''


def findMiddle(listHead):
    slow = listHead
    fast = listHead
    while fast:
        fast = fast.next.next
        slow = slow.next

    return slow


'''
initialize three pointers
prev = None
current = head
next = None

while current has a value
    the next node becomes the current.next node
    the current.next becomes the previous value
    the previous node become the current value
list.head becomes the current (null) previous (last becomes first) 

'''


def reverse(listHead):
    prev = None
    current = listHead
    next = listHead.next

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    listhead = prev
