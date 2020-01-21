# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        input_str = ''
        current_head = head
        while current_head:
            input_str += str(current_head.val)
            current_head = current_head.next

        return int(input_str, 2)
