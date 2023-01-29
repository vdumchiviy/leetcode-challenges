"""
141. Linked List Cycle
Easy
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
 

Example 1:
3 -> 2 -> 0 -> -4 -> 2
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
1 -> 2 -> 1
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
1
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:
The number of the nodes in the list is in the range [0, 10**4].
-10**5 <= Node.val <= 10**5
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        one_step: ListNode = head
        two_step: ListNode = head.next

        while two_step.next is not None or one_step != two_step:
            if two_step.next is None or two_step.next.next is None:
                return False
            if one_step == two_step.next:
                return True
            one_step = one_step.next
            two_step = two_step.next.next

        return False


sol = Solution()
# cycled_node =

# 3 -> 2 -> 0 -> -4 -> 2
A = ListNode(3)
B = ListNode(2)
C = ListNode(0)
D = ListNode(-4)
head = A
A.next = B
B.next = C
C.next = D
D.next = B
assert sol.hasCycle(head) is True


# 1 -> 2 -> 1
A = ListNode(1)
B = ListNode(2)
head = A
A.next = B
B.next = A
assert sol.hasCycle(head) is True


# 3 -> 2 -> 0 -> -4 ->
A = ListNode(3)
B = ListNode(2)
C = ListNode(0)
D = ListNode(-4)
head = A
A.next = B
B.next = C
C.next = D
assert sol.hasCycle(head) is False

# 3 -> 2 -> 0 -> -4 -> 5 ->
A = ListNode(3)
B = ListNode(2)
C = ListNode(0)
D = ListNode(-4)
E = ListNode(5)
head = A
A.next = B
B.next = C
C.next = D
D.next = E
assert sol.hasCycle(head) is False


# 3
A = ListNode(3)
head = A
assert sol.hasCycle(head) is False
