from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 

    Add the two numbers and return the sum as a linked list.
    !!! You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Returns:
        [type]: [description]
    """
    class ListN(ListNode):
        """override ListNode class for adding functionality

        Args:
            ListNode ([type]): [description]
        """

        def __repr__(self):
            """representative layer

            Returns:
                [str]: [representative layer]
            """
            return "ListN(val=" + str(self.val) + ", next={" + str(self.next) + "})"

        def add(self, new_val):
            """adding new node with new_val value to the end of node list

            Args:
                new_val ([Any]): [new value]
            """
            last_value = Solution.ListN(new_val)
            node = self
            while node.next:
                node = node.next
            node.next = last_value

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Adding the two numbers and return the sum as a linked list. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 

        Args:
            l1 (Optional[ListNode]): [linked list.The digits are stored in reverse order, and each of their nodes contains a single digit ]
            l2 (Optional[ListNode]): [linked list.The digits are stored in reverse order, and each of their nodes contains a single digit ]

        Returns:
            Optional[ListNode]: [the sum as a linked list.The digits are stored in reverse order, and each of their nodes contains a single digit ]
        """

        summ = 0
        override = 0
        flag_create_result = True
        while l1 is not None or l2 is not None:

            summ = override + (0 if l1 is None else l1.val) + \
                (0 if l2 is None else l2.val)
            override = 0
            if summ >= 10:
                override = 1
                summ = summ - 10
            if flag_create_result:
                flag_create_result = False
                result: Solution.ListN = Solution.ListN(summ)
            else:
                result.add(summ)

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if override == 1:
            result.add(override)

        return result


p3 = ListNode(5)
p2 = ListNode(4, p3)
l1 = ListNode(3, p2)

p3 = ListNode(4)
p2 = ListNode(4, p3)
p1 = ListNode(7, p2)
l2 = ListNode(1, p1)

solution = Solution()
# l1 = solution.ListN(9)
# l2 = solution.ListN(9)


print(solution.addTwoNumbers(l1, l2))

# list1: Solution.ListN = Solution.ListN(l1.val)
# len_list1 = 1
# while l1.next:
#     len_list1 += 1
#     l1 = l1.next
#     list1.add(l1.val)
# list2: Solution.ListN = Solution.ListN(l2.val)
# len_list2 = 1
# while l2.next:
#     len_list2 += 1
#     l2 = l2.next
#     list2.add(l2.val)

# summ = l1.val + l2.val
# if summ >= 10:
#     override = 1
#     summ = summ - 10

# result: Solution.ListN = Solution.ListN(summ)
# l1 = l1.next
# l2 = l2.next
# if min(len_list1, len_list2) > 1:
#     while x in range(min(len_list1, len_list2)):
#         summ = override + l1.val + l2.val
#         override = 0
#         if summ >= 10:
#             override = 1
#             summ = summ - 10
#         result.add(summ)

# p2 = 0
# flag_continue = True
# while flag_continue:
#     if l1[p1] is None and l2[p2] is None:
#         flag_continue = False
#     else:
#         break
