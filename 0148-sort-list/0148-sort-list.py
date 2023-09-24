# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.getMid(head) # First node of second list
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
    # Helper function to find mid node and split list into two lists
    def getMid(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        # split the list
        prev.next = None
        # slow is the start of the second partition (even length) or in the exact middle (odd length)
        return slow
        
    # Helper function to merge two sorted lists
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> ListNode:
        if not head2:
            return head1
        dummy_head = ListNode(-1)
        cur = dummy_head
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if not head2:
            cur.next = head1
        else:
            cur.next = head2
        return dummy_head.next