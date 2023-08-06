# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        save_head = head
        tmp_value = 0
        while l1 or l2 or tmp_value:
            if l1 is not None:
                tmp_value += l1.val
                l1 = l1.next
            if l2 is not None:
                tmp_value += l2.val
                l2 = l2.next
            head.next = ListNode(tmp_value % 10)
            head = head.next
            tmp_value = tmp_value // 10
        return save_head.next