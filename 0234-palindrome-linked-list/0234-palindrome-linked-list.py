# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle (slow pointer)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half of the list 
        prev = None 
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # chcek palindrome
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
            
        