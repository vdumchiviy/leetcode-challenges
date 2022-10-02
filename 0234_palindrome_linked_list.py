'''
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
1 -> 2 -> 2 -> 1
Input: head = [1,2,2,1]
Output: true

Example 2:
1 -> 2
Input: head = [1,2]
Output: false
 

Constraints:
The number of nodes in the list is in the range [1, 10**5].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_solution(self, point: Optional[ListNode]):
        self.f += str(point.val)
        if point.next is None:
            return
        else:
            return self.find_solution(point.next)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.f = ""
        self.find_solution(head)
        return self.f == self.f[::-1]


sol = Solution()

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
assert sol.isPalindrome(head=head) is True

head = ListNode(1, ListNode(2))
assert sol.isPalindrome(head=head) is False

head = ListNode(1)
assert sol.isPalindrome(head=head) is True