# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        # find last node 
        cur = head
        size = 1
        while cur.next:
            cur = cur.next
            size += 1
        # find right place to undo connection 
        last_element = k % size
        fast, slow = head, head
        while last_element:
            fast = fast.next
            last_element -= 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # cur now has the last element
        cur.next = head
        
        head = slow.next
        slow.next = None
        return head