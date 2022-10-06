# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head


# solution = Solution()
# assert solution.removeNthFromEnd([1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

def _print_list(head):
    while head:
        print(head.val, )
        head = head.next

    print("\n")


if __name__ == '__main__':
    head = ListNode(1)
    node = head
    for i in [2, 3, 4, 5]:
        node.next = ListNode(i)
        node = node.next

    _print_list(head)

    s = Solution()
    # head = s.removeNthFromEnd(head, 7)
    head = s.removeNthFromEnd(head, 2)

    _print_list(head)
