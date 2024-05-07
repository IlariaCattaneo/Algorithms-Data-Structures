class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_two_sorted_lists(l1,l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    prev = ListNode(None)
    res = prev
    while l1 != None and l2 != None:
        if l1.value <= l2.value:
            prev.next = l1
            l1 = l1.next
            prev = prev.next
        else:
            prev.next = l2
            l2 = l2.next
            prev = prev.next
    if l1 == None:
        prev.next = l2
    else:
        prev.next = l1
    return res.next


# List 1: 1 -> 2 -> 4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

# List 2: 1 -> 3 -> 5
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(5)
node4.next = node5
node5.next = node6

# Merge lists
merged_head = merge_two_sorted_lists(node1, node4)

# Print merged list
current = merged_head
while current:
    print(current.value, end=" -> ")
    current = current.next