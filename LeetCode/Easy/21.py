# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        first_head = l1
        second_head = l2

        if first_head.val < second_head.val:
            answer = first_head
            first_head = first_head.next
        else:
            answer = second_head
            second_head = second_head.next

        current_node = answer

        while first_head and second_head:
            if first_head.val < second_head.val:
                current_node.next = first_head
                first_head = first_head.next
            else:
                current_node.next = second_head
                second_head = second_head.next

            current_node = current_node.next

        if first_head:
            current_node.next = first_head
        else:
            current_node.next = second_head

        return answer


if __name__ == "__main__":
    a = Solution().mergeTwoLists(
        ListNode(0),
        None
    )

    print("end")
