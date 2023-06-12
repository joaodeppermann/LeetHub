# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if head is None:
            return None
        if head.next is None:
            return head
        # keep dummy head just to return the orignal head
        dummy_head = ListNode(val=0, next=head)
        # keep track of current good node 
        first, second = head, head.next
        while second is not None:
            # check if you need to get second out or not 
            if second.val == first.val:
                # need to pop the second Node
                first.next = second.next
            else:
                # no need to pop, just keep going 
                first = first.next
            # second pointer always move 
            second = second.next
        return dummy_head.next
        
        