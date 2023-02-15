"""237. Delete Node in a Linked List
Medium

Example 1:
4 -> 5 -> 1 -> 9
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should
 become 4 -> 1 -> 9 after calling your function.

Example 2:
4 -> 5 -> 1 -> 9
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should 
become 4 -> 5 -> 9 after calling your function.
 

Constraints:
The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def list_2_listnode(lst: list) -> ListNode:
    if len(lst) == 0:
        return None

    result = None
    prev = None
    lst.reverse()
    for val in lst:
        result = ListNode(val)
        result.next = prev

        prev = result

    return result


def get_node_by_value(head: ListNode, v: int) -> ListNode:
    node = head
    while node is not None:
        if node.val == v:
            return node
        else:
            node = node.next


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node: ListNode = node.next
        node.val = next_node.val
        node.next = next_node.next


sol = Solution()

head = list_2_listnode([4, 1, 5, 9])
node = get_node_by_value(head, 5)
sol.deleteNode(node)
actual = listnode_2_str(head)
expected = "#4#1#9"
assert actual == expected
