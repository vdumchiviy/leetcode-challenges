'''
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
1 -> 2 -> 3 -> 4 -> 5
Output: [5,4,3,2,1]
5 -> 4 -> 3 -> 2 -> 1

Example 2:
Input: head = [1,2]
1 -> 2
Output: [2,1]
2 -> 1

Example 3:
Input: head = []
Output: []
 

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:

    def deep(
        self,
        point: Optional[ListNode],
        point_next: Optional[ListNode], 
    ) -> Optional[ListNode]:
        if point_next.next is None:
            point_next.next = point
            return point_next
        else:
            new_head = self.deep(point_next, point_next.next)
            point_next.next = point
            return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None if head is None else self.deep(None, head)
        return new_head


sol = Solution()

head = ListNode(1, ListNode(2))
sol.reverseList(head)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reverseList(head)

sol.reverseList(None)
