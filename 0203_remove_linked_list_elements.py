"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all 
the nodes of the linked list that has Node.val == val, 
and return the new head.

 

Example 1:
1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:
The number of nodes in the list is in the range [0, 10**4].
1 <= Node.val <= 50
0 <= val <= 50
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listnode_2_str(head: ListNode) -> str:
    result = ""
    node = head
    if node is None:
        return ""
    while node.next is not None:
        result += "#" + str(node.val)
        node = node.next
    result += "#" + str(node.val)
    return result


class Solution:
    def removeElements(
        self,
        head: Optional[ListNode],
        val: int
    ) -> Optional[ListNode]:
        if head is None:
            return None

        node = head
        prev = None

        while True:
            if node is None:
                break

            if node.val == val:
                if prev is None:
                    if node.next is None:
                        return None
                    else:
                        head = node.next
                        node = head
                else:
                    if node.next is None:
                        prev.next = None
                        node = node.next
                    else:
                        prev.next = node.next
                        node = node.next
            else:
                if node.next is None:
                    break
                else:
                    prev = node
                    node = node.next

            # if node.next is None:
            #     break

        return head


# Input: head = [1, 2, 6, 3, 4, 5, 6], val = 6
# Output: [1, 2, 3, 4, 5]
sol = Solution()


head = ListNode(1, ListNode(2, ListNode(
    6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
result = sol.removeElements(head=head, val=6)
assert listnode_2_str(result) == '#1#2#3#4#5'

head = None
result = sol.removeElements(head=head, val=1)
# print(listnode_2_str(result))
assert listnode_2_str(result) == ''

head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
result = sol.removeElements(head=head, val=7)
assert listnode_2_str(result) == ''
