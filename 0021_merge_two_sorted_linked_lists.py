'''
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
[1] -> [2] -> [4]
(1) -> (3) -> (4)

[1] -> (1) -> [2] -> (3) -> [4] -> (4)

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deep(
        self,
        head: Optional[ListNode],
        other: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head.next is None:
            if other is not None:
                head.next, other = other, None
                return head
            else:
                return head
        if head.next.val <= other.val:
            return self.deep(head.next, other)
        else:
            head.next, other = other, head.next
            return self.deep(head.next, other)

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            head = list1
            other = list2
            self.deep(head, other)
        else:
            head = list2
            other = list1
            self.deep(head, other)

        return head

    @staticmethod
    def repr(l: Optional[ListNode]) -> str:
        if l is None:
            return None
        result = list()
        l_ = l
        while True:
            result.append(str(l_.val))
            if l_.next is None:
                break
            else:
                l_ = l_.next
        return "->".join(result)


sol = Solution()

list1 = ListNode(1, ListNode(3, ListNode(8)))
list2 = ListNode(5, ListNode(6, ListNode(9)))
assert sol.repr(sol.mergeTwoLists(list1, list2)) == "1->3->5->6->8->9"

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
assert sol.repr(sol.mergeTwoLists(list1, list2)) == "1->1->2->3->4->4"

list1 = None
list2 = None
assert sol.repr(sol.mergeTwoLists(list1, list2)) is None

list1 = ListNode(1)
list2 = None
assert sol.repr(sol.mergeTwoLists(list1, list2)) == "1"

list1 = None
list2 = ListNode(1)
assert sol.repr(sol.mergeTwoLists(list1, list2)) == "1"

list1 = None
list2 = ListNode(1, ListNode(2))
assert sol.repr(sol.mergeTwoLists(list1, list2)) == "1->2"

list1 = ListNode(-9, ListNode(3))
list2 = ListNode(5, ListNode(7))
assert sol.repr(sol.mergeTwoLists(list1, list2)) == "-9->3->5->7"


