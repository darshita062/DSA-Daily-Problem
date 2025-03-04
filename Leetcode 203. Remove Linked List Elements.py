class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def removeElements(head, val):
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next  
            else:
                prev = curr  
            curr = curr.next  

        return dummy.next