# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case
        if head is None:
            return None
        
        # get the size of the list and keep a pointer to the last node 
        last = head
        size = 1
        while last.next:
            last = last.next
            size += 1
            
        # find which node should be the last one
        last_element = k % size     
        fast, slow = head, head
        while last_element:
            fast = fast.next
            last_element -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # slow is the future last node of the list
        # last is now rewired to the head (making a temporary cyclic list)
        last.next = head
        
        # change the head to the first node after the last node
        head = slow.next
        # disconnect last node's next pointer
        slow.next = None
        return head