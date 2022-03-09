class ListNode():
    def __init__(self, x,next=None):
        self.data = x
        self.next = next

def xe(head:ListNode):
    temp = head
    x = ""
    while temp:
        x += str(temp.data)+"->"
        temp = temp.next
    return x
    

def partition(head, x):
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.data < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next


if __name__ == '__main__':
    s1 = ListNode(5,None)
    s2 = ListNode(7,s1)
    s3 = ListNode(1,s2)
    s4 = ListNode(8,s3)
    s5 = ListNode(6,s4)
    s6 = ListNode(3,s5)
    s7 = ListNode(2,s6)
    s8 = ListNode(4,s7)
    temp = xe(s8)
    print(temp)
    temp = partition(s8,6)
    temp = xe(temp)
    print(temp)
    