
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        # Find the midpoint
        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next

        # Reverse the second half of the list
        fast = None
        while slow is not None:
            tmp = slow.next
            slow.next = fast
            fast = slow
            slow = tmp

        # Check both halves of the list
        slow = head
        while fast is not None:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next

        return True
        