# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count = len(lists)
        if not count:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                firstList = lists[i]
                secondList = lists[i + 1] if i + 1 in range(len(lists)) else None
                mergedLists.append(self.mergeTwoLists(firstList, secondList))
                
            lists = mergedLists
        return lists[0]
        
        
    def mergeTwoLists(self, list1, list2):
        dummyHead = tail = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummyHead.next
