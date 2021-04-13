# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output_list_node = ListNode()
        current_node = output_list_node
        prev_overflow = 0

        while l1 or l2:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            value = l1_val + l2_val + prev_overflow

            new_node = ListNode(value % 10)
            prev_overflow = value // 10

            current_node.next = new_node

            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if prev_overflow > 0:
            current_node.next = ListNode(prev_overflow)

        return output_list_node.next


if __name__ == "__main__":

    input_list_1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    input_list_2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    a = Solution().addTwoNumbers(input_list_1, input_list_2)
